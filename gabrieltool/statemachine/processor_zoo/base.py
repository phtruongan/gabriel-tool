
# -*- coding: utf-8 -*-
"""Abstract base classes for processors
"""
import cv2
from cv2 import dnn
import numpy as np
from logzero import logger


class StatefulProcessor(object):
    """Represent a stateful processor.

    A stateful processor's context needs to be initialized when running.
    """
    def init():
        raise NotImplementedError()

    def clean():
        raise NotImplementedError()


class FasterRCNNOpenCVProcessor(StatefulProcessor):
    def __init__(self, proto_path, model_path, labels=None, *args, **kwargs):
        # For default parameter settings,
        # see: https://github.com/rbgirshick/fast-rcnn/blob/b612190f279da3c11dd8b1396dd5e72779f8e463/lib/fast_rcnn/config.py
        self._scale = 600
        self._max_size = 1000
        # Pixel mean values (BGR order) as a (1, 1, 3) array
        # We use the same pixel mean for all networks even though it's not exactly what
        # they were trained with
        self._pixel_means = [102.9801, 115.9465, 122.7717]
        self._nms_threshold = 0.3
        self._labels = labels
        self._net = cv2.dnn.readNetFromCaffe(proto_path, model_path)
        return super(FasterRCNNOpenCVProcessor, self).__init__(*args, **kwargs)

    def _getOutputsNames(self, net):
        layersNames = net.getLayerNames()
        return [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    def __call__(self, image, conf_threshold=0.8):
        height, width = image.shape[:2]

        # resize image to correct size
        im_size_min = np.min(image.shape[0:2])
        im_size_max = np.max(image.shape[0:2])
        im_scale = float(self._scale) / float(im_size_min)
        # Prevent the biggest axis from being more than MAX_SIZE
        if np.round(im_scale * im_size_max) > self._max_size:
            im_scale = float(self._max_size) / float(im_size_max)
        im = cv2.resize(image, None, None, fx=im_scale, fy=im_scale,
                        interpolation=cv2.INTER_LINEAR)
        # create input data
        blob = cv2.dnn.blobFromImage(im, 1, (width, height), self._pixel_means,
                                     swapRB=False, crop=False)
        imInfo = np.array([height, width, im_scale], dtype=np.float32)
        self._net.setInput(blob, 'data')
        self._net.setInput(imInfo, 'im_info')

        # infer
        outs = self._net.forward(self._getOutputsNames(self._net))
        t, _ = self._net.getPerfProfile()
        logger.debug('Inference time: %.2f ms' % (t * 1000.0 / cv2.getTickFrequency()))

        # postprocess
        classIds = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out[0, 0]:
                confidence = detection[2]
                if confidence > conf_threshold:
                    left = int(detection[3])
                    top = int(detection[4])
                    right = int(detection[5])
                    bottom = int(detection[6])
                    width = right - left + 1
                    height = bottom - top + 1
                    classIds.append(int(detection[1]) - 1)  # Skip background label
                    confidences.append(float(confidence))
                    boxes.append([left, top, width, height])

        indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, self._nms_threshold)
        results = []
        for i in indices:
            i = i[0]
            box = boxes[i]
            left = box[0]
            top = box[1]
            width = box[2]
            height = box[3]
            classId = classIds[i]
            confidence = confidences[i]
            results.append([left, top, left+width, top+height, confidence, classId])
        return results

    def init():
        pass

    def clean():
        pass
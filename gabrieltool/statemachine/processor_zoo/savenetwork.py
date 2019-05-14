list_net = []
list_labels = []

def findIdx(labels):
    for i in range(len(list_labels)):
        if list_labels[i] == labels:
            return i
    return -1

def saveNet(caffenet, labels):
    list_net.append(caffenet)
    list_labels.append(labels)

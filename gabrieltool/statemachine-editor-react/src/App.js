import React, { Component } from "react";
import Container from "react-bootstrap/lib/Container";
import Row from "react-bootstrap/lib/Row";
import Col from "react-bootstrap/lib/Col";
import Alert from "react-bootstrap/lib/Alert";
import { Diagram } from "./diagram.js";
import "./App.css";
import InfoBox from "./infoBox.js";
import ToolBar from "./toolbar.js";
var fsmPb = require("./wca-state-machine_pb");

function loadFsm(fsmData) {
  console.log("load_fsm called");
  var fsm = null;
  try {
    fsm = new fsmPb.StateMachine.deserializeBinary(fsmData);
  } catch (err) {
    throw err;
  }
  return fsm;
}

class App extends Component {
  constructor(props) {
    super(props);
    this.onImport = this.onImport.bind(this);
    this.state = {
      fsm: null,
      alertMsg: {
        show: false,
        type: "info",
        msg: ""
      }
    };
  }

  render() {
    return (
      <Container>
        <h1>State Machine Visualizer with React</h1>
        {this.state.alertMsg.msg !== "" && (
          <Alert dismissible variant={this.state.alertMsg.type}>
            {this.state.alertMsg.msg}
          </Alert>
        )}
        <Row>
          <Col sm={6} style={{ backgroundColor: "lavender" }}>
            <h4>Diagram</h4>
            <Diagram />
          </Col>
          <Col sm={6}>
            <Row>
              <ToolBar onImport={this.onImport} />
            </Row>
            <Row>
              <InfoBox />
            </Row>
          </Col>
        </Row>
        <footer>
          <Container>
            <span className="text-muted">
              Copyright Carnegie Mellon University
            </span>
          </Container>
        </footer>
      </Container>
    );
  }

  onImport(e, fileArray) {
    fileArray.forEach(result => {
      const e = result[0];
      let fileContent = e.target.result;
      let fsm = null;
      try {
        fsm = loadFsm(fileContent);
      } catch (err) {
        this.setState({
          alertMsg: {
            type: "danger",
            msg: "Incorrect File Format. Failed to import the file."
          }
        });
      }
      this.setState({ fsm: fsm });
      this.setState({
        alertMsg: {
          type: "info",
          msg: "Success! State machine imported."
        }
      });
    });
  }
}

export default App;
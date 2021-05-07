import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
from peers_gui_client import Ui_MainWindow
import json
import commands as co
import socket
import threading
import pyqtgraph as pg
import numpy as np


class MainWindow(QMainWindow, Ui_MainWindow):
    signal = QtCore.pyqtSignal(dict)
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.default_rf_config_filepath = "config/rf_params_ttk.json"
        self.default_anchors_filepath = "config/anchors.json"
        self.request_socket = socket.socket()
        self.stream_socket = socket.socket()
        self.isConnected = 0

        self.ConnectButton.clicked.connect(self.ConnectButtonClicked)
        self.DisconnectButton.clicked.connect(self.DisconnectButtonClicked)
        self.NewAnchorsButton.clicked.connect(self.NewAnchorsButtonClicked)
        self.RelateToMastersButton.clicked.connect(self.RelateToMastersButtonClicked)
        self.ConfigureButton.clicked.connect(self.ConfigureButtonClicked)
        self.StartButton.clicked.connect(self.StartButtonClicked)
        self.StopButton.clicked.connect(self.StopButtonClicked)
        self.StateRequestButton.clicked.connect(self.StateRequestButtonClicked)
        self.AddObjButton.clicked.connect(self.AddObjButtonClicked)
        self.signal.connect(self.process_object)



        self.floor_map.setXRange(0, 5)
        self.floor_map.setYRange(0, 5)
        self.floor_map.showGrid(x=True, y=True)

        self.streamthread = threading.Thread(target=self.streamer)
        self.streamthread.start()

    # @pyqtSlot(str)
    # def signal(self, value):
    #     assert isinstance(value, str)

    def ConnectButtonClicked(self):
        self.request_socket.connect(('192.168.99.52', 5051))
        self.stream_socket.connect(('192.168.99.52', 5052))
        co.send_state_request(self.request_socket)
        msg = co.receive_from_server(self.request_socket)
        print(msg)

        if len(msg["anchors_info"]) > 0:
            for anchor in msg["anchors_info"]:
                anchor["type"] = "anchor"
                if self.is_on_map(anchor)[0] == 0:
                    self.add_object_on_map(anchor)
        if len(msg["tags_info"]) > 0:
            for tag in msg["tags_info"]:
                tag["type"] = "tag"
                if self.is_on_map(tag)[0] == 0:
                    self.add_object_on_map(tag)

        self.isConnected = 1
        self.BeepLabel.setText("Connected")

    def DisconnectButtonClicked(self):
        co.send_disconnect(self.request_socket)
        self.request_socket.close()
        self.stream_socket.close()
        self.isConnected = 0
        self.BeepLabel.setText("DisConnected")


    def NewAnchorsButtonClicked(self):
        anchors_conf = self.read_anchors_file(self.default_anchors_filepath)
        print(anchors_conf)
        for anchor in anchors_conf:
            co.send_anchor_info(anchor, self.request_socket)
        self.BeepLabel.setText("Sended")


    def RelateToMastersButtonClicked(self):
        co.send_relate_to_masters(self.request_socket)
        self.BeepLabel.setText("Related")

        # co.send_state_request(self.request_socket)
        # msg = co.receive_from_server(self.request_socket)
        #
        # if len(msg["anchors_info"]) > 0:
        #     for anchor in msg["anchors_info"]:
        #         anchor["type"] = "anchor"
        #         if self.is_on_map(anchor) == 0:
        #             self.add_object_on_map(anchor)
        # if len(msg["tags_info"]) > 0:
        #     for tag in msg["tags_info"]:
        #         tag["type"] = "tag"
        #         if self.is_on_map(tag) == 0:
        #             self.add_object_on_map(tag)

    def ConfigureButtonClicked(self):
        rf_params = self.read_rf_config_file(self.default_rf_config_filepath)
        co.send_rf_config(rf_params, self.request_socket)
        self.BeepLabel.setText("Configured")

    def StartButtonClicked(self):
        co.send_start(self.request_socket)

    def StopButtonClicked(self):
        co.send_stop(self.request_socket)

    def StateRequestButtonClicked(self):
        co.send_state_request(self.request_socket)
        msg = co.receive_from_server(self.request_socket)
        print(msg)

    def AddObjButtonClicked(self):
        obj = {}
        obj["type"] = "another"
        obj["x"] = np.random.normal()
        obj["y"] = np.random.normal()
        obj["name"] = str(np.random.normal())
        self.add_object_on_map(obj)

    def read_anchors_file(self, filepath):
        anchors_conf = []
        with open(filepath, "r") as file:
            for line in file:
                anchors_conf.append(json.loads(line))
        return anchors_conf

    def read_rf_config_file(self, filepath):
        with open(filepath, "r") as file:
            rf_params = (json.loads(file.read()))
        return rf_params

    def streamer(self):
        while 1:
            if self.isConnected:
                rcv_size = int.from_bytes(self.stream_socket.recv(4), 'little')
                msg = json.loads(self.stream_socket.recv(rcv_size).decode())
                self.signal.emit(msg)
                print(msg)
                self.BeepLabel.setText(json.dumps(msg))
                # if msg["type"] == "tag":
                #     self.process_tag(msg)
                # elif msg["type"] == "anchor":
                #     if self.is_on_map(msg) == 0:
                #         self.add_object_on_map(msg)

    def process_object(self, obj):
        match_flag, num = self.is_on_map(obj)
        if match_flag:
            self.update_object(obj, num)
        else:
            self.add_object_on_map(obj)

    def is_on_map(self, obj):
        match_flag = 0
        num = 0
        for i, item in enumerate(self.floor_map.plotItem.dataItems):
            if item.opts["name"] == obj["name"]:
                match_flag = 1
                num = i
        return match_flag, num

    def add_object_on_map(self, obj):
        if obj["type"] == "anchor":
            item_symbol = 't1'
            item_pen = 'b'
            item_symbol_pen = 'r'
            item_symbol_Brush = '0.2'
        elif obj["type"] == "tag":
            item_symbol = 'o'
            item_pen = 'r'
            item_symbol_pen = 'b'
            item_symbol_Brush = '0.2'
        elif obj["type"] == "another":
            item_symbol = 'o'
            item_pen = 'b'
            item_symbol_pen = 'r'
            item_symbol_Brush = '0.2'

        g = pg.ScatterPlotItem([obj["x"]], [obj["y"]],
                               pen=item_pen,
                               symbol=item_symbol,
                               symbolPen=item_symbol_pen,
                               symbolBrush=item_symbol_Brush,
                               name=obj["name"])
        self.floor_map.addItem(g)

    def update_object(self, obj, num):
        items = self.floor_map.plotItem.dataItems
        items[num].setData([obj["x"]],[obj["y"]])


def main_application():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main_application()
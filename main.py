import sys

from PIL import Image
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
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
        self.default_rf_config_filepath = "config/rf_params_nik.json"
        self.default_anchors_filepath = "config/anchors.json"
        self.request_socket = socket.socket()
        self.stream_socket = socket.socket()
        self.isConnected = 0
        self.tags = []
        self.tags_tail = 10
        self.avatar_dict = {"cc13455": "config/123.png"}
        self.alpha = 0.9

        self.ConnectButton.clicked.connect(self.ConnectButtonClicked)
        self.DisconnectButton.clicked.connect(self.DisconnectButtonClicked)
        self.NewAnchorsButton.clicked.connect(self.NewAnchorsButtonClicked)
        self.RelateToMastersButton.clicked.connect(self.RelateToMastersButtonClicked)
        self.ConfigureButton.clicked.connect(self.ConfigureButtonClicked)
        self.StartButton.clicked.connect(self.StartButtonClicked)
        self.StopButton.clicked.connect(self.StopButtonClicked)
        self.StateRequestButton.clicked.connect(self.StateRequestButtonClicked)
        self.AddMapButton.clicked.connect(self.AddMapButtonClicked)
        self.ClearMapButton.clicked.connect(self.ClearMapButtonClicked)
        self.log_check_box.clicked.connect(self.logcheckboxClicked)
        self.accumulation_mod_check_box.clicked.connect(self.accumulationmodcheckboxClicked)
        self.signal.connect(self.process_object)

        self.floor_map.setXRange(0, 5)
        self.floor_map.setYRange(0, 5)
        self.floor_map.showGrid(x=True, y=True)
        self.floor_map.setLabel('left', 'y', units='m')
        self.floor_map.setLabel('bottom', 'x', units='m')

        self.x0_map_edit.setText("0")
        self.y0_map_edit.setText("0")
        self.x_Range_map_edit.setText("13")
        self.y_Range_map_edit.setText("6")

        self.streamthread = threading.Thread(target=self.streamer)
        self.streamthread.start()


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
                    self.add_object_on_anchor_table(anchor)
                else:
                    self.update_anchor_table_object(anchor)
        if len(msg["tags_info"]) > 0:
            for tag in msg["tags_info"]:
                tag["type"] = "tag"
                if self.is_on_map(tag)[0] == 0:
                    self.add_object_on_map(tag)
                    self.add_object_on_tags_table(tag)
                else:
                    self.update_tags_table_object(tag)

                match_flag = 0
                for tag1 in self.tags:
                    if tag1["name"] == tag["name"]:
                        match_flag = 1
                        tag1["x"].append(tag["x"])
                        tag1["y"].append(tag["y"])
                        if len(tag1["x"]) > self.tags_tail:
                            del tag1["x"][0]
                            del tag1["y"][0]
                        break
                if match_flag == 0:
                    new_tag = {}
                    new_tag["name"] = tag["name"]
                    new_tag["x"] = []
                    new_tag["x"].append(tag["x"])
                    new_tag["y"] = []
                    new_tag["y"].append(tag["y"])
                    self.tags.append(new_tag)

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
        self.BeepLabel.setText(json.dumps(msg))

    def AddMapButtonClicked(self):
        # self.ClearMapButtonClicked()
        img = Image.open('config/map.png')
        img_data = np.flipud(np.array(img))
        img = pg.ImageItem(img_data.transpose([1, 0, 2]), name="map")
        x0 = int(self.x0_map_edit.text())
        y0 = int(self.y0_map_edit.text())
        xR = int(self.x_Range_map_edit.text())
        yR = int(self.y_Range_map_edit.text())
        rect = QRect(x0, y0, xR, yR)
        img.setRect(rect)
        self.floor_map.addItem(img)

    def ClearMapButtonClicked(self):
        for item in self.floor_map.plotItem.items:
            try:
                opts = item.opts
            except:
                self.floor_map.removeItem(item)

    def logcheckboxClicked(self):
        if self.log_check_box.isChecked():
            co.send_log_enable(self.request_socket)
        else:
            co.send_log_disable(self.request_socket)

    def accumulationmodcheckboxClicked(self):
        if self.accumulation_mod_check_box.isChecked():
            buf_len = int(self.buflen_edit.text())
            co.send_accumulation_on(self.request_socket, buf_len)
        else:
            co.send_accumulation_off(self.request_socket)



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

    def process_object(self, obj):
        match_flag, num = self.is_on_map(obj)
        if match_flag:
            self.update_object(obj, num)
            if obj["type"] == "tag":
                self.update_tags_table_object(obj)
            if obj["type"] == "anchor":
                self.update_anchor_table_object(obj)
        else:
            self.add_object_on_map(obj)
            if obj["type"] == "tag":
                self.add_object_on_tags_table(obj)
            elif obj["type"] == "anchor":
                self.add_object_on_anchor_table(obj)


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
            item_pen = 'r'
            item_symbol_pen = 'r'
            item_symbol_Brush = '0.8'
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

        # match_flag = 0
        # for tag in self.avatar_dict:
        #     if tag["key"] == obj["name"]:
        #         pic = tag["value"]
        #         match_flag = 1
        #         break

        # if match_flag:
        #     img = Image.open(pic)
        #     img_data = np.flipud(np.array(img))
        #     g = pg.ImageItem(img_data.transpose([1, 0, 2]), name=obj["name"])
        #
        # else:
        if obj["type"] == "tag":
            g = pg.PlotCurveItem([obj["x"]], [obj["y"]],
                                   width=3,
                                   pen=pg.mkPen(width=3, color='r'),
                                   symbol=item_symbol,
                                   symbolPen=item_symbol_pen,
                                   symbolBrush=item_symbol_Brush,
                                   name=obj["name"])
        else:
            g = pg.ScatterPlotItem([obj["x"]], [obj["y"]],
                                   size=10,
                                   pen=item_pen,
                                   symbol=item_symbol,
                                   symbolPen=item_symbol_pen,
                                   symbolBrush=item_symbol_Brush,
                                   name=obj["name"])

        self.floor_map.addItem(g)

    def add_object_on_anchor_table(self, obj):
        numRows = self.anchors_table.rowCount()
        self.anchors_table.insertRow(numRows)
        self.anchors_table.setItem(numRows, 0, QTableWidgetItem(obj["name"]))
        self.anchors_table.setItem(numRows, 1, QTableWidgetItem(obj["IP"]))
        self.anchors_table.setItem(numRows, 2, QTableWidgetItem(str(round(obj["x"], 2))))
        self.anchors_table.setItem(numRows, 3, QTableWidgetItem(str(round(obj["y"], 2))))
        self.anchors_table.setItem(numRows, 4, QTableWidgetItem(str(round(obj["z"], 2))))
        if obj["role"] == "Master":
            obj["master_name"] = "-"
        self.anchors_table.setItem(numRows, 5, QTableWidgetItem(obj["master_name"]))
        self.anchors_table.setItem(numRows, 6, QTableWidgetItem(obj["role"]))
        if obj["connection"] == 1:
            connect_item = QTableWidgetItem("Online")
            connect_color = QtGui.QColor(0, 255, 0)
        elif obj["connection"] == 0:
            connect_item = QTableWidgetItem("Offline")
            connect_color = QtGui.QColor(255, 0, 0)
        self.anchors_table.setItem(numRows, 7, connect_item)
        self.anchors_table.item(numRows, 7).setForeground(connect_color)
        if obj["sync_flag"] == 1:
            sync_item = QTableWidgetItem("Synchronized")
            sync_color =  QtGui.QColor(0, 255, 0)
        elif obj["sync_flag"] == 0:
            sync_item = QTableWidgetItem("Synchronization Lost")
            sync_color = QtGui.QColor(255, 0, 0)
        self.anchors_table.setItem(numRows, 8, sync_item)
        self.anchors_table.item(numRows, 8).setForeground(sync_color)
        self.anchors_table.setItem(numRows, 9, QTableWidgetItem(str(obj["ADRx"])))
        self.anchors_table.setItem(numRows, 10, QTableWidgetItem(str(obj["ADTx"])))

    def add_object_on_tags_table(self, obj):
        numRows = self.tags_table.rowCount()
        self.tags_table.insertRow(numRows)
        self.tags_table.setItem(numRows, 0, QTableWidgetItem(obj["name"]))
        self.tags_table.setItem(numRows, 1, QTableWidgetItem(str(round(obj["x"], 2))))
        self.tags_table.setItem(numRows, 2, QTableWidgetItem(str(round(obj["y"], 2))))
        self.tags_table.setItem(numRows, 3, QTableWidgetItem(str(round(obj["z"], 2))))
        self.tags_table.setItem(numRows, 4, QTableWidgetItem(str(round(obj["dop"], 2))))
        if obj["dop"] < 1.5:
            dop_color = QtGui.QColor(0, 255, 0)
        elif obj["dop"] < 3.0:
            dop_color = QtGui.QColor(255, 255, 0)
        else:
            dop_color = QtGui.QColor(255, 0, 0)
        self.tags_table.item(numRows, 4).setForeground(dop_color)
        self.tags_table.setItem(numRows, 5, QTableWidgetItem(str(round(obj["lifetime"], 2))))


    def update_object(self, obj, num):

        match_flag = 0
        for tag1 in self.tags:
            if tag1["name"] == obj["name"]:
                match_flag = 1
                tag1["x"].append(obj["x"] * (1 - self.alpha) + self.alpha * tag1["x"][-1])
                tag1["y"].append(obj["y"] * (1 - self.alpha) + self.alpha * tag1["y"][-1])
                if len(tag1["x"]) > self.tags_tail:
                    del tag1["x"][0]
                    del tag1["y"][0]
                break
        if match_flag == 0:
            tag1 = {}
            tag1["name"] = obj["name"]
            tag1["x"] = []
            tag1["x"].append(obj["x"])
            tag1["y"] = []
            tag1["y"].append(obj["y"])
            self.tags.append(tag1)
        x_sorted = sorted(tag1["x"])
        y_sorted = sorted(tag1["y"])
        items = self.floor_map.plotItem.dataItems
        if len(tag1["x"]) == self.tags_tail:
            #items[num].setData([x_sorted[int(self.tags_tail/2)]], [y_sorted[int(self.tags_tail/2)]])
            items[num].setData(tag1["x"], tag1["y"])


    def update_anchor_table_object(self, obj):
        numRows = self.anchors_table.rowCount()
        for i in range(numRows):
            if obj["name"] == self.anchors_table.item(i, 0).text():
                self.anchors_table.setItem(i, 2, QTableWidgetItem(str(round(obj["x"], 2))))
                self.anchors_table.setItem(i, 3, QTableWidgetItem(str(round(obj["y"], 2))))
                self.anchors_table.setItem(i, 4, QTableWidgetItem(str(round(obj["z"], 2))))
                if obj["role"] == "Master":
                    obj["master_name"] = "-"
                self.anchors_table.setItem(i, 5, QTableWidgetItem(obj["master_name"]))
                self.anchors_table.setItem(i, 6, QTableWidgetItem(obj["role"]))
                if obj["connection"] == 1:
                    connect_item = QTableWidgetItem("Online")
                    connect_color = QtGui.QColor(0, 255, 0)
                elif obj["connection"] == 0:
                    connect_item = QTableWidgetItem("Offline")
                    connect_color = QtGui.QColor(255, 0, 0)
                self.anchors_table.setItem(i, 7, connect_item)
                self.anchors_table.item(i, 7).setForeground(connect_color)
                if obj["sync_flag"] == 1:
                    sync_item = QTableWidgetItem("Synchronized")
                    sync_color = QtGui.QColor(0, 255, 0)
                elif obj["sync_flag"] == 0:
                    sync_item = QTableWidgetItem("Synchronization Lost")
                    sync_color = QtGui.QColor(255, 0, 0)
                self.anchors_table.setItem(i, 8, sync_item)
                self.anchors_table.item(i, 8).setForeground(sync_color)
                self.anchors_table.setItem(i, 9, QTableWidgetItem(str(obj["ADRx"])))
                self.anchors_table.setItem(i, 10, QTableWidgetItem(str(obj["ADTx"])))
                break

    def update_tags_table_object(self, obj):
        numRows = self.tags_table.rowCount()
        for i in range(numRows):
            if obj["name"] == self.tags_table.item(i, 0).text():
                self.tags_table.setItem(i, 1, QTableWidgetItem(str(round(obj["x"], 2))))
                self.tags_table.setItem(i, 2, QTableWidgetItem(str(round(obj["y"], 2))))
                self.tags_table.setItem(i, 3, QTableWidgetItem(str(round(obj["z"], 2))))
                self.tags_table.setItem(i, 4, QTableWidgetItem(str(round(obj["dop"], 2))))
                if obj["dop"] < 1.5:
                    dop_color = QtGui.QColor(0, 255, 0)
                elif obj["dop"] < 3.0:
                    dop_color = QtGui.QColor(255, 255, 0)
                else:
                    dop_color = QtGui.QColor(255, 0, 0)
                self.tags_table.item(i, 4).setForeground(dop_color)
                self.tags_table.setItem(i, 5, QTableWidgetItem(str(round(obj["lifetime"], 2))))
                break



def main_application():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main_application()

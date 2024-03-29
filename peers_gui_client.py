# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'peers_gui_client.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1597, 812)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 280, 181, 191))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 160, 160))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.AddMapButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.AddMapButton.setObjectName("AddMapButton")
        self.verticalLayout_2.addWidget(self.AddMapButton)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.x0_map_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.x0_map_edit.setObjectName("x0_map_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.x0_map_edit)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.y0_map_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.y0_map_edit.setObjectName("y0_map_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.y0_map_edit)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.x_Range_map_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.x_Range_map_edit.setObjectName("x_Range_map_edit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.x_Range_map_edit)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.y_Range_map_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.y_Range_map_edit.setObjectName("y_Range_map_edit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.y_Range_map_edit)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.ClearMapButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ClearMapButton.setObjectName("ClearMapButton")
        self.verticalLayout_2.addWidget(self.ClearMapButton)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 201, 261))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 80, 179, 111))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_4)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 160, 83))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.NewAnchorsButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.NewAnchorsButton.setObjectName("NewAnchorsButton")
        self.verticalLayout_3.addWidget(self.NewAnchorsButton)
        self.RelateToMastersButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.RelateToMastersButton.setObjectName("RelateToMastersButton")
        self.verticalLayout_3.addWidget(self.RelateToMastersButton)
        self.ConfigureButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.ConfigureButton.setObjectName("ConfigureButton")
        self.verticalLayout_3.addWidget(self.ConfigureButton)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 20, 179, 61))
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 158, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ConnectButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ConnectButton.setObjectName("ConnectButton")
        self.horizontalLayout.addWidget(self.ConnectButton)
        self.DisconnectButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.DisconnectButton.setObjectName("DisconnectButton")
        self.horizontalLayout.addWidget(self.DisconnectButton)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 200, 181, 51))
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_6)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 160, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.StartButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.StartButton.setObjectName("StartButton")
        self.horizontalLayout_2.addWidget(self.StartButton)
        self.StopButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.StopButton.setObjectName("StopButton")
        self.horizontalLayout_2.addWidget(self.StopButton)
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(220, 10, 1361, 51))
        self.groupBox_7.setObjectName("groupBox_7")
        self.StateRequestButton = QtWidgets.QPushButton(self.groupBox_7)
        self.StateRequestButton.setGeometry(QtCore.QRect(10, 20, 158, 23))
        self.StateRequestButton.setObjectName("StateRequestButton")
        self.BeepLabel = QtWidgets.QLabel(self.groupBox_7)
        self.BeepLabel.setGeometry(QtCore.QRect(170, 20, 1181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.BeepLabel.setFont(font)
        self.BeepLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BeepLabel.setText("")
        self.BeepLabel.setObjectName("BeepLabel")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(230, 60, 1341, 711))
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.floor_map = PlotWidget(self.tab)
        self.floor_map.setGeometry(QtCore.QRect(10, 10, 1311, 661))
        self.floor_map.setObjectName("floor_map")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 10, 1221, 341))
        self.groupBox_5.setObjectName("groupBox_5")
        self.tags_table = QtWidgets.QTableWidget(self.groupBox_5)
        self.tags_table.setGeometry(QtCore.QRect(10, 20, 1191, 311))
        self.tags_table.setObjectName("tags_table")
        self.tags_table.setColumnCount(6)
        self.tags_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tags_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tags_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tags_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tags_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tags_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tags_table.setHorizontalHeaderItem(5, item)
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 360, 1221, 281))
        self.groupBox_8.setObjectName("groupBox_8")
        self.anchors_table = QtWidgets.QTableWidget(self.groupBox_8)
        self.anchors_table.setGeometry(QtCore.QRect(10, 20, 1201, 251))
        self.anchors_table.setMaximumSize(QtCore.QSize(16777215, 16777213))
        self.anchors_table.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.anchors_table.setObjectName("anchors_table")
        self.anchors_table.setColumnCount(11)
        self.anchors_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.anchors_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.anchors_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.anchors_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.anchors_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.anchors_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.anchors_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.anchors_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.anchors_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.anchors_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.anchors_table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.anchors_table.setHorizontalHeaderItem(10, item)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 480, 97, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.log_check_box = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.log_check_box.setObjectName("log_check_box")
        self.verticalLayout.addWidget(self.log_check_box)
        self.accumulation_mod_check_box = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.accumulation_mod_check_box.setObjectName("accumulation_mod_check_box")
        self.verticalLayout.addWidget(self.accumulation_mod_check_box)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.buflen_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.buflen_edit.setObjectName("buflen_edit")
        self.horizontalLayout_3.addWidget(self.buflen_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1597, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Floor Map"))
        self.AddMapButton.setText(_translate("MainWindow", "Add map"))
        self.label.setText(_translate("MainWindow", "x_0"))
        self.label_2.setText(_translate("MainWindow", "y_0"))
        self.label_3.setText(_translate("MainWindow", "x_Range"))
        self.label_4.setText(_translate("MainWindow", "y_Range"))
        self.ClearMapButton.setText(_translate("MainWindow", "Clear"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Control Panel"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Anchors configuration"))
        self.NewAnchorsButton.setText(_translate("MainWindow", "Send Anchors"))
        self.RelateToMastersButton.setText(_translate("MainWindow", "Relate to masters"))
        self.ConfigureButton.setText(_translate("MainWindow", "Configure"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Connection"))
        self.ConnectButton.setText(_translate("MainWindow", "Connect"))
        self.DisconnectButton.setText(_translate("MainWindow", "Disconnect"))
        self.groupBox_6.setTitle(_translate("MainWindow", "RTLS"))
        self.StartButton.setText(_translate("MainWindow", "Start"))
        self.StopButton.setText(_translate("MainWindow", "Stop"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Console log"))
        self.StateRequestButton.setText(_translate("MainWindow", "State Request"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Map"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Tags"))
        item = self.tags_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tags_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "x"))
        item = self.tags_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "y"))
        item = self.tags_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "z"))
        item = self.tags_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "DOP"))
        item = self.tags_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Lifetime"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Anchors"))
        item = self.anchors_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.anchors_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "IP"))
        item = self.anchors_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "x"))
        item = self.anchors_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "y"))
        item = self.anchors_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "z"))
        item = self.anchors_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Master"))
        item = self.anchors_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Role"))
        item = self.anchors_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Connection"))
        item = self.anchors_table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Synchronized"))
        item = self.anchors_table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "ADRx"))
        item = self.anchors_table.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "ADTx"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Info"))
        self.log_check_box.setText(_translate("MainWindow", "log_enable"))
        self.accumulation_mod_check_box.setText(_translate("MainWindow", "accumulation"))
        self.label_5.setText(_translate("MainWindow", "buf len"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

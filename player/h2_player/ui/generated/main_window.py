# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(613, 574)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(512, 512))
        self.groupBox.setCursor(QCursor(Qt.IBeamCursor))
        self.groupBox.setCheckable(False)
        self.icon_label = QLabel(self.groupBox)
        self.icon_label.setObjectName(u"icon_label")
        self.icon_label.setGeometry(QRect(20, 40, 100, 100))

        self.horizontalLayout_2.addWidget(self.groupBox)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.icon_index_spinbox = QSpinBox(self.centralwidget)
        self.icon_index_spinbox.setObjectName(u"icon_index_spinbox")
        self.icon_index_spinbox.setMaximum(1000)
        self.icon_index_spinbox.setValue(74)

        self.verticalLayout.addWidget(self.icon_index_spinbox)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.sprite_start_spinbox = QSpinBox(self.centralwidget)
        self.sprite_start_spinbox.setObjectName(u"sprite_start_spinbox")

        self.verticalLayout.addWidget(self.sprite_start_spinbox)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.sprite_end_spinbox = QSpinBox(self.centralwidget)
        self.sprite_end_spinbox.setObjectName(u"sprite_end_spinbox")
        self.sprite_end_spinbox.setValue(9)

        self.verticalLayout.addWidget(self.sprite_end_spinbox)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.fps_spinbox = QDoubleSpinBox(self.centralwidget)
        self.fps_spinbox.setObjectName(u"fps_spinbox")
        self.fps_spinbox.setValue(5.000000000000000)

        self.verticalLayout.addWidget(self.fps_spinbox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.current_frame_label = QLabel(self.centralwidget)
        self.current_frame_label.setObjectName(u"current_frame_label")

        self.verticalLayout.addWidget(self.current_frame_label)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 613, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"_Quit", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Icon Rendering", None))
        self.icon_label.setText(QCoreApplication.translate("MainWindow", u"icon", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Icon Index", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Start Sprite", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"End Sprite", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"FPS", None))
        self.current_frame_label.setText(QCoreApplication.translate("MainWindow", u"1", None))
    # retranslateUi


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
        MainWindow.resize(565, 417)
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

        self.icon_index_edit = QLineEdit(self.centralwidget)
        self.icon_index_edit.setObjectName(u"icon_index_edit")

        self.verticalLayout.addWidget(self.icon_index_edit)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.sprite_start_spin = QSpinBox(self.centralwidget)
        self.sprite_start_spin.setObjectName(u"sprite_start_spin")

        self.verticalLayout.addWidget(self.sprite_start_spin)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.sprite_end_spin = QLineEdit(self.centralwidget)
        self.sprite_end_spin.setObjectName(u"sprite_end_spin")

        self.verticalLayout.addWidget(self.sprite_end_spin)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.fps_edit = QLineEdit(self.centralwidget)
        self.fps_edit.setObjectName(u"fps_edit")

        self.verticalLayout.addWidget(self.fps_edit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.animate_button = QPushButton(self.centralwidget)
        self.animate_button.setObjectName(u"animate_button")

        self.horizontalLayout.addWidget(self.animate_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 565, 22))
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
        self.icon_index_edit.setText(QCoreApplication.translate("MainWindow", u"74", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Start Sprite", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"End Sprite", None))
        self.sprite_end_spin.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"FPS", None))
        self.fps_edit.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.animate_button.setText(QCoreApplication.translate("MainWindow", u"Animate", None))
    # retranslateUi


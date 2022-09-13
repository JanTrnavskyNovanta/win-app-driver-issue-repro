# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
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
        MainWindow.resize(800, 600)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionDummyAnother = QAction(MainWindow)
        self.actionDummyAnother.setObjectName(u"actionDummyAnother")
        self.actionAnother_option1 = QAction(MainWindow)
        self.actionAnother_option1.setObjectName(u"actionAnother_option1")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 60, 80, 21))
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(30, 100, 84, 19))
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(30, 30, 72, 19))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAnother_Option = QMenu(self.menubar)
        self.menuAnother_Option.setObjectName(u"menuAnother_Option")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAnother_Option.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionDummyAnother)
        self.menuAnother_Option.addAction(self.actionAnother_option1)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"DummyNew", None))
        self.actionDummyAnother.setText(QCoreApplication.translate("MainWindow", u"DummyAnother", None))
        self.actionAnother_option1.setText(QCoreApplication.translate("MainWindow", u"Another option1", None))
#if QT_CONFIG(accessibility)
        self.pushButton.setAccessibleName(QCoreApplication.translate("MainWindow", u"TestButton", None))
#endif // QT_CONFIG(accessibility)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
#if QT_CONFIG(accessibility)
        self.radioButton.setAccessibleName(QCoreApplication.translate("MainWindow", u"TestRadioButton", None))
#endif // QT_CONFIG(accessibility)
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
#if QT_CONFIG(accessibility)
        self.checkBox.setAccessibleName(QCoreApplication.translate("MainWindow", u"TestCheckBox", None))
#endif // QT_CONFIG(accessibility)
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAnother_Option.setTitle(QCoreApplication.translate("MainWindow", u"Another Option", None))
    # retranslateUi


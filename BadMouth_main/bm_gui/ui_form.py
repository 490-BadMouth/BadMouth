# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
        MainWindow.resize(1280, 720)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(154, 153, 150, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(231, 230, 225, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(192, 191, 187, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(77, 77, 75, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(103, 102, 100, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush7 = QBrush(QColor(204, 204, 202, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        brush8 = QBrush(QColor(255, 255, 220, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush9 = QBrush(QColor(0, 0, 0, 127))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush10 = QBrush(QColor(239, 239, 239, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush6)
        brush11 = QBrush(QColor(202, 202, 202, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush11)
        brush12 = QBrush(QColor(159, 159, 159, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush12)
        brush13 = QBrush(QColor(184, 184, 184, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        brush14 = QBrush(QColor(118, 118, 118, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush14)
        brush15 = QBrush(QColor(247, 247, 247, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush15)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        brush16 = QBrush(QColor(0, 0, 0, 128))
        brush16.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush17 = QBrush(QColor(177, 177, 177, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush17)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush15)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#endif
        MainWindow.setPalette(palette)
        MainWindow.setAnimated(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 221, 681))
        self.verticalLayout_buttons = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_buttons.setObjectName(u"verticalLayout_buttons")
        self.verticalLayout_buttons.setContentsMargins(0, 0, 0, 0)
        self.pushButton_home = QPushButton(self.verticalLayoutWidget)
        self.pushButton_home.setObjectName(u"pushButton_home")
        self.pushButton_home.setMaximumSize(QSize(16777215, 125))
        self.pushButton_home.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setFamily(u"Ubuntu")
        font.setPointSize(36)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setAutoFillBackground(False)

        self.verticalLayout_buttons.addWidget(self.pushButton_home)

        self.pushButton_eq = QPushButton(self.verticalLayoutWidget)
        self.pushButton_eq.setObjectName(u"pushButton_eq")
        self.pushButton_eq.setMaximumSize(QSize(16777215, 125))
        self.pushButton_eq.setBaseSize(QSize(0, 0))
        self.pushButton_eq.setFont(font)
        self.pushButton_eq.setAutoFillBackground(False)

        self.verticalLayout_buttons.addWidget(self.pushButton_eq)

        self.pushButton_vis = QPushButton(self.verticalLayoutWidget)
        self.pushButton_vis.setObjectName(u"pushButton_vis")
        self.pushButton_vis.setMaximumSize(QSize(16777215, 125))
        self.pushButton_vis.setBaseSize(QSize(0, 0))
        self.pushButton_vis.setFont(font)
        self.pushButton_vis.setAutoFillBackground(False)

        self.verticalLayout_buttons.addWidget(self.pushButton_vis)

        self.pushButton_stats = QPushButton(self.verticalLayoutWidget)
        self.pushButton_stats.setObjectName(u"pushButton_stats")
        self.pushButton_stats.setMaximumSize(QSize(16777215, 125))
        self.pushButton_stats.setBaseSize(QSize(0, 0))
        self.pushButton_stats.setFont(font)
        self.pushButton_stats.setAutoFillBackground(False)

        self.verticalLayout_buttons.addWidget(self.pushButton_stats)

        self.frame_content = QFrame(self.centralwidget)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setGeometry(QRect(260, 20, 1001, 681))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush12)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush14)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush17)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
#endif
        self.frame_content.setPalette(palette1)
        font1 = QFont()
        font1.setPointSize(10)
        self.frame_content.setFont(font1)
        self.frame_content.setAutoFillBackground(False)
        self.frame_content.setFrameShape(QFrame.WinPanel)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.frame_content.setLineWidth(0)
        self.frame_content.setMidLineWidth(0)
        self.stackedWidget_content = QStackedWidget(self.frame_content)
        self.stackedWidget_content.setObjectName(u"stackedWidget_content")
        self.stackedWidget_content.setGeometry(QRect(1, 1, 999, 679))
        self.stackedWidget_content.setLineWidth(0)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.stackedWidget_content.addWidget(self.page_home)
        self.page_eq = QWidget()
        self.page_eq.setObjectName(u"page_eq")
        self.horizontalLayoutWidget = QWidget(self.page_eq)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 120, 961, 261))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(150)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.dial_2 = QDial(self.horizontalLayoutWidget)
        self.dial_2.setObjectName(u"dial_2")
        self.dial_2.setNotchesVisible(True)

        self.horizontalLayout.addWidget(self.dial_2)

        self.dial_3 = QDial(self.horizontalLayoutWidget)
        self.dial_3.setObjectName(u"dial_3")
        self.dial_3.setNotchesVisible(True)

        self.horizontalLayout.addWidget(self.dial_3)

        self.dial = QDial(self.horizontalLayoutWidget)
        self.dial.setObjectName(u"dial")
        self.dial.setNotchesVisible(True)

        self.horizontalLayout.addWidget(self.dial)

        self.horizontalLayoutWidget_2 = QWidget(self.page_eq)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 40, 961, 80))
        self.horizontalLayout_eq_labels = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_eq_labels.setSpacing(150)
        self.horizontalLayout_eq_labels.setObjectName(u"horizontalLayout_eq_labels")
        self.horizontalLayout_eq_labels.setContentsMargins(0, 0, 0, 0)
        self.label_bass = QLabel(self.horizontalLayoutWidget_2)
        self.label_bass.setObjectName(u"label_bass")
        font2 = QFont()
        font2.setPointSize(36)
        self.label_bass.setFont(font2)
        self.label_bass.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_eq_labels.addWidget(self.label_bass)

        self.label_mid = QLabel(self.horizontalLayoutWidget_2)
        self.label_mid.setObjectName(u"label_mid")
        self.label_mid.setFont(font2)
        self.label_mid.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_eq_labels.addWidget(self.label_mid)

        self.label_treb = QLabel(self.horizontalLayoutWidget_2)
        self.label_treb.setObjectName(u"label_treb")
        self.label_treb.setFont(font2)
        self.label_treb.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_eq_labels.addWidget(self.label_treb)

        self.horizontalLayoutWidget_3 = QWidget(self.page_eq)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(19, 379, 961, 91))
        self.horizontalLayout_eq_7segs = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_eq_7segs.setObjectName(u"horizontalLayout_eq_7segs")
        self.horizontalLayout_eq_7segs.setContentsMargins(0, 0, 0, 0)
        self.lcdNumber_3 = QLCDNumber(self.horizontalLayoutWidget_3)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")
        self.lcdNumber_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_eq_7segs.addWidget(self.lcdNumber_3)

        self.lcdNumber_2 = QLCDNumber(self.horizontalLayoutWidget_3)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_eq_7segs.addWidget(self.lcdNumber_2)

        self.lcdNumber = QLCDNumber(self.horizontalLayoutWidget_3)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_eq_7segs.addWidget(self.lcdNumber)

        self.stackedWidget_content.addWidget(self.page_eq)
        self.page_vis = QWidget()
        self.page_vis.setObjectName(u"page_vis")
        self.gridLayoutWidget = QWidget(self.page_vis)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(9, 9, 981, 661))
        self.gridLayout_plot = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_plot.setObjectName(u"gridLayout_plot")
        self.gridLayout_plot.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_content.addWidget(self.page_vis)
        self.page_stats = QWidget()
        self.page_stats.setObjectName(u"page_stats")
        self.stackedWidget_content.addWidget(self.page_stats)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_content.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BadMouth", None))
        self.pushButton_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_eq.setText(QCoreApplication.translate("MainWindow", u"Equalizer", None))
        self.pushButton_vis.setText(QCoreApplication.translate("MainWindow", u"Visualizer", None))
        self.pushButton_stats.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.label_bass.setText(QCoreApplication.translate("MainWindow", u"Bass", None))
        self.label_mid.setText(QCoreApplication.translate("MainWindow", u"Mid", None))
        self.label_treb.setText(QCoreApplication.translate("MainWindow", u"Treble", None))
    # retranslateUi

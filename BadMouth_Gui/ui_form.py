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
        MainWindow.setAutoFillBackground(False)
        MainWindow.setAnimated(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 268, 681))
        self.verticalLayout_buttons = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_buttons.setObjectName(u"verticalLayout_buttons")
        self.verticalLayout_buttons.setContentsMargins(0, 0, 0, 0)
        self.pushButton_home = QPushButton(self.verticalLayoutWidget)
        self.pushButton_home.setObjectName(u"pushButton_home")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_home.sizePolicy().hasHeightForWidth())
        self.pushButton_home.setSizePolicy(sizePolicy)
        self.pushButton_home.setMaximumSize(QSize(250, 125))
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
        sizePolicy.setHeightForWidth(self.pushButton_eq.sizePolicy().hasHeightForWidth())
        self.pushButton_eq.setSizePolicy(sizePolicy)
        self.pushButton_eq.setMaximumSize(QSize(250, 125))
        self.pushButton_eq.setBaseSize(QSize(0, 0))
        self.pushButton_eq.setFont(font)
        self.pushButton_eq.setAutoFillBackground(False)

        self.verticalLayout_buttons.addWidget(self.pushButton_eq)

        self.pushButton_vis = QPushButton(self.verticalLayoutWidget)
        self.pushButton_vis.setObjectName(u"pushButton_vis")
        sizePolicy.setHeightForWidth(self.pushButton_vis.sizePolicy().hasHeightForWidth())
        self.pushButton_vis.setSizePolicy(sizePolicy)
        self.pushButton_vis.setMaximumSize(QSize(250, 125))
        self.pushButton_vis.setBaseSize(QSize(0, 0))
        self.pushButton_vis.setFont(font)
        self.pushButton_vis.setAutoFillBackground(False)

        self.verticalLayout_buttons.addWidget(self.pushButton_vis)

        self.pushButton_stats = QPushButton(self.verticalLayoutWidget)
        self.pushButton_stats.setObjectName(u"pushButton_stats")
        sizePolicy.setHeightForWidth(self.pushButton_stats.sizePolicy().hasHeightForWidth())
        self.pushButton_stats.setSizePolicy(sizePolicy)
        self.pushButton_stats.setMaximumSize(QSize(250, 125))
        self.pushButton_stats.setBaseSize(QSize(0, 0))
        self.pushButton_stats.setFont(font)
        self.pushButton_stats.setAutoFillBackground(False)

        self.verticalLayout_buttons.addWidget(self.pushButton_stats)

        self.label_UART_in = QLabel(self.verticalLayoutWidget)
        self.label_UART_in.setObjectName(u"label_UART_in")
        font1 = QFont()
        font1.setPointSize(24)
        self.label_UART_in.setFont(font1)
        self.label_UART_in.setAlignment(Qt.AlignCenter)

        self.verticalLayout_buttons.addWidget(self.label_UART_in)

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
        font2 = QFont()
        font2.setPointSize(10)
        self.frame_content.setFont(font2)
        self.frame_content.setAutoFillBackground(False)
        self.frame_content.setFrameShape(QFrame.WinPanel)
        self.frame_content.setFrameShadow(QFrame.Sunken)
        self.frame_content.setLineWidth(0)
        self.frame_content.setMidLineWidth(0)
        self.stackedWidget_content = QStackedWidget(self.frame_content)
        self.stackedWidget_content.setObjectName(u"stackedWidget_content")
        self.stackedWidget_content.setGeometry(QRect(1, 1, 999, 679))
        self.stackedWidget_content.setProperty("", 0)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.pushButton_pato = QPushButton(self.page_home)
        self.pushButton_pato.setObjectName(u"pushButton_pato")
        self.pushButton_pato.setEnabled(True)
        self.pushButton_pato.setGeometry(QRect(100, 60, 799, 600))
        sizePolicy.setHeightForWidth(self.pushButton_pato.sizePolicy().hasHeightForWidth())
        self.pushButton_pato.setSizePolicy(sizePolicy)
        self.pushButton_pato.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setPointSize(36)
        self.pushButton_pato.setFont(font3)
        icon = QIcon()
        icon.addFile(u"bad duck.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"good duck.png", QSize(), QIcon.Normal, QIcon.On)
        icon.addFile(u"bad duck.png", QSize(), QIcon.Disabled, QIcon.Off)
        icon.addFile(u"bad duck.png", QSize(), QIcon.Active, QIcon.Off)
        icon.addFile(u"bad duck.png", QSize(), QIcon.Selected, QIcon.Off)
        self.pushButton_pato.setIcon(icon)
        self.pushButton_pato.setIconSize(QSize(600, 600))
        self.pushButton_pato.setCheckable(True)
        self.pushButton_pato.setChecked(False)
        self.label_enabled = QLabel(self.page_home)
        self.label_enabled.setObjectName(u"label_enabled")
        self.label_enabled.setGeometry(QRect(100, 0, 801, 61))
        self.label_enabled.setFont(font3)
        self.label_enabled.setAlignment(Qt.AlignCenter)
        self.label_disabled = QLabel(self.page_home)
        self.label_disabled.setObjectName(u"label_disabled")
        self.label_disabled.setGeometry(QRect(110, 0, 801, 61))
        self.label_disabled.setFont(font3)
        self.label_disabled.setAlignment(Qt.AlignCenter)
        self.stackedWidget_content.addWidget(self.page_home)
        self.page_eq = QWidget()
        self.page_eq.setObjectName(u"page_eq")
        self.horizontalLayoutWidget = QWidget(self.page_eq)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 130, 951, 241))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.dial_bass = QDial(self.horizontalLayoutWidget)
        self.dial_bass.setObjectName(u"dial_bass")
        self.dial_bass.setMinimum(0)
        self.dial_bass.setMaximum(16)
        self.dial_bass.setValue(8)
        self.dial_bass.setNotchesVisible(True)

        self.horizontalLayout.addWidget(self.dial_bass)

        self.dial_mid = QDial(self.horizontalLayoutWidget)
        self.dial_mid.setObjectName(u"dial_mid")
        self.dial_mid.setMinimum(0)
        self.dial_mid.setMaximum(16)
        self.dial_mid.setValue(8)
        self.dial_mid.setNotchesVisible(True)

        self.horizontalLayout.addWidget(self.dial_mid)

        self.dial_treb = QDial(self.horizontalLayoutWidget)
        self.dial_treb.setObjectName(u"dial_treb")
        self.dial_treb.setMinimum(0)
        self.dial_treb.setMaximum(16)
        self.dial_treb.setValue(8)
        self.dial_treb.setNotchesVisible(True)

        self.horizontalLayout.addWidget(self.dial_treb)

        self.dial_vol = QDial(self.horizontalLayoutWidget)
        self.dial_vol.setObjectName(u"dial_vol")
        self.dial_vol.setMinimumSize(QSize(0, 0))
        self.dial_vol.setMinimum(0)
        self.dial_vol.setMaximum(16)
        self.dial_vol.setValue(16)
        self.dial_vol.setNotchesVisible(True)

        self.horizontalLayout.addWidget(self.dial_vol)

        self.horizontalLayoutWidget_2 = QWidget(self.page_eq)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 40, 971, 81))
        self.horizontalLayout_eq_labels = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_eq_labels.setSpacing(0)
        self.horizontalLayout_eq_labels.setObjectName(u"horizontalLayout_eq_labels")
        self.horizontalLayout_eq_labels.setContentsMargins(0, 0, 0, 0)
        self.label_bass = QLabel(self.horizontalLayoutWidget_2)
        self.label_bass.setObjectName(u"label_bass")
        self.label_bass.setFont(font3)
        self.label_bass.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_eq_labels.addWidget(self.label_bass)

        self.label_mid = QLabel(self.horizontalLayoutWidget_2)
        self.label_mid.setObjectName(u"label_mid")
        self.label_mid.setFont(font3)
        self.label_mid.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_eq_labels.addWidget(self.label_mid)

        self.label_treb = QLabel(self.horizontalLayoutWidget_2)
        self.label_treb.setObjectName(u"label_treb")
        self.label_treb.setFont(font3)
        self.label_treb.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_eq_labels.addWidget(self.label_treb)

        self.label_vol = QLabel(self.horizontalLayoutWidget_2)
        self.label_vol.setObjectName(u"label_vol")
        self.label_vol.setFont(font3)
        self.label_vol.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_eq_labels.addWidget(self.label_vol)

        self.horizontalLayoutWidget_3 = QWidget(self.page_eq)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(19, 379, 961, 91))
        self.horizontalLayout_eq_7segs = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_eq_7segs.setObjectName(u"horizontalLayout_eq_7segs")
        self.horizontalLayout_eq_7segs.setContentsMargins(0, 0, 0, 0)
        self.lcdNumber_bass = QLCDNumber(self.horizontalLayoutWidget_3)
        self.lcdNumber_bass.setObjectName(u"lcdNumber_bass")
        self.lcdNumber_bass.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_eq_7segs.addWidget(self.lcdNumber_bass)

        self.lcdNumber_mid = QLCDNumber(self.horizontalLayoutWidget_3)
        self.lcdNumber_mid.setObjectName(u"lcdNumber_mid")
        self.lcdNumber_mid.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_eq_7segs.addWidget(self.lcdNumber_mid)

        self.lcdNumber_treble = QLCDNumber(self.horizontalLayoutWidget_3)
        self.lcdNumber_treble.setObjectName(u"lcdNumber_treble")
        self.lcdNumber_treble.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_eq_7segs.addWidget(self.lcdNumber_treble)

        self.lcdNumber_vol = QLCDNumber(self.horizontalLayoutWidget_3)
        self.lcdNumber_vol.setObjectName(u"lcdNumber_vol")
        self.lcdNumber_vol.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_eq_7segs.addWidget(self.lcdNumber_vol)

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
        self.bad_words_blocked = QLabel(self.page_stats)
        self.bad_words_blocked.setObjectName(u"bad_words_blocked")
        self.bad_words_blocked.setGeometry(QRect(230, -30, 541, 161))
        self.bad_words_blocked.setFont(font3)
        self.main_count = QLCDNumber(self.page_stats)
        self.main_count.setObjectName(u"main_count")
        self.main_count.setGeometry(QRect(400, 90, 171, 91))
        self.main_count.setFrameShape(QFrame.Panel)
        self.main_count.setFrameShadow(QFrame.Sunken)
        self.main_count.setProperty("intValue", 12642)
        self.gridLayoutWidget_2 = QWidget(self.page_stats)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(40, 190, 933, 301))
        self.gridLayout = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.s_disposed = QLabel(self.gridLayoutWidget_2)
        self.s_disposed.setObjectName(u"s_disposed")
        font4 = QFont()
        font4.setPointSize(32)
        self.s_disposed.setFont(font4)

        self.gridLayout.addWidget(self.s_disposed, 1, 0, 1, 1)

        self.f_bomb_count = QLCDNumber(self.gridLayoutWidget_2)
        self.f_bomb_count.setObjectName(u"f_bomb_count")
        self.f_bomb_count.setFrameShape(QFrame.Panel)
        self.f_bomb_count.setFrameShadow(QFrame.Sunken)
        self.f_bomb_count.setProperty("intValue", 9469)

        self.gridLayout.addWidget(self.f_bomb_count, 0, 1, 1, 1)

        self.d_blocked = QLabel(self.gridLayoutWidget_2)
        self.d_blocked.setObjectName(u"d_blocked")
        self.d_blocked.setFont(font4)

        self.gridLayout.addWidget(self.d_blocked, 0, 2, 1, 1)

        self.s_disposed_count = QLCDNumber(self.gridLayoutWidget_2)
        self.s_disposed_count.setObjectName(u"s_disposed_count")
        self.s_disposed_count.setFrameShape(QFrame.Panel)
        self.s_disposed_count.setFrameShadow(QFrame.Sunken)
        self.s_disposed_count.setProperty("intValue", 1620)

        self.gridLayout.addWidget(self.s_disposed_count, 1, 1, 1, 1)

        self.f_bombs = QLabel(self.gridLayoutWidget_2)
        self.f_bombs.setObjectName(u"f_bombs")
        self.f_bombs.setFont(font4)

        self.gridLayout.addWidget(self.f_bombs, 0, 0, 1, 1)

        self.d_blocked_count = QLCDNumber(self.gridLayoutWidget_2)
        self.d_blocked_count.setObjectName(u"d_blocked_count")
        self.d_blocked_count.setFrameShape(QFrame.Panel)
        self.d_blocked_count.setFrameShadow(QFrame.Sunken)
        self.d_blocked_count.setProperty("intValue", 573)

        self.gridLayout.addWidget(self.d_blocked_count, 0, 3, 1, 1)

        self.ass_covered = QLabel(self.gridLayoutWidget_2)
        self.ass_covered.setObjectName(u"ass_covered")
        self.ass_covered.setFont(font4)

        self.gridLayout.addWidget(self.ass_covered, 1, 2, 1, 1)

        self.ass_count = QLCDNumber(self.gridLayoutWidget_2)
        self.ass_count.setObjectName(u"ass_count")
        self.ass_count.setFrameShape(QFrame.Panel)
        self.ass_count.setFrameShadow(QFrame.Sunken)
        self.ass_count.setProperty("intValue", 120)

        self.gridLayout.addWidget(self.ass_count, 1, 3, 1, 1)

        self.nasty_spoken = QLabel(self.page_stats)
        self.nasty_spoken.setObjectName(u"nasty_spoken")
        self.nasty_spoken.setGeometry(QRect(40, 510, 661, 71))
        self.nasty_spoken.setFont(font4)
        self.nasty_count = QLCDNumber(self.page_stats)
        self.nasty_count.setObjectName(u"nasty_count")
        self.nasty_count.setGeometry(QRect(690, 500, 181, 81))
        self.nasty_count.setFrameShape(QFrame.Panel)
        self.nasty_count.setFrameShadow(QFrame.Sunken)
        self.nasty_count.setProperty("intValue", 860)
        self.reset_stats = QPushButton(self.page_stats)
        self.reset_stats.setObjectName(u"reset_stats")
        self.reset_stats.setGeometry(QRect(840, 20, 141, 51))
        self.stackedWidget_content.addWidget(self.page_stats)
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_content.raise_()
        self.verticalLayoutWidget.raise_()

        self.retranslateUi(MainWindow)
        self.dial_mid.valueChanged.connect(self.lcdNumber_mid.display)
        self.dial_bass.valueChanged.connect(self.lcdNumber_bass.display)
        self.dial_treb.valueChanged.connect(self.lcdNumber_treble.display)
        self.pushButton_pato.toggled.connect(self.label_disabled.setHidden)
        self.pushButton_pato.toggled.connect(self.label_enabled.setVisible)
        self.dial_vol.valueChanged.connect(self.lcdNumber_vol.display)

        self.pushButton_home.setDefault(False)
        self.stackedWidget_content.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BadMouth", None))
        self.pushButton_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_eq.setText(QCoreApplication.translate("MainWindow", u"Equalizer", None))
        self.pushButton_vis.setText(QCoreApplication.translate("MainWindow", u"Visualizer", None))
        self.pushButton_stats.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.label_UART_in.setText(QCoreApplication.translate("MainWindow", u"UART TEXT", None))
        self.pushButton_pato.setText("")
        self.label_enabled.setText(QCoreApplication.translate("MainWindow", u"Audio Processing: Enabled", None))
        self.label_disabled.setText(QCoreApplication.translate("MainWindow", u"Audio Processing: Disabled", None))
        self.label_bass.setText(QCoreApplication.translate("MainWindow", u"Bass", None))
        self.label_mid.setText(QCoreApplication.translate("MainWindow", u"Mid", None))
        self.label_treb.setText(QCoreApplication.translate("MainWindow", u"Treble", None))
        self.label_vol.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
        self.bad_words_blocked.setText(QCoreApplication.translate("MainWindow", u"Bad Words Blocked:", None))
        self.s_disposed.setText(QCoreApplication.translate("MainWindow", u"Sh*ts Disposed of:", None))
        self.d_blocked.setText(QCoreApplication.translate("MainWindow", u"D*cks Blocked:", None))
        self.f_bombs.setText(QCoreApplication.translate("MainWindow", u"F-Bombs dropped:", None))
        self.ass_covered.setText(QCoreApplication.translate("MainWindow", u"A**es Covered:", None))
        self.nasty_spoken.setText(QCoreApplication.translate("MainWindow", u"Other Nasty Words Spoken:", None))
        self.reset_stats.setText(QCoreApplication.translate("MainWindow", u"RESET STATS", None))
    # retranslateUi


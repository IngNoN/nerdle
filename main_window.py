# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1244, 795)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(60, 10, 1151, 721))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFrameShape(QFrame.Box)
        self.label_8.setLineWidth(2)

        self.gridLayout.addWidget(self.label_8, 2, 5, 1, 1)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFrameShape(QFrame.Box)
        self.label_6.setLineWidth(2)

        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFrameShape(QFrame.Box)
        self.label_5.setLineWidth(2)

        self.gridLayout.addWidget(self.label_5, 2, 7, 1, 1)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFrameShape(QFrame.Box)
        self.label_7.setLineWidth(2)

        self.gridLayout.addWidget(self.label_7, 2, 6, 1, 1)

        self.label_1 = QLabel(self.verticalLayoutWidget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setFrameShape(QFrame.Box)
        self.label_1.setLineWidth(2)

        self.gridLayout.addWidget(self.label_1, 2, 0, 1, 1)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFrameShape(QFrame.Box)
        self.label_2.setLineWidth(2)

        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)

        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFrameShape(QFrame.Box)
        self.label_9.setLineWidth(2)

        self.gridLayout.addWidget(self.label_9, 2, 3, 1, 1)

        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFrameShape(QFrame.Box)
        self.label_10.setLineWidth(2)

        self.gridLayout.addWidget(self.label_10, 2, 4, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(100, -1, 100, -1)
        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        font = QFont()
        font.setPointSize(20)
        self.pushButton_3.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_9 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_9)

        self.pushButton_8 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_7)

        self.pushButton_6 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_6)

        self.pushButton_10 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_10)

        self.pushButton_5 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(200, -1, 200, -1)
        self.pushButton_16 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setFont(font)

        self.horizontalLayout_5.addWidget(self.pushButton_16)

        self.pushButton_15 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setFont(font)

        self.horizontalLayout_5.addWidget(self.pushButton_15)

        self.pushButton_14 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setFont(font)

        self.horizontalLayout_5.addWidget(self.pushButton_14)

        self.pushButton_13 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setFont(font)

        self.horizontalLayout_5.addWidget(self.pushButton_13)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_12 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setFont(font)

        self.horizontalLayout_8.addWidget(self.pushButton_12)

        self.pushButton_11 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font)

        self.horizontalLayout_8.addWidget(self.pushButton_11)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_8)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalLayout.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1244, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_8.setText("")
        self.label_6.setText("")
        self.label_5.setText("")
        self.label_7.setText("")
        self.label_1.setText("")
        self.label_2.setText("")
        self.label_9.setText("")
        self.label_10.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
    # retranslateUi


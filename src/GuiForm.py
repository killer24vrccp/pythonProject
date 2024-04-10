# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(586, 264)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"	background-color: rgb(175, 175, 175);\n"
"}\n"
"\n"
"#frame_5{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 20px;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)


        self.verticalLayout_7.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.frame = QFrame(self.frame_5)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)

        self.source_edit = QLineEdit(self.frame_3)
        self.source_edit.setObjectName(u"source_edit")
        self.source_edit.setFont(font1)

        self.horizontalLayout.addWidget(self.source_edit)

        self.source_button = QToolButton(self.frame_3)
        self.source_button.setObjectName(u"source_button")
        self.source_button.setFont(font1)

        self.horizontalLayout.addWidget(self.source_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.destination_edit = QLineEdit(self.frame_3)
        self.destination_edit.setObjectName(u"destination_edit")
        self.destination_edit.setFont(font1)

        self.horizontalLayout_2.addWidget(self.destination_edit)

        self.destination_button = QToolButton(self.frame_3)
        self.destination_button.setObjectName(u"destination_button")
        self.destination_button.setFont(font1)

        self.horizontalLayout_2.addWidget(self.destination_button)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout_7.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.copy_button = QPushButton(self.frame_2)
        self.copy_button.setObjectName(u"copy_button")
        self.copy_button.setFont(font1)
        self.copy_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.copy_button)

        self.move_button = QPushButton(self.frame_2)
        self.move_button.setObjectName(u"move_button")
        self.move_button.setFont(font1)
        self.move_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.move_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_7.addWidget(self.frame_2, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.frame_5)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"File Manager", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Source", None))
        self.source_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Destination", None))
        self.destination_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.copy_button.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.move_button.setText(QCoreApplication.translate("MainWindow", u"Move", None))
    # retranslateUi


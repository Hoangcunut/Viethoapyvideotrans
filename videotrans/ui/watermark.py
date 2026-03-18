from PySide6 import QtWidgets
from PySide6.QtCore import QMetaObject, QSize, Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout

from videotrans.configure.config import ROOT_DIR, tr, app_cfg, settings, params, TEMP_DIR, logger, defaulelang, HOME_DIR


class Ui_watermark(object):
    def setupUi(self, watermark):
        self.has_done = False
        self.videourls = []
        if not watermark.objectName():
            watermark.setObjectName("watermark")

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(watermark.sizePolicy().hasHeightForWidth())
        watermark.setSizePolicy(size_policy)
        watermark.setMinimumSize(643, 350)

        self.horizontalLayout_3 = QHBoxLayout(watermark)
        self.verticalLayout = QVBoxLayout()

        self.horizontalLayout = QHBoxLayout()
        self.videourl = QLineEdit()
        self.videourl.setObjectName("videourl")
        self.videourl.setMinimumSize(QSize(0, 35))
        self.videourl.setReadOnly(True)
        self.horizontalLayout.addWidget(self.videourl)

        self.videobtn = QPushButton()
        self.videobtn.setObjectName("videobtn")
        self.videobtn.setMinimumSize(QSize(180, 35))
        self.videobtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalLayout.addWidget(self.videobtn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.pngurl = QLineEdit()
        self.pngurl.setObjectName("pngurl")
        self.pngurl.setMinimumSize(QSize(0, 35))
        self.pngurl.setReadOnly(True)
        self.horizontalLayout_2.addWidget(self.pngurl)

        self.pngbtn = QPushButton()
        self.pngbtn.setObjectName("pngbtn")
        self.pngbtn.setMinimumSize(QSize(180, 35))
        self.pngbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalLayout_2.addWidget(self.pngbtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        pos = QtWidgets.QHBoxLayout()
        self.labelpos = QtWidgets.QLabel()
        self.compos = QtWidgets.QComboBox()
        if defaulelang == "zh":
            positions = ["上左", "上右", "下右", "下左", "居中"]
        elif defaulelang == "vi":
            positions = ["Trên trái", "Trên phải", "Dưới phải", "Dưới trái", "Chính giữa"]
        else:
            positions = ["Upper left", "Upper right", "Bottom right", "Bottom left", "Center"]
        self.compos.addItems(positions)
        pos.addWidget(self.labelpos)
        pos.addWidget(self.compos)
        self.verticalLayout.addLayout(pos)

        tmpx = QtWidgets.QHBoxLayout()
        self.labelx = QtWidgets.QLabel()
        self.linex = QtWidgets.QLineEdit()
        tmpx.addWidget(self.labelx)
        tmpx.addWidget(self.linex)

        tmpy = QtWidgets.QHBoxLayout()
        self.labely = QtWidgets.QLabel()
        self.liney = QtWidgets.QLineEdit()
        tmpy.addWidget(self.labely)
        tmpy.addWidget(self.liney)

        tmpw = QtWidgets.QHBoxLayout()
        self.labelw = QtWidgets.QLabel()
        self.linew = QtWidgets.QLineEdit()
        tmpw.addWidget(self.labelw)
        tmpw.addWidget(self.linew)

        self.startbtn = QPushButton()
        self.startbtn.setObjectName("startbtn")
        self.startbtn.setMinimumSize(QSize(0, 35))
        self.startbtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addLayout(tmpx)
        self.verticalLayout.addLayout(tmpy)
        self.verticalLayout.addLayout(tmpw)
        self.verticalLayout.addWidget(self.startbtn)

        self.resultlabel = QLabel()
        self.resultlabel.setObjectName("resultlabel")
        self.verticalLayout.addWidget(self.resultlabel)

        self.resultbtn = QPushButton()
        self.resultbtn.setObjectName("resultbtn")
        self.resultbtn.setStyleSheet("background-color:transparent")
        self.resultbtn.setMinimumSize(QSize(0, 30))
        self.resultbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.verticalLayout.addWidget(self.resultbtn)

        self.horizontalLayout_3.addLayout(self.verticalLayout)
        watermark.setWindowTitle(tr("Adding image watermark to videos"))
        self.retranslateUi()
        QMetaObject.connectSlotsByName(watermark)

    def retranslateUi(self):
        self.videourl.setPlaceholderText(tr("Select  Videos"))
        self.pngurl.setPlaceholderText(tr("Select a watermark image"))
        self.videobtn.setText(tr("Select a Video"))
        self.pngbtn.setText(tr("Select an Image"))
        self.startbtn.setText(tr("Start operating"))
        self.resultlabel.setText("")
        self.resultbtn.setText(tr("Open the save results directory"))
        self.labelx.setText(tr("Distance of watermark from left or right side"))
        self.labely.setText(tr("Distance of watermark from top or bottom"))
        self.labelw.setText(tr("Watermark width x height"))
        self.linew.setText("50x50")
        self.labelpos.setText(tr("Watermark Location"))
        self.linex.setText("10")
        self.liney.setText("10")

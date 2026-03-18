import requests
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QByteArray, QThread, Signal
from PySide6.QtGui import Qt, QPixmap

from videotrans.configure.config import ROOT_DIR, tr, app_cfg, settings, params, TEMP_DIR, logger, defaulelang, HOME_DIR
from videotrans.util import tools


ZH_INFO_TEXT = """本项目基于兴趣创建，无商业和收费计划，你可以一直免费使用，或者 fork 后自己修改（开源协议 GPL-v3）。
所有代码均开源可审查。
至于维护问题，开源项目主要依赖空闲时间和热情投入，因此有时会更新快一些，有时会慢一些。
当然，如果觉得该项目对你有价值，并希望它能稳定持续维护，也欢迎小额捐助。

Email: jianchang512@gmail.com
文档站/下载: pyvideotrans.com
【软件免费下载使用，不收取任何费用，也未在任何平台销售】
"""

VI_INFO_TEXT = """Dự án này được tạo từ đam mê, không có kế hoạch thương mại hay thu phí. Bạn có thể dùng miễn phí lâu dài hoặc fork để tự chỉnh sửa theo giấy phép GPL-v3.
Toàn bộ mã nguồn đều mở và có thể kiểm tra.
Việc duy trì dự án chủ yếu dựa vào thời gian rảnh và tinh thần đóng góp cho mã nguồn mở, nên có lúc cập nhật nhanh, có lúc sẽ chậm hơn.
Nếu bạn thấy dự án hữu ích và muốn nó được duy trì ổn định lâu dài, bạn có thể ủng hộ một khoản nhỏ.

Email: jianchang512@gmail.com
Tài liệu/Tải xuống: pyvideotrans.com
【Phần mềm được phát hành miễn phí, không bán trên bất kỳ nền tảng nào】
"""

EN_INFO_TEXT = """This project is created based on interest, there is no commercial and no charge plan, you can use it for free or fork it and modify it (open source license GPL-v3).
All code is open source and can be reviewed.
As for maintenance, open source mostly runs on spare time and goodwill, so updates may sometimes be fast and sometimes slower.
Of course, if you think this project is useful and want it to continue being maintained, you are welcome to donate a small amount.

Email: jianchang512@gmail.com
Documents: pyvideotrans.com
"""


class Ui_infoform(object):
    def setupUi(self, infoform):
        infoform.setObjectName("infoform")
        infoform.setWindowModality(QtCore.Qt.NonModal)
        infoform.resize(950, 600)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(infoform.sizePolicy().hasHeightForWidth())
        infoform.setSizePolicy(size_policy)
        self.v1 = QtWidgets.QVBoxLayout(infoform)
        self.v1.setAlignment(Qt.AlignTop)

        self.label = QtWidgets.QLabel(infoform)
        self.label.setText(tr("Donate to help the software to keep on maintaining"))
        self.label.setStyleSheet("font-size:20px")
        self.v1.addWidget(self.label)

        self.text1 = QtWidgets.QPlainTextEdit(infoform)
        self.text1.setObjectName("text1")
        self.text1.setReadOnly(True)
        self.text1.setMaximumHeight(180)
        if defaulelang == "zh":
            self.text1.setPlainText(ZH_INFO_TEXT)
        elif defaulelang == "vi":
            self.text1.setPlainText(VI_INFO_TEXT)
        else:
            self.text1.setPlainText(EN_INFO_TEXT)
        self.text1.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.text1.setStyleSheet("border:none;")
        self.v1.addWidget(self.text1)

        self.link = QtWidgets.QPushButton(infoform)
        self.link.setText(tr("Thank all donators, Click to view the list of donators"))
        self.link.setFixedHeight(35)
        self.link.setStyleSheet("background-color:transparent")
        self.link.setCursor(Qt.PointingHandCursor)
        self.link.clicked.connect(lambda: tools.open_url("https://pyvideotrans.com/about.html"))

        label = QtWidgets.QLabel(infoform)
        label.setText(tr("You can scan the QR code or click the above button to donate via the web"))
        h2 = QtWidgets.QHBoxLayout()
        h2.addWidget(self.link)
        h2.addStretch()
        self.v1.addLayout(h2)
        self.v1.addWidget(label)

        self.h1 = QtWidgets.QHBoxLayout()
        if defaulelang == "zh":
            self.wxpay = QtWidgets.QLabel()
            self.alipay = QtWidgets.QLabel()
            self.mp = QtWidgets.QLabel()
            self.wxpay.setFixedHeight(200)
            self.alipay.setFixedHeight(200)
            self.mp.setFixedHeight(200)
            self.h1.addWidget(self.wxpay)
            self.h1.addWidget(self.alipay)
            self.h1.addWidget(self.mp)
            self.v1.addLayout(self.h1)
            wxpaystask = DownloadImg(parent=self, urls={"name": "wxpay", "link": "https://pvtr2.pyvideotrans.com/images/wxpay.jpg"})
            alipaytask = DownloadImg(parent=self, urls={"name": "alipay", "link": "https://pvtr2.pyvideotrans.com/images/alipay.png"})
            mptask = DownloadImg(parent=self, urls={"name": "mp", "link": "https://pvtr2.pyvideotrans.com/images/mp.jpg"})
            wxpaystask.finished.connect(lambda: self.showimg("wxpay"))
            wxpaystask.start()
            alipaytask.finished.connect(lambda: self.showimg("alipay"))
            alipaytask.start()
            mptask.finished.connect(lambda: self.showimg("mp"))
            mptask.start()
        else:
            self.v1.addLayout(self.h1)
            link2 = QtWidgets.QPushButton(infoform)
            link2.setText("Hoặc ủng hộ qua https://ko-fi.com/jianchang512" if defaulelang == "vi" else "Or Donate via https://ko-fi.com/jianchang512")
            link2.setFixedHeight(35)
            link2.setStyleSheet("background-color:transparent;text-align:left")
            link2.setCursor(Qt.PointingHandCursor)
            link2.clicked.connect(lambda: tools.open_url("https://ko-fi.com/jianchang512"))
            self.v1.addWidget(link2)

        lawbtn = QtWidgets.QPushButton()
        lawbtn.setFixedHeight(35)
        lawbtn.setMaximumWidth(300)
        lawbtn.setStyleSheet("background-color:rgba(255,255,255,0);text-align:left")
        lawbtn.setCursor(Qt.PointingHandCursor)
        lawbtn.setText(tr("Software License Agreement"))
        lawbtn.clicked.connect(lambda: tools.open_url("https://pyvideotrans.com/law.html"))
        self.v1.addWidget(lawbtn)
        self.v1.addStretch()
        infoform.setWindowTitle(tr("Donate to help the software to keep on maintaining"))
        QtCore.QMetaObject.connectSlotsByName(infoform)

    def showimg(self, name):
        pixmap = QPixmap()
        pixmap.loadFromData(app_cfg.INFO_WIN["data"][name])
        pixmap = pixmap.scaledToHeight(200, Qt.SmoothTransformation)
        if name == "wxpay":
            self.wxpay.setPixmap(pixmap)
        elif name == "alipay":
            self.alipay.setPixmap(pixmap)
        elif name == "mp":
            self.mp.setPixmap(pixmap)

    def closeEvent(self, event):
        self.hide()


class DownloadImg(QThread):
    finished = Signal(str)

    def __init__(self, parent=None, urls=None):
        super().__init__(parent=parent)
        self.urls = urls

    def run(self):
        try:
            response = requests.get(self.urls["link"])
            response.raise_for_status()
            app_cfg.INFO_WIN["data"][self.urls["name"]] = QByteArray(response.content)
            self.finished.emit(self.urls["name"])
        except Exception:
            pass

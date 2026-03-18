from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QMetaObject, QSize, Qt
from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton, QSizePolicy

from videotrans.configure.config import ROOT_DIR, tr, app_cfg, settings, params, TEMP_DIR, logger, defaulelang, HOME_DIR
from videotrans.util import tools


class Ui_transapiform(object):
    def setupUi(self, transapiform):
        self.has_done = False
        if not transapiform.objectName():
            transapiform.setObjectName("transapiform")
        transapiform.setWindowModality(Qt.NonModal)
        transapiform.resize(600, 400)
        size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(transapiform.sizePolicy().hasHeightForWidth())
        transapiform.setSizePolicy(size_policy)
        transapiform.setMaximumSize(QSize(600, 400))
        v1 = QtWidgets.QVBoxLayout(transapiform)

        h1 = QtWidgets.QHBoxLayout()
        self.label = QLabel()
        self.label.setObjectName("label")
        self.label.setMinimumSize(QSize(150, 35))
        self.api_url = QLineEdit()
        self.api_url.setObjectName("api_url")
        self.api_url.setMinimumSize(QSize(0, 35))
        h1.addWidget(self.label)
        h1.addWidget(self.api_url)
        v1.addLayout(h1)

        h2 = QtWidgets.QHBoxLayout()
        self.label_3 = QLabel()
        self.label_3.setObjectName("miyue")
        self.label_3.setMinimumSize(QSize(150, 35))
        self.miyue = QLineEdit()
        self.miyue.setObjectName("miyue")
        h2.addWidget(self.label_3)
        h2.addWidget(self.miyue)
        v1.addLayout(h2)

        self.tips = QtWidgets.QPlainTextEdit()
        self.tips.setObjectName("tips")
        self.tips.setReadOnly(True)
        v1.addWidget(self.tips)

        h3 = QtWidgets.QHBoxLayout()
        self.save = QPushButton()
        self.save.setObjectName("save")
        self.save.setMinimumSize(QSize(0, 35))
        self.test = QPushButton(transapiform)
        self.test.setObjectName("test")
        self.test.setMinimumSize(QSize(0, 35))

        help_btn = QtWidgets.QPushButton()
        help_btn.setMinimumSize(QtCore.QSize(0, 35))
        help_btn.setStyleSheet("background-color: rgba(255, 255, 255,0)")
        help_btn.setObjectName("help_btn")
        help_btn.setCursor(Qt.PointingHandCursor)
        help_btn.setText(tr("Fill out the tutorial"))
        help_btn.clicked.connect(lambda: tools.open_url(url="https://pyvideotrans.com/transapi"))
        h3.addWidget(self.save)
        h3.addWidget(self.test)
        h3.addWidget(help_btn)

        v1.addLayout(h3)

        self.retranslateUi(transapiform)
        QMetaObject.connectSlotsByName(transapiform)

    def retranslateUi(self, transapiform):
        if defaulelang == "zh":
            tips = """
将以 GET 请求向填写的 API 地址发送 application/www-urlencode 数据：
text: 需要翻译的文本/字符串
source_language: 原始文字语言代码 zh,en,ja,ko,ru,de,fr,tr,th,vi,ar,hi,hu,es,pt,it
target_language: 目标文字语言代码 zh,en,ja,ko,ru,de,fr,tr,th,vi,ar,hi,hu,es,pt,it
期望从接口返回 JSON 格式数据：
{
    code: 0=成功，>0 代表失败,
    msg: ok=成功，其它为失败原因,
    text: 翻译后的文本
}
基于 cloudflare 和 m2m100 实现的免费翻译 API 见: github.com/jianchang512/translate-api
"""
        elif defaulelang == "vi":
            tips = """
Dữ liệu `application/www-urlencode` sẽ được gửi bằng yêu cầu GET tới địa chỉ API bạn điền:
text: văn bản/chuỗi cần dịch
source_language: mã ngôn ngữ nguồn zh,en,ja,ko,ru,de,fr,tr,th,vi,ar,hi,hu,es,pt,it
target_language: mã ngôn ngữ đích zh,en,ja,ko,ru,de,fr,tr,th,vi,ar,hi,hu,es,pt,it
Ứng dụng mong đợi API trả về dữ liệu JSON:
{
    code: 0 là thành công, số >0 là thất bại,
    msg: ok là thành công, giá trị khác là lý do lỗi,
    text: văn bản đã dịch
}
Ví dụ API miễn phí dựa trên Cloudflare và m2m100: github.com/jianchang512/translate-api
"""
        else:
            tips = """
The application/www-urlencode data will be sent as a GET request to the filled API address:
text:text/string to be translated
source_language:original text language code zh,en,ja,ko,ru,de,fr,tr,th,vi,ar,hi,hu,es,pt,it/string
target_language:target_language code zh,en,ja,ko,ru,de,fr,tr,th,vi,ar,hi,hu,es,pt,it/string
Expect data to be returned from the interface in json format:
{
    code:0=on success  numbers >0 represent failures, msg:ok=success  others are failure reasons,text:Translated text
}
Usage: github.com/jianchang512/translate-api
"""
        transapiform.setWindowTitle(tr("Customizing the Translate API"))
        self.label_3.setText(tr("Secret"))
        self.miyue.setPlaceholderText("Điền khóa bí mật" if defaulelang == "vi" else "å¡«å†™å¯†é’¥")
        self.tips.setPlainText(tips)
        self.save.setText(tr("Save"))
        self.api_url.setPlaceholderText(tr("Fill in the full address starting with http"))
        self.label.setText(tr("Translate API"))
        self.test.setText(tr("Test"))

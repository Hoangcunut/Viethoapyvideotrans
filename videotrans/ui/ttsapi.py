from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QMetaObject, QSize, Qt
from PySide6.QtWidgets import QLabel, QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy

from videotrans.configure.config import ROOT_DIR, tr, app_cfg, settings, params, TEMP_DIR, logger, defaulelang, HOME_DIR
from videotrans.util import tools


class Ui_ttsapiform(object):
    def setupUi(self, ttsapiform):
        self.has_done = False
        if not ttsapiform.objectName():
            ttsapiform.setObjectName("ttsapiform")
        ttsapiform.setWindowModality(Qt.NonModal)
        ttsapiform.resize(600, 600)
        size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(ttsapiform.sizePolicy().hasHeightForWidth())
        ttsapiform.setSizePolicy(size_policy)
        ttsapiform.setMaximumSize(QSize(600, 600))

        v1 = QtWidgets.QVBoxLayout(ttsapiform)
        self.label = QLabel()
        self.label.setObjectName("label")
        self.label.setMinimumSize(QSize(0, 35))
        self.api_url = QLineEdit(ttsapiform)
        self.api_url.setObjectName("api_url")
        self.api_url.setMinimumSize(QSize(0, 35))

        h1 = QtWidgets.QHBoxLayout()
        h1.addWidget(self.label)
        h1.addWidget(self.api_url)
        v1.addLayout(h1)

        h2 = QtWidgets.QHBoxLayout()
        self.label_2 = QLabel(ttsapiform)
        self.label_2.setObjectName("label_2")
        self.label_2.setMinimumSize(QSize(0, 35))
        self.label_2.setSizeIncrement(QSize(0, 35))
        self.voice_role = QPlainTextEdit(ttsapiform)
        self.voice_role.setObjectName("voice_role")
        self.voice_role.setMinimumSize(QSize(0, 35))
        h2.addWidget(self.label_2)
        h2.addWidget(self.voice_role)
        v1.addLayout(h2)

        h3 = QtWidgets.QHBoxLayout()
        h4 = QtWidgets.QHBoxLayout()
        h5 = QtWidgets.QHBoxLayout()
        self.label_3 = QLabel(ttsapiform)
        self.label_3.setObjectName("label_3")
        self.extra = QLineEdit(ttsapiform)
        self.extra.setObjectName("extra")
        self.extra.setMinimumSize(QSize(0, 35))

        self.label_4 = QLabel(ttsapiform)
        self.label_4.setObjectName("label_4")
        self.label_4.setText(tr("Language"))
        self.language_boost = QtWidgets.QComboBox(ttsapiform)
        self.language_boost.setObjectName("language_boost")
        self.language_boost.setMinimumSize(QSize(0, 35))
        self.language_boost.addItems([
            "auto", "Chinese", "Chinese,Yue", "English", "Arabic", "Russian", "Spanish", "French", "Portuguese",
            "German", "Turkish", "Dutch", "Ukrainian", "Vietnamese", "Indonesian", "Japanese", "Italian", "Korean"
        ])

        label_5 = QLabel(ttsapiform)
        label_5.setText(tr("Emotion"))
        self.emotion = QtWidgets.QComboBox(ttsapiform)
        self.language_boost.setObjectName("emotion")
        self.emotion.setMinimumSize(QSize(0, 35))
        self.emotion.addItems(["happy", "sad", "angry", "fearful", "disgusted", "surprised", "neutral"])

        h3.addWidget(self.label_3)
        h3.addWidget(self.extra)
        h4.addWidget(self.label_4)
        h4.addWidget(self.language_boost)
        h5.addWidget(label_5)
        h5.addWidget(self.emotion)
        v1.addLayout(h3)
        v1.addLayout(h4)
        v1.addLayout(h5)

        self.tips = QPlainTextEdit(ttsapiform)
        self.tips.setObjectName("tips")
        self.tips.setReadOnly(True)
        v1.addWidget(self.tips)

        h6 = QtWidgets.QHBoxLayout()
        self.save = QPushButton(ttsapiform)
        self.save.setObjectName("save")
        self.save.setMinimumSize(QSize(0, 35))
        self.test = QPushButton(ttsapiform)
        self.test.setObjectName("test")
        self.test.setMinimumSize(QSize(0, 35))

        help_btn = QtWidgets.QPushButton()
        help_btn.setMinimumSize(QtCore.QSize(0, 35))
        help_btn.setStyleSheet("background-color: rgba(255, 255, 255,0)")
        help_btn.setObjectName("help_btn")
        help_btn.setCursor(Qt.PointingHandCursor)
        help_btn.setText(tr("Fill out the tutorial"))
        help_btn.clicked.connect(lambda: tools.open_url(url="https://pyvideotrans.com/ttsapi"))

        h6.addWidget(self.save)
        h6.addWidget(self.test)
        h6.addWidget(help_btn)
        v1.addLayout(h6)

        self.retranslateUi(ttsapiform)
        QMetaObject.connectSlotsByName(ttsapiform)

    def retranslateUi(self, ttsapiform):
        if defaulelang == "zh":
            tips = """
将以 POST 请求向填写的 API 地址发送 application/www-urlencode 数据：

text: 需要合成的文本/字符串
language: 文字所属语言代码(zh-cn,zh-tw,en,ja,ko,ru,de,fr,tr,th,vi,ar,hi,hu,es,pt,it)
voice: 配音角色名称/字符串
rate: 加减速值，0 或 '+数字%' '-数字%'，表示在正常速度基础上的加减速百分比
ostype: win32 或 mac 或 linux 操作系统类型
extra: 额外参数/字符串

期望从接口返回 JSON 格式数据：
{
    code: 0=合成成功，>0 代表失败
    msg: ok=成功，其它为失败原因
    data: 成功时返回 mp3 文件完整 URL，供软件下载；失败时为空
}
"""
        elif defaulelang == "vi":
            tips = """
Dữ liệu `application/www-urlencode` sẽ được gửi bằng yêu cầu POST tới địa chỉ API bạn điền:

text: văn bản/chuỗi cần tổng hợp
language: mã ngôn ngữ của văn bản (zh-cn,zh-tw,en,ja,ko,ru,de,fr,tr,th,vi,ar,hi,hu,es,pt,it)
voice: tên giọng đọc/chuỗi
rate: giá trị tăng giảm tốc, 0 hoặc '+số%' '-số%', biểu thị phần trăm thay đổi tốc độ
ostype: loại hệ điều hành win32, mac hoặc linux
extra: tham số bổ sung/chuỗi

Ứng dụng mong đợi API trả về JSON:
{
    code: 0 là tổng hợp thành công, số >0 là thất bại
    msg: ok là thành công, giá trị khác là lý do lỗi
    data: khi thành công trả về URL đầy đủ của tệp mp3 để phần mềm tải về; nếu thất bại thì để trống
}
"""
        else:
            tips = """
The application/www-urlencode data will be sent in a POST request to the filled API address:

text:text/string
language:language code(zh-cn,zh-tw,en,ja,ko,ru,de,fr,tr,th,vi,ar,hi,hu,es,pt,it) / string
voice:voice character name/string
rate:acceleration/deceleration value, 0 or '+numeric%' '-numeric%', represents the percentage of acceleration/deceleration on top of the normal speed /string
ostype:win32 or mac or linux OS type/string
extra:extra parameters/string

Expect data to be returned from the interface in json format:
{
    code:0=when synthesis is successful, a number >0 means failure
    msg:ok=when the synthesis was successful, other is the reason for failure
    data:On successful synthesis, return the full url of the mp3 file for downloading within the software. When it fails, the url will be empty.
}
"""
        ttsapiform.setWindowTitle(tr("Customizing the TTS-API"))
        self.label_3.setText(tr("SK"))
        self.tips.setPlainText(tips)
        self.tips.setPlaceholderText("")
        self.save.setText(tr("Save"))
        self.api_url.setPlaceholderText(tr("Fill in the full address starting with http"))
        self.label.setText(tr("Customizing TTS-API"))
        self.voice_role.setPlaceholderText(tr("Fill in the available voice acting role names, separate multiple with English commas"))
        self.label_2.setText(tr("Fill in the names of the available voiceover characters, separating multiple ones with English commas"))
        self.extra.setPlaceholderText(tr("Fill in the extra parameters passed to the api via the extra key, null to pass pyvideotrans"))
        self.test.setText(tr("Test"))

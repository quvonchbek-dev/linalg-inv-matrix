from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from src import functions
form, base = uic.loadUiType("src/main.ui")


class MyApp(QtWidgets.QMainWindow, form):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)
        self.setupUi(self)
        self.encode.clicked.connect(self.encode_text)
        self.decode.clicked.connect(self.decode_text)
    
    def encode_text(self):
        try:
            text = functions.filter_text(self.input_1.toPlainText())
            key_t = functions.filter_text(self.key_matrix.text())
            key_a = list(map(int, key_t.split()))
            key_v = [key_a[:2], key_a[2:]]
            self.encoded.setText(str(functions.encode(text, key_v)))
        except Exception as ex:
            print(ex)
            QMessageBox.warning(self, "Xatolik!", "Maydonlar hammasi to'liq va to'g'ri to'ldirilishi kerak.")
    
    def decode_text(self):
        try:
            text = functions.filter_text(self.input_2.toPlainText())
            A = list(map(int, text.split()))
            key_t = functions.filter_text(self.key_matrix.text())
            key_a = list(map(int, key_t.split()))
            key_v = [key_a[:2], key_a[2:]]
            self.decoded.setText(str(functions.decode(A, key_v)))
        except Exception as ex:
            QMessageBox.warning(self, "Xatolik", "Siz maydonlarni to'g'ri to'ldirmadingiz yoki kodlash matritsasini xato kiritdingiz.")

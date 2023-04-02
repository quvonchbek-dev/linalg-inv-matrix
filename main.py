import sys
from PyQt5 import QtWidgets, uic
from src.App import MyApp

app = QtWidgets.QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec_())
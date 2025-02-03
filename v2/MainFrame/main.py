from PyQt5.QtWidgets import QWidget
from PySide6.QtWidgets import (QApplication, QMainWindow)
from ui_tela import Ui_MainWindow
import sys

class tela(QWidget, Ui_MainWindow):
    def __init__(self) -> None:
        super(tela, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Iniciar o Sistema")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = tela()
    window.show()
    app.exec()
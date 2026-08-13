from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CDSS")
        self.setFixedSize(320, 240)

        label = QLabel("Hello world")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

app = QApplication()

window = MainWindow()

window.show()

app.exec()
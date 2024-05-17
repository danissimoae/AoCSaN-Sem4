from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication

from controller import MainWindow

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.setWindowIcon(QIcon('webIcon.png'))
    mainwindow.show()
    sys.exit(app.exec())

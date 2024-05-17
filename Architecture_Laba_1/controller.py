from PyQt6.QtGui import QMovie, QPixmap
from PyQt6.QtWidgets import QMainWindow, QApplication
from model import NetworkParams
from Architecture_Laba_1_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = NetworkParams()
        self.model.changed.connect(self.update_data)

        self.ui.lineEditBeginIp.editingFinished.connect(
            lambda: self.model.set_start_ip(self.ui.lineEditBeginIp.text())
        )
        self.ui.lineEditEndIp.editingFinished.connect(
            lambda: self.model.set_end_ip(self.ui.lineEditEndIp.text())
        )
        self.ui.pushButtonGenerateAnswer.clicked.connect(
            self.calculate_params
        )
        self.ui.movie = QMovie("animation.gif")
        self.ui.labelGif.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.update_data()

    def calculate_params(self):
        self.model.calculate_network_params()

    def update_data(self):
        self.ui.lineEditBeginIp.setText(self.model.get_start_ip())
        self.ui.lineEditEndIp.setText(self.model.get_end_ip())
        self.ui.textEditAnswer.setText(self.model.get_result_text())


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

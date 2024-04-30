from PyQt6 import QtWidgets
from PyQt6.QtGui import QMovie, QFont, QIcon
import Architecture_Laba_1_ui
import sys
import algorithm


class ArchitectureLaba1(QtWidgets.QMainWindow, Architecture_Laba_1_ui.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле
        # Вызываем метод из родительского класса
        super().__init__()
        self.setupUi(self)


        ## Настройки окна
        self.setWindowTitle("Калькулятор параметров сети")
        self.setWindowIcon(QIcon("webIcon.png"))

        ## Отрисовка красивой анимации
        self.movie = QMovie("animation.gif")
        self.labelGif.setMovie(self.movie)
        self.movie.start()


        ## Сигналы
        self.pushButtonGenerateAnswer.clicked.connect(self.generateAnswer)
        self.textEditAnswer.setReadOnly(True)


    ## Обработчики - слоты
    def generateAnswer(self):
        ip = self.lineEditIp.text()
        if algorithm.validateIp(ip) == True:
            params = algorithm.calculateNetworkParams(ip) 
            answer = f"""
<style>
    table {{
        font-family: monospace;
        border-collapse: collapse;
    }}
    th, td {{
        border: 1px solid white;
        padding: 8px;
        transition: background-color 0.3s;
    }}
</style>
<table>
    <tr>
        <th>Адрес сети</th>
        <td>{params[0].ljust(14)}</td>
    </tr>
    <tr>
        <th>Broadcast адрес</th>
        <td>{params[1].ljust(14)}</td>
    </tr>
    <tr>
        <th>Маска сети</th>
        <td>{params[2].ljust(14)}</td>
    </tr>
    <tr>
        <th>Мак адрес</th>
        <td>{params[3].ljust(14)}</td>
    </tr>
</table>
"""
            self.textEditAnswer.setFont(QFont("Cascadia", 10))
            self.textEditAnswer.setText(answer)
            self.label.setText("<- Параметры")
        else:
            self.label.setText("Неверный формат !")
            self.textEditAnswer.setText(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error: Invalid IP Format</title>
    <style>
        body {{
            font-family: monospace;
            color: white;
            background-color: black;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }}
        .error-container {{
            background-color: black;
            border: 1px solid white;
            border-radius: 5px;
            padding: 20px;
            text-align: center;
        }}
        .error-message {{
            margin-bottom: 10px;
            font-size: 18px;
            font-weight: bold;
        }}
        .instruction {{
            font-size: 16px;
        }}
    </style>
</head>
<body>
    <div class="error-container">
        <p class="error-message">Ошибка ввода</p>
        <p class="instruction">Введите адрес в формате: 0.0.0.0/0</p>
    </div>
</body>
</html>
""")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ArchitectureLaba1()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
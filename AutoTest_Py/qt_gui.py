import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(500, 300, 800, 500)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('E:/Python/AutoTest_Py/Icon/title.png'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import os
import sys
import time


class ThreadProgress(QThread):
    mysignal = pyqtSignal(int)
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
    def run(self):
        i = 0
        while i<101:
            time.sleep(0.1)
            self.mysignal.emit(i)
            i += 1

FROM_SPLASH,_ = loadUiType(os.path.join(os.path.dirname(__file__),"splash.ui"))
FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"main.ui"))


class Main(QMainWindow, FROM_MAIN):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_click)

    def on_click(self):
        QMessageBox.information(self, "Omar Othman", "This code writed by Omar Othman")

        
class Splash(QMainWindow, FROM_SPLASH):
    def __init__(self, parent = None):
        super(Splash, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        pixmap = QPixmap("splash.png")
        self.splah_image.setPixmap(pixmap.scaled(350, 300))
        progress = ThreadProgress(self)
        progress.mysignal.connect(self.progress)
        progress.start()
        
    @pyqtSlot(int)
    def progress(self, i):
        self.progressBar.setValue(i)
        if i == 100:
            self.hide()
            main = Main(self)
            main.show()


def main():
    app=QApplication(sys.argv)
    window = Splash()
    window.show()
    app.exec_()

if __name__ == '__main__':
    try:
        main()
    except Exception as why:
        print(why)


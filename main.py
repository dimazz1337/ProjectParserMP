import sys
import time
from PyQt5 import QtWidgets, QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from parser import Ui_MainWindow
from src.site_one import main_one
from src.site_two import main_two
from src.site_three import main_three
from src.wathcer.watcher import Watcher
from threading import Thread
from config import html_file_path
from PyQt5.QtCore import QThread



class ParserThread(QThread):
    def __init__(self, site_function):
        super().__init__()
        self.site_function = site_function

    def run(self):
        self.site_function()


class ParserWindow(QMainWindow):
    def __init__(self):
        super(ParserWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.threads = []  #список потоков

        #обработчик кнопок
        self.ui.btn_start.clicked.connect(lambda: self.start_parser())
        self.ui.btn_clear.clicked.connect(lambda: self.clear_parser(''))
        self.ui.btn_stop.clicked.connect(lambda: self.stop_parser())


    # кнопка старт
    def start_parser(self) -> None:
        if self.ui.check_metallinfo.isChecked():
            thread = ParserThread(main_one)
            self.threads.append(thread)
            thread.start()

        if self.ui.check_metalexpo.isChecked():
            thread2 = ParserThread(main_two)
            self.threads.append(thread2)
            thread2.start()

        if self.ui.check_metallbulletin.isChecked():
            thread3 = ParserThread(main_three)
            self.threads.append(thread3)
            thread3.start()

        if not self.threads:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Информация")
            dlg.setText("Выберите хотя бы один сайт.")
            button = dlg.exec()
            if button == QMessageBox.Ok:
                print("Выберите хотя бы один сайт")

    def clear_parser(self, area_clear: str) -> None:
        self.ui.log_label.setText(area_clear)

    def stop_parser(self) -> None:
        for thread in self.threads:
            thread.terminate()
            print(thread.isFinished())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ParserWindow()
    window.show()
    sys.exit(app.exec())

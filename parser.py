from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)
#import src_img_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(432, 412)
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    color: #ABABAB;\n"
"    background-color: #101523;\n"
"	font-family: Onest;\n"
"	font-size: 10pt;\n"
"	font-weight: 600;\n"
"}\n"
"\n"
"QPushButton{\n"
"	 position: relative;\n"
"	border-radius: 3px;\n"
" 	 vertical-align: top;\n"
" 	 width: 100%;\n"
"  	 height: 22px;\n"
"  	 padding: 0;\n"
" 	 font-size: 11px;\n"
" 	 color: white;\n"
"	 font-family: Onest;\n"
" 	 text-align: center;\n"
" 	 text-shadow: 0 1px 2px rgba(0, 0, 0, 0.25);\n"
" 	 background: #5523EF;\n"
" 	 border: 0;\n"
" 	 cursor: pointer;\n"
"  	-webkit-box-shadow: inset 0 -2px #e8930c;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background:#7045EF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background:#451CBF;\n"
"	height: 20px;\n"
"	top: 1px;\n"
" 	outline: none;\n"
"     -webkit-box-shadow: none;\n"
"     box-shadow: none;\n"
"}\n"
"\n"
"QcheckBox {\n"
"    background-color: #5523EF;\n"
"}")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid rgba(178, 178, 178, 255);\n"
"    margin-top: 6px;\n"
"    padding-top: 8px;\n"
"	border-radius: 5px;\n"
"}\n"
" \n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    left: 10px;\n"
"    margin: 0 5px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.check_metallinfo = QCheckBox(self.groupBox)
        self.check_metallinfo.setObjectName(u"check_metallinfo")

        self.verticalLayout_3.addWidget(self.check_metallinfo)

        self.check_metalexpo = QCheckBox(self.groupBox)
        self.check_metalexpo.setObjectName(u"check_metalexpo")

        self.verticalLayout_3.addWidget(self.check_metalexpo)

        self.check_metallbulletin = QCheckBox(self.groupBox)
        self.check_metallbulletin.setObjectName(u"check_metallbulletin")

        self.verticalLayout_3.addWidget(self.check_metallbulletin)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout.addWidget(self.groupBox)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer_3 = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_start = QPushButton(self.centralwidget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.btn_start, 0, 0, 1, 1)

        self.btn_stop = QPushButton(self.centralwidget)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_stop, 1, 0, 1, 1)

        self.btn_saveas = QPushButton(self.centralwidget)
        self.btn_saveas.setObjectName(u"btn_saveas")
        self.btn_saveas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_saveas.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.btn_saveas, 0, 1, 1, 1)

        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_clear.setStyleSheet(u"#pushButton_4 {\n"
"  background-color: #e74c3c;\n"
"}\n"
"\n"
"#pushButton_4:hover {\n"
"	background-color: #E76253;\n"
"\n"
"}\n"
"\n"
"#pushButton_4:pressed {\n"
"	background-color: #C14032\n"
"}")

        self.gridLayout_2.addWidget(self.btn_clear, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(0, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.log_label = QTextEdit(self.centralwidget)
        self.log_label.setObjectName(u"log_label")
        self.log_label.setStyleSheet(u"QTextEdit {\n"
"	background-color: #232323;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #B2B2B2;\n"
"}\n"
"")
        self.log_label.setReadOnly(True)

        self.gridLayout.addWidget(self.log_label, 2, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 5, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_2)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    background-color: #F9F9F9;\n"
"    color: black;\n"
"    border-style: solid;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"    font-family: Onest;\n"
"	font-size: 8pt;\n"
"	height: 20px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    border-radius: 10px;\n"
"	background-color: #54FF83\n"
"}")
        self.progressBar.setValue(0)

        self.verticalLayout_2.addWidget(self.progressBar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 432, 19))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MP Parser", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0441\u0430\u0439\u0442\u0430 \u0434\u043b\u044f \u043f\u0430\u0440\u0441\u0438\u043d\u0433\u0430", None))
        self.check_metallinfo.setText(QCoreApplication.translate("MainWindow", u"metalinfo.ru", None))
        self.check_metalexpo.setText(QCoreApplication.translate("MainWindow", u"metal-expo.ru", None))
        self.check_metallbulletin.setText(QCoreApplication.translate("MainWindow", u"metalbulletin.ru", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
        self.btn_stop.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.btn_saveas.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 \u0444\u0430\u0439\u043b", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043b\u043e\u0433\u0438", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438", None))
        self.log_label.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Onest'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi


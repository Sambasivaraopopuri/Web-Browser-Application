from turtle import back, forward
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        nav_bar=QToolBar()
        self.addToolBar(nav_bar)
        back_button=QAction("Back",self)
        back_button.triggered.connect(self.browser.back)
        nav_bar.addAction(back_button)

        forward_btn=QAction("Forward",self)
        forward_btn.triggered.connect(self.browser.forward)
        nav_bar.addAction(forward_btn)
app=QApplication(sys.argv)
QApplication.setApplicationName("SSR")
window=MainWindow()
app.exec_()
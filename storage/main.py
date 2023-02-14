from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, QWidget
from PySide6.QtGui import QColor
from PySide6.QtCore import QUrl
from PySide6 import QtNetwork
from PySide6.QtWebEngineWidgets import QWebEngineView
from sideBar.Style import Style
import sys
from sideBar.SideBarButtons import SideBarButton
from sideBar.SideBar import SideBar

class MainWindow(QMainWindow):
    
    def __init__(self):
        
        super(MainWindow, self).__init__()
        
        self.setFixedSize(1000, 1000)
        
        self.setStyleSheet("""
                           * {
                            border: 1px solid pink;   
                           }
                           """)
        self.bufferWidget = QWidget()
        
        self.mainlayout1 = QVBoxLayout()
        # self.mainlayout2 = QHBoxLayout()
        # self.mainlayout3 = QHBoxLayout()
        
        # self.mainlayout2.addWidget(SideBarButton())
        startColor = QColor(194, 187, 240)
        endColor = QColor(98, 191, 237)
        # button = SideBarButton(startColor=startColor,
        #                                          endColor=endColor,
        #                                          style=Style,
        #                                          text="Test")
        # self.mainlayout1.addWidget(button)
        
        # print(button.text())
        # view = QWebEngineView(self)
        # view.load(QUrl("https://www.tcgplayer.com/product/253906/yugioh-maximum-gold-el-dorado-blue-eyes-white-dragon?xid=pie9b7d0fd-2bec-41fb-a5c0-a025660fb92f&page=1&Language=English"))
        # print(view.())
        # view.setFixedSize(1000,1000)
        # view.show()
        # self.bufferWidget.setLayout(self.mainlayout1)
        
        # self.mainlayout1.addLayout(self.mainlayout2)
        # self.mainlayout1.addLayout(self.mainlayout3)
        # self.setCentralWidget(self.bufferWidget)
        # self.setLayout(self.mainlayout1)
        self.sideBar = SideBar()
        self.setCentralWidget(self.sideBar)
        
        

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    w = MainWindow()
    w.show()
    
    app.exec()
        
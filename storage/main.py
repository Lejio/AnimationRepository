from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, QWidget
from PySide6.QtGui import QColor
from sideBar.Style import Style
import sys
from sideBar.SideBarButtons import SideBarButton

class MainWindow(QMainWindow):
    
    def __init__(self):
        
        super(MainWindow, self).__init__()
        
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
        button = SideBarButton(startColor=startColor,
                                                 endColor=endColor,
                                                 style=Style,
                                                 text="Test")
        self.mainlayout1.addWidget(button)
        
        print(button.text())
        
        
        self.bufferWidget.setLayout(self.mainlayout1)
        
        # self.mainlayout1.addLayout(self.mainlayout2)
        # self.mainlayout1.addLayout(self.mainlayout3)
        self.setCentralWidget(self.bufferWidget)
        # self.setLayout(self.mainlayout1)
        
        

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    w = MainWindow()
    w.show()
    
    app.exec()
        
from PySide6.QtWidgets import QPushButton, QWidget, QMainWindow, QHBoxLayout
from PySide6.QtCore import QPropertyAnimation
from PySide6.QtGui import QColor
from animateWidget import animateWidget
from testCheckBox import testCheckBox
from testButton import testButton
from testWidget import testWidget

class animate(QMainWindow):
    
    def __init__(self, name) -> None:
        super(animate, self).__init__()
        
        '''
        To animate your custom widget, I must learn how to use QPainter and it's subclasses + any other special properties it comes with. 
        
        Things under the QtGui package.
        
        Everytime the setter and getters are called, the interpolated values are inserted into the chosen property. You would then need to call the update() function.
        
        The update() function calls the paintEvent, which changes the look of the widget. If we want to make our own custom animation, we would want to override the paintEvent. That results in the entire widget "disappearing". We would need to draw our own widget using the QtGui package. 
        '''
        
        
        # self.setStyleSheet("""
        #                    background-color: gray;
        #                    """)
        self.setGeometry(100, 100, 500, 500)
        self.setContentsMargins(10,10,10,10)
        
        self.boxlayout = QHBoxLayout()
        
        # a = animateWidget(name=name)
        a = testCheckBox()
        b = testButton()
        c = QPushButton("Hello")
        d = testWidget(height=500)
        # b = QPushButton("Bruh")
        # b.setStyleSheet("""
        #                 background-color: green;
        #                 """)
        # anim = QPropertyAnimation(b, b"geometry")
        # anim.setStartValue(100)
        # anim.setEndValue(200)
        # anim.setDuration(2500)
        # anim.start()
        
        self.boxlayout.addWidget(a)
        self.boxlayout.addWidget(b)
        self.boxlayout.addWidget(c)
        # self.boxlayout.addWidget(b)
        
        self.setLayout(self.boxlayout)
        
        # color_names = QColor.colorNames()
        
        # QColor("gold")
        # QColor("cyan")
        
        
        
        # for item in color_names:
            
        #     print(str(item))
        
        # print(QColor.colorNames)
        # self.anim = QPropertyAnimation(a, b'color')
        # self.anim.setStartValue(0)
        # self.anim.setEndValue(255)
        # self.anim.setDuration(2500)
        # self.anim.start()
        
        
        self.setCentralWidget(d)
        
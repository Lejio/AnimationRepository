from PySide6.QtWidgets import QWidget, QPushButton
from PySide6.QtCore import Property, QPropertyAnimation, QRect
from PySide6.QtGui import QPainter, QPaintEvent


class animateWidget(QPushButton):
    
    def __init__(self, name):
        
        super(animateWidget, self).__init__()
        
        # self.setText(name)
        self._color = 0
        self._opacity = 0
        
        print("Setting Style.")
        self.setStyleSheet(f"""
                           background-color: rgba(255, 255, 100, 255);
                           """)
        # self.setStyleSheet("""
        #                    background-color: green;
        #                    """)
        
        # self.anim = QPropertyAnimation(self, b'color', self)
        # self.anim.setDuration(2500)
        # self.anim.setEndValue(255)
        # self.anim.start()
    
    
    def paintEvent(self, e: QPaintEvent):
        pass
        # print(self._color)
        # self.setStyleSheet(f"""
        #                    background-color: rgba({self._color}, {self._color}, {self._color}, 255)
        #                    """)
        
        # print(f"background-color: rgba({self._color}, {self._color}, {self._color}, 255)")
        # print(e)
        
        
        
    
    # @Property(int)
    # def color(self):
        
    #     return self.color
    
    # @color.setter
    # def color(self, col):
        
    #     self.color = col
    #     self.update()
        
    @Property(int)
    def color(self):
        return self._color

    @color.setter
    def color(self, pos):
        """change the property
        we need to trigger QWidget.update() method, either by:
            1- calling it here [ what we're doing ].
            2- connecting the QPropertyAnimation.valueChanged() signal to it.
        """
        self._color = pos
        self.update()
        print(self._color)
        
        
        
    
        
        
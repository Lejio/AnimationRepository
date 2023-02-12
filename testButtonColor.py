from PySide6.QtWidgets import QPushButton, QGraphicsColorizeEffect
from PySide6.QtGui import QColor, QEnterEvent
from PySide6.QtCore import QPropertyAnimation, QEvent

class buttonColor(QPushButton):
    
    def __init__(self, name):
        
        super(buttonColor, self).__init__()
        
        self.text = name
        self.setObjectName = "Bruh"
        
        self.setStyleSheet("""
                           background-color: #348AA7;
                           """)
        
        # QGraphicsColorizeEffect only takes one arg, which is the parent argument
        self.colorEffect = QGraphicsColorizeEffect(self)
        
        # Set the color of the effect (the default is blue)
        self.colorEffect.setColor(QColor("lime"))
        
        # Sets the graphic effect we made to self.
        self.setGraphicsEffect(self.colorEffect)
        
        # We are animating the effect, and not the button itself. Also we are changing the color.
        self.colorAnim = QPropertyAnimation(self.colorEffect, b"color")
        # self.colorAnim.setStartValue(0)
        
        self.colorAnim.setDuration(1000)
        
    def enterEvent(self, event: QEnterEvent) -> None:
        print("Entered")
        self.colorAnim.setDirection(self.colorAnim.Direction.Forward)
        
        if self.colorAnim.state() == self.colorAnim.State.Stopped:
            
            # Since we are animating QColor here, the start and end values would be in QColors as well.
            self.colorAnim.setStartValue(QColor("lime"))
            self.colorAnim.setEndValue(QColor("gray"))
            self.colorAnim.start()
            
        return super().enterEvent(event)
            
    def leaveEvent(self, event: QEvent) -> None:
        print("Left")
        self.colorAnim.setDirection(self.colorAnim.Direction.Backward)
        
        if self.colorAnim.state() == self.colorAnim.State.Stopped:
            self.colorAnim.start()
            
        return super().leaveEvent(event)
    
    def mousePressEvent(self, e) -> None:
        print("clicked")
        return super().mousePressEvent(e)
                    
        
        
        
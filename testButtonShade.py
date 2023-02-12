from PySide6.QtWidgets import QPushButton, QGraphicsColorizeEffect
from PySide6.QtGui import QColor, QEnterEvent
from PySide6.QtCore import QPropertyAnimation, QEvent

class buttonShade(QPushButton):
    
    def __init__(self, name):
        
        super(buttonShade, self).__init__()
        
        self.text = name
        self.setObjectName = "Bruh"
        
        self.setStyleSheet("""
                           background-color: #348AA7;
                           """)
        
        # QGraphicsColorizeEffect only takes one arg, which is the parent argument
        self.colorEffect = QGraphicsColorizeEffect(self)
        
        # setStrength is talking about the "strength" of the colorization effect. goes from 0-1
        self.colorEffect.setStrength(0)
        
        # Set the color of the effect (the default is blue)
        self.colorEffect.setColor(QColor("red"))
        
        # Sets the graphic effect we made to self.
        self.setGraphicsEffect(self.colorEffect)
        
        # We are animating the effect, and not the button itself. Also we are changing the strength
        self.colorAnim = QPropertyAnimation(self.colorEffect, b"strength")
        # self.colorAnim.setStartValue(0)
        
        self.colorAnim.setDuration(1000)
        
    def enterEvent(self, event: QEnterEvent) -> None:
        print("Entered")
        self.colorAnim.setDirection(self.colorAnim.Direction.Forward)
        
        if self.colorAnim.state() == self.colorAnim.State.Stopped:
            self.colorAnim.setStartValue(0)
            self.colorAnim.setEndValue(1)
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
                    
        
        
        
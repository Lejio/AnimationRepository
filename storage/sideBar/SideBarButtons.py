from PySide6.QtWidgets import QPushButton, QGraphicsColorizeEffect
from PySide6.QtGui import QEnterEvent, QColor
from PySide6.QtCore import QEvent, QPropertyAnimation, Property, QEasingCurve
from sideBar.Style import Style

class SideBarButton(QPushButton):
    
    def __init__(self, 
                 curve = QEasingCurve.Type.Linear,
                 startColor: QColor = QColor("gray"),
                 endColor: QColor = QColor("snow"),
                 borderColor: QColor = QColor("gray"),
                 style = Style,
                 height = 28,
                 width = 60,
                 duration = 300):
        
        super(SideBarButton, self).__init__()

        self.borderColor = borderColor
        self.colorStart = startColor
        self.Style = style

        self.colorEnd = endColor
        self.setFixedSize(width, height)
        self.curve = curve
        self.duration = duration
        self.setup_animation()
        
    def setup_animation(self):
        
        self.setStyleSheet(self.Style(self.colorStart))
        
        self.animColor = QPropertyAnimation(self, b"color")
        self.animColor.setEasingCurve(self.curve)

        self.animColor.setDuration(self.duration)
        
        
    def mousePressEvent(self, e):
        
        print("Clicked")
        
    def enterEvent(self, event: QEnterEvent) -> None:
        self.animColor.setDirection(self.animColor.Direction.Forward)
        if self.animColor.state() == self.animColor.State.Stopped:
            
            self.animColor.setStartValue(self.colorStart)
            self.animColor.setEndValue(self.colorEnd)
            self.animColor.start()
        
        return super().enterEvent(event)
    
    def leaveEvent(self, event: QEvent) -> None:
        
        self.animColor.setDirection(self.animColor.Direction.Backward)
        if self.animColor.state() == self.animColor.State.Stopped:
            
            self.animColor.start()
        
        return super().leaveEvent(event)
        
    
    @Property(QColor)
    def color(self):
        
        return self.colorStart
    
    @color.setter
    def color(self, c):
        
        self.colorStart = c
        self.setStyleSheet(self.Style(c))
        
from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QEnterEvent, QColor
from PySide6.QtCore import QEvent, QPropertyAnimation, Property, QEasingCurve,  QParallelAnimationGroup
from sideBar.Style import Style

class SideBarButton(QPushButton):
    
    def __init__(self,
                 text = "", 
                 curve = QEasingCurve.Type.Linear,
                 startColor: QColor = QColor("gray"),
                 endColor: QColor = QColor("snow"),
                 borderColor: QColor = QColor("gray"),
                 endBorderColor: QColor = QColor("gray"),
                 startTextColor: QColor = QColor("black"),
                 endTextColor: QColor = QColor("black"),
                 style = Style,
                 height = 28,
                 width = 60,
                 duration = 300):
        
        super(SideBarButton, self).__init__()

        self.setText(text)
        self.borderColor = borderColor
        self.endBorderColor = endBorderColor
        self.startTextColor = startTextColor
        self.endTextColor = endTextColor
        
        self.colorStart = startColor
        self.Style = style

        self.colorEnd = endColor
        self.setFixedSize(width, height)
        self.curve = curve
        self.duration = duration
        self.setup_animation()
        
    def setup_animation(self):
        
        self.setStyleSheet(self.Style(self.colorStart))
        
        self.animColor = QPropertyAnimation(self, b"bgcolor")
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
    def bgcolor(self):
        
        return self.colorStart
    
    @bgcolor.setter
    def bgcolor(self, c):
        
        self.colorStart = c
        self.setStyleSheet(self.Style(c))
        
    @Property(QColor)
    def bordercolor(self):
        
        return self.borderColor
    
    @bordercolor.setter
    def bordercolor(self, c):
        
        self.borderColor = c
        # Somehow change bordercolor
        
    @Property(QColor)
    def textcolor(self):
        
        return self.startTextColor
    
    @textcolor.setter
    def textcolor(self, c):
        
        self.startTextColor = c
        # Change text color
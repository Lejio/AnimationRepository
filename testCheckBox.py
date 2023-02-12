from PySide6.QtWidgets import QPushButton, QCheckBox
from PySide6.QtCore import QRect, Property, QPropertyAnimation, QEasingCurve, Qt, QPoint
from PySide6.QtGui import QPainter, QPaintEvent, QColor, QMouseEvent


class testCheckBox (QCheckBox):
    
    def __init__(self,
                 width = 60,
                 height = 28,
                 animation_curve = QEasingCurve.Type.OutBounce
                 ) -> None:
        
        super(testCheckBox, self).__init__()
                
        self.setFixedSize(width, height)
        
        self.start_x = 3
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.animationCurve = animation_curve
        
        
        self.anim = QPropertyAnimation(self, b"startx")
        self.anim.setEasingCurve(animation_curve)
        self.anim.setDuration(500)
        
        self.stateChanged.connect(self.start_transition)
        
    def start_transition(self, value):
        
        self.anim.stop()
        
        if value:
            
            self.anim.setEndValue(self.width() - 25)
            
        else:
            
            self.anim.setEndValue(3)
            
        self.anim.start()
        
    def hitButton(self, pos: QPoint):
        
        return self.contentsRect().contains(pos)

    def paintEvent(self, e):
        
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        p.setPen(Qt.NoPen)
        
        rect = QRect(0, 0, self.width(), self.height())
        
        if not self.isChecked():
            
            p.setBrush(QColor("gray"))
            p.drawRoundedRect(0, 0, rect.width(), rect.height(), self.height()/2, self.height()/2)
            p.setBrush(QColor("snow"))
            # print(self.start_x)
            p.drawEllipse(self.start_x, 3, 22, 22)
            
        else:
            
            p.setBrush(QColor("lightgreen"))
            p.drawRoundedRect(0, 0, rect.width(), rect.height(), self.height()/2, self.height()/2)
            p.setBrush(QColor("snow"))
            # print(self.start_x)
            # print(rect.width())
            p.drawEllipse(self.start_x, 3, 22, 22)
            
        
        p.end()
        
            
    # @Property(int)
    # def bgcolor(self):
        
    #     return self.color
    
    
    # @bgcolor.setter
    # def bgcolor(self, color: int):
        
    #     self.color = color
    #     self.update()
    
    # def mouseDoubleClickEvent(self, e):
        
    #     print("performing animation..")
    #     anim = QPropertyAnimation(self, b"bgcolor")
    #     anim.setStartValue(QColor("snow"))
    #     anim.setEndValue(0)
    #     anim.setDuration(2500)
    #     anim.start()
    
    @Property(float)
    def startx(self):
        return self.start_x
    
    @startx.setter
    def startx(self, x):
        self.start_x = x
        self.update()

        
    
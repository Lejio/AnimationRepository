from PySide6.QtWidgets import QPushButton, QCheckBox
from PySide6.QtCore import QRect, Property, QPropertyAnimation, QEasingCurve, Qt, QPoint, QVariantAnimation
from PySide6.QtGui import QPainter, QPaintEvent, QColor, QMouseEvent

class testButton(QPushButton):
    
    def __init__(self,
                width = 60,
                height = 28,
                color = QColor("snow"),
                animation_curve = QEasingCurve.Type.Linear):
        
        super(testButton, self).__init__()
        
        self.setFixedSize(width, height)
        self.color = color
        
        # print("Qhat the fuck")
        self.anim = QVariantAnimation(self)
        # self.anim.setStartValue(self.color)
        self.anim.setEndValue(QColor("lightgreen"))
        self.anim.setEasingCurve(animation_curve)
        self.anim.setDuration(500)
        print(self.anim.keyValues)
        self.anim.updateCurrentValue(self.color)
        # self.anim.start()
        # self.anim.setEasingCurve(animation_curve)
        # self.anim.setDuration(500)
        
    
    def paintEvent(self, e):
        
        # print("drawing")
        
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        p.setPen(Qt.NoPen)
        
        rect = QRect(0, 0, self.width(), self.height())
        
        p.setBrush(self.color)
        p.drawRoundedRect(0, 0, rect.width(), rect.height(), rect.height()/2, rect.height()/2)
        
        p.end()
        
    def updateCurrentValue(self, e):
        
        print("Hello")
        
    def mousePressEvent(self, e):
        
        self.anim.start()
    
    # @Property(float)
    # def color(self):
    #     return self.color
    
    # @color.setter
    # def color(self, color):
    #     self.color = color
    #     self.update()
    
    # def mousePressEvent(self, e):
        
    #     self.anim.setEndValue(QColor("lightgreen"))
    #     self.anim.start()
    
    # def valueChanged
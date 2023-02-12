from PySide6.QtWidgets import QPushButton, QCheckBox, QWidget
from PySide6.QtCore import QRect, Property, QPropertyAnimation, QEasingCurve, Qt, QPoint, QEvent, QObject
from PySide6.QtGui import QPainter, QPaintEvent, QColor, QMouseEvent, QHoverEvent

class testWidget(QWidget):
    
    def __init__(self,
                 width = 50,
                 height = 0,
                 color = QColor("lightgray"),
                 setCurve = QEasingCurve.Type.OutBounce):
        
        super(testWidget, self).__init__()
        self.currWidth = width
        self.color = color
        self.currHeight = height
        self.setFixedWidth(width)
        self.setCurve = setCurve
        self.maxSize = self.currWidth * 5
        self.minimumSize = width
        
        self.anim = QPropertyAnimation(self, b"changewidth")
        self.anim.setDuration(500)
        self.anim.setEasingCurve(self.setCurve)
        self.setMouseTracking(True)
        
        # print(str(self.pos().x), str(self.pos().y))
        # if self.mouse
        self.installEventFilter(self)
        # hover = QHoverEvent(QHoverEvent.Type.HoverEnter)
        
        # self.event(hover)     
        # print(hover.pos())
    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        
        if watched == self:
            print("WTF")
        
        return super().eventFilter(watched, event)
        
        
    def paintEvent(self, e):
        
        self.setFixedWidth(self.currWidth)
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        p.setPen(Qt.NoPen)
        
        rect = QRect(0, 0, self.currWidth, self.currHeight)
        
        p.setBrush(self.color)
        p.drawRect(rect)
        
        p.end()
        
        
    def mousePressEvent(self, e):
        
        self.anim.setEndValue(self.minimumSize)
        self.anim.start()
        
    def mouseMoveEvent(self, e):
        
        self.anim.setEndValue(self.maxSize)
        self.anim.start()
        # self.anim.setEndValue(self.minimumSize)

    
    @Property(int)
    def changewidth(self):
        
        return self.currWidth
    
    @changewidth.setter
    def changewidth(self, w):
        
        self.currWidth = w
        self.update()
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
        
        
        # This here sets up the animation
        self.anim = QPropertyAnimation(self, b"changewidth")
        self.anim.setDuration(500)
        self.anim.setEasingCurve(self.setCurve)
        self.setMouseTracking(True)
        
        # This is used to "connect" a widget to an event filter. So now ever single event 
        # (related to this widget) will be passed to the eventfilter.
        # Here, I am installing an event filter for this current widget (which is just a rectangle)
        self.installEventFilter(self)

        
    ###############################################################################################
    # You can have an EventFilter. All events that occur goes to the event filter. Here you can
    # choose to detect certain events and do actions with them.
    # Every event filter comes with 3 parameters: self, watched and event.
    ###############################################################################################
    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        
        # For this widget, if the object passing the event is itself, and the type is mouse
        # entering itself, set the end value to max and run expanding animation.
        if ((watched == self) and (event.type() == QEvent.Type().Enter)):
            self.anim.setEndValue(self.maxSize)
            self.anim.start()
            
        # If the event thrown is itself, and the even is leaving the widget, minimize.
        elif ((watched == self) and (event.type() == QEvent.Type().Leave)):
            self.anim.setEndValue(self.minimumSize)
            self.anim.start()
        
        # The event filter must return the following:
        return super().eventFilter(watched, event)
        
    
    ###############################################################################################
    # Every widget will call a paintEvent when instantiating and animating. This event basically
    # draws the widget itself. You can customize the widget by drawing your own by using QPainter.
    ###############################################################################################
    def paintEvent(self, e):
        
        self.setFixedWidth(self.currWidth)
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        p.setPen(Qt.NoPen)
        
        rect = QRect(0, 0, self.currWidth, self.currHeight)
        
        p.setBrush(self.color)
        p.drawRect(rect)
        
        p.end()
        
    ###############################################################################################
    # Depricated events. I was experienting with specific mouse move event hoping it would achieve
    # a mouse hover effect I was looking for. Didn't quite work out.
    ###############################################################################################
    
    # def mousePressEvent(self, e):
        
    #     self.anim.setEndValue(self.minimumSize)
    #     self.anim.start()
        
    # def mouseMoveEvent(self, e):
        
    #     self.anim.setEndValue(self.maxSize)
    #     self.anim.start()
        # self.anim.setEndValue(self.minimumSize)

    ###############################################################################################
    # In order to run animations, you need to set up setters and getters for the custom property
    # you want to animate. Here, I want to animate the variable currWidth which is the current
    # width of the widget. Notice, when I create the QPropertyAnimation, I used the setter and 
    # getter's method names and not the currWidth (line 24).
    # The setter must end with a self.update(). Each QObject has this method, and it is used to
    # re-draw the widget (and this is where the paintEvent comes in).
    ###############################################################################################
    @Property(int)
    def changewidth(self):
        
        return self.currWidth
    
    @changewidth.setter
    def changewidth(self, w):
        
        self.currWidth = w
        self.update()
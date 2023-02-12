from PySide6.QtWidgets import QWidget, QApplication, QGraphicsOpacityEffect
from PySide6.QtCore import QPropertyAnimation, QPoint, QEasingCurve, QSize, QParallelAnimationGroup
import sys

# LINEAR
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.resize(600, 600)
#         self.child = QWidget(self)
#         self.child.setStyleSheet("background-color:red;border-radius:15px;")
#         self.child.resize(100, 100)
#         self.anim = QPropertyAnimation(self.child, b"pos")
#         self.anim.setEndValue(QPoint(400, 400))
#         self.anim.setDuration(1500)
#         self.anim.start()
        
# INOUTCUBIC     
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.resize(600, 600)
#         self.child = QWidget(self)
#         self.child.setStyleSheet("background-color:red;border-radius:15px;")
#         self.child.resize(100, 100)
#         self.anim = QPropertyAnimation(self.child, b"pos")
#         self.anim.setEasingCurve(QEasingCurve.OutInQuint)
#         self.anim.setEndValue(QPoint(400, 400))
#         self.anim.setDuration(1500)
#         self.anim.start()

# OUTINCUBIC
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.resize(600, 600)
#         self.child = QWidget(self)
#         self.child.setStyleSheet("background-color:red;border-radius:15px;")
#         self.child.resize(100, 100)
#         self.anim = QPropertyAnimation(self.child, b"pos")
#         self.anim.setEasingCurve(QEasingCurve.OutInCubic)
#         self.anim.setEndValue(QPoint(400, 400))
#         self.anim.setDuration(1500)
#         self.anim.start()

# OUTBOUNCE
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.resize(600, 600)
#         self.child = QWidget(self)
#         self.child.setStyleSheet("background-color:red;border-radius:15px;")
#         self.child.resize(100, 100)
#         self.anim = QPropertyAnimation(self.child, b"pos")
#         self.anim.setEasingCurve(QEasingCurve.OutBounce)
#         self.anim.setEndValue(QPoint(400, 400))
#         self.anim.setDuration(1500)
#         self.anim.start()

# SQUENCIAL MOVE AND GROW
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.resize(600, 600)
#         self.child = QWidget(self)
#         self.child.setStyleSheet("background-color:red;border-radius:15px;")
#         self.child.resize(100, 100)
#         self.anim = QPropertyAnimation(self.child, b"pos")
#         self.anim.setEndValue(QPoint(200, 200))
#         self.anim.setDuration(1500)
#         self.anim_2 = QPropertyAnimation(self.child, b"size")
#         self.anim_2.setEndValue(QSize(250, 150))
#         self.anim_2.setDuration(2000)
#         self.anim_group = QSequentialAnimationGroup()
#         self.anim_group.addAnimation(self.anim)
#         self.anim_group.addAnimation(self.anim_2)
#         self.anim_group.start()
    
# PARALLEL ANIMATION 
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.resize(600, 600)
#         self.child = QWidget(self)
#         effect = QGraphicsOpacityEffect(self.child)
#         self.child.setGraphicsEffect(effect)
#         self.child.setStyleSheet("background-color:red;border-radius:15px;")
#         self.child.resize(100, 100)
#         self.anim = QPropertyAnimation(self.child, b"pos")
#         self.anim.setEndValue(QPoint(200, 200))
#         self.anim.setDuration(1500)
#         self.anim_2 = QPropertyAnimation(effect, b"opacity")
#         self.anim_2.setStartValue(0)
#         self.anim_2.setEndValue(1)
#         self.anim_2.setDuration(2500)
#         self.anim_group = QParallelAnimationGroup()
#         self.anim_group.addAnimation(self.anim)
#         self.anim_group.addAnimation(self.anim_2)
#         self.anim_group.start()

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.child = QWidget(self)
        effect = QGraphicsOpacityEffect(self.child)
        self.child.setGraphicsEffect(effect)
        self.child.setStyleSheet("background-color:red;border-radius:15px;")
        self.child.resize(100, 100)
        
        # Creates the QProperty animation and sets the property name. This means that the widget self.child has the instance variable pos that could be editied.
        # The variable selector must have a getter and setter.
        self.anim = QPropertyAnimation(self.child, b"pos")
        # self.anim.propertyName()
        
        print("The property name is: " + self.anim.propertyName())
        
        # Start value set at the point 200px, 200px
        self.anim.setEndValue(QPoint(200, 200))
        
        # The duration is set in ms. 
        self.anim.setDuration(1500)
        
        self.anim_2 = QPropertyAnimation(effect, b"opacity")
        self.anim_2.setStartValue(0)
        self.anim_2.setEndValue(1)
        self.anim_2.setDuration(2500)
        self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(self.anim)
        self.anim_group.addAnimation(self.anim_2)
        self.anim_group.start()
app = QApplication(sys.argv)

window = Window()
window.show()

app.exec()


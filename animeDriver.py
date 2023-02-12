from PySide6.QtWidgets import QApplication
from animatePractice import animate
import sys




if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    w = animate("bruh")
    w.show()
    
    app.exec()
    
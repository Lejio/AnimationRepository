from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from sideBar.SideBarButtons import SideBarButton


class SideBar(QWidget):
    
    def __init__(self) -> None:
        
        self.row = QVBoxLayout()
        
        self.setLayout(self.row)
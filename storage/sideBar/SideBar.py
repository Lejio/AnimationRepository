from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from sideBar.SideBarButtons import SideBarButton
from sideBar.Style import Style


class SideBar(QWidget):
    
    def __init__(self) -> None:
        
        super(SideBar, self).__init__()
        
        self.row = QVBoxLayout()
        self.testButton = SideBarButton(text="Hello", style=Style)
        self.row.addWidget(self.testButton)
        self.setLayout(self.row)
        
        
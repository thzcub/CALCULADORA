
from PySide6.QtWidgets import  QMainWindow, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        
        self.cw = QWidget()
        self.vLayout= QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)
        
        self.setWindowTitle('Calculadora')
        
        
        
    def adjustFixedSize(self):
        # Última coisa a ser feita
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())   
    
    def addwidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
        
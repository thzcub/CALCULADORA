import sys

from display import Display
from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
#from styles import addTema
from variables import WINDOW_ICON_PATH
from botao import  ButtonsGrid
if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    #addTema()
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('conta')
    window.addwidgetToVLayout(info)

    # Displa
    display = Display()
    window.addwidgetToVLayout(display)
    
    #grid
    buttonsGrid= ButtonsGrid(display, info)
    window.vLayout.addLayout(buttonsGrid)


    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
    
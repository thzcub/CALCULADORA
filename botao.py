from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE
from utils import isEmpty, isNumOrDot, isValidNumber

from PySide6.QtCore import Slot
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from display import Display
    from info import Info

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
        
    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)
          


class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self._equation = ''
        self._left = None
        self._right = None
        self._makeGrid()
        self._op = None
    
    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)
            
    
    def _makeGrid(self):
        for rowNumber, rowData in enumerate(self._gridMask):
            for colNumber, buttonText in enumerate(rowData):
                button = Button(buttonText)

                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, rowNumber, colNumber)
                Slot = self._makeSlot(self._insertButtonTextToDisplay, button)
                self._connectButtonClicked(button, Slot )
                
    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)
        
    def _configSpecialButton(self, button):
        text = button.text()
   
        if text == 'C':
            #button.clicked.connect(self.display.clear)
            self._connectButtonClicked(button, self._clear)
            
        
        if text == '-=*/':
            self._connectButtonClicked(button, self._makeSlot, self._operatorClicked, button)    
        
    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot
                    
    def _insertButtonTextToDisplay(self, button):
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText
        
        if not isValidNumber(newDisplayValue):
            return
        self.display.insert(buttonText)
    
    def _clear(self):
        print('vou fazer outra coisa aqui')
        self.display.clear()
    
    def _operatorClicked(self, button):
        buttonText = button.text()
        displayText = self.display.text()
        self.display.clear()
        
        if not isValidNumber(displayText) and self._left is None:
            print('fgf')
            return
        
        print(buttonText)
         
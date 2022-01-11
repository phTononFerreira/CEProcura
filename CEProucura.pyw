from re import A
from buscaCEP import buscarCEP
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.x = 100 
        self.y = 100

        self.width = 350  
        self.height = 280 
        self.setFixedSize(self.width, self.height)

        self.name = 'CEPROCURA'

        self.setWindowIcon(QIcon('icon.png'))

        self.setStyleSheet("background-color: black;")

        self.MainLabel = QLabel(self)                                                            
        self.MainLabel.setText('CEPROCURA')                                                           
        self.MainLabel.move(75, 20)                                                               
        self.MainLabel.resize(220,40)
        self.MainLabel.setFont(QFont('Century Gothic',10))                                   
        self.MainLabel.setStyleSheet('QLabel {color:#B82C2C; font-size:35px}')    
        
        self.imgCEProcura = QLabel(self)
        self.imgCEProcura.setPixmap(QPixmap('icon.png'))
        self.imgCEProcura.setScaledContents(True)
        self.imgCEProcura.move(25,15)
        self.imgCEProcura.resize(50,50)


        self.lblForm = QLabel(self)                                                            
        self.lblForm.setText('Digite o CEP:')                                                           
        self.lblForm.move(30, 78)                                                               
        self.lblForm.resize(100,20)
        self.lblForm.setFont(QFont('Century Gothic',10))                                                           
        self.lblForm.setStyleSheet('QLabel {color:#9C3333; font: bold; font-size:15px}')     

        self.lblStatus = QLabel(self)                                                            
        self.lblStatus.setText('')                                                           
        self.lblStatus.move(30, 125)                                                               
        self.lblStatus.resize(140,20)
        self.lblStatus.setFont(QFont('Century Gothic',10))                                                              
        self.lblStatus.setStyleSheet('QLabel {color:#DEBA2C; font: bold; font-size:15px}')   

        self.formCEP = QLineEdit(self)
        self.formCEP.move(30,100)
        self.formCEP.resize(200,25)
        self.formCEP.setMaxLength(8)
        self.formCEP.setStyleSheet('QLineEdit {border: 2px solid red; border-radius: 4px; color:#9C3333; background-color:#000000; font:arial; font-size:15px}')  

        self.btoProcurar = QPushButton('Procurar', self)                                                      
        self.btoProcurar.move(240, 100)                                                                        
        self.btoProcurar.resize(80,25)                                                                      
        self.btoProcurar.setStyleSheet('QPushButton {border: 2px solid red; border-radius: 4px; background-color:#000000; color:#9C3333;font:bold; font-size:15px}')  
        self.btoProcurar.clicked.connect(self.procurar) 


        self.lblCEP = QLabel(self)                                                            
        self.lblCEP.setText('CEP:')                                                           
        self.lblCEP.move(30, 150)                                                               
        self.lblCEP.resize(300,20)                                                               
        self.lblCEP.setStyleSheet('QLabel {color:#CCCCCC; font: bold; font-size:15px}')

        self.lblESTADO = QLabel(self)                                                            
        self.lblESTADO.setText('ESTADO:')                                                           
        self.lblESTADO.move(30, 170)                                                               
        self.lblESTADO.resize(300,20)                                                               
        self.lblESTADO.setStyleSheet('QLabel {color:#CCCCCC; font: bold; font-size:15px}')

        self.lblCIDADE = QLabel(self)                                                            
        self.lblCIDADE.setText('CIDADE:')                                                           
        self.lblCIDADE.move(30, 190)                                                               
        self.lblCIDADE.resize(300,20)                                                               
        self.lblCIDADE.setStyleSheet('QLabel {color:#CCCCCC; font: bold; font-size:15px}')

        self.lblBAIRRO = QLabel(self)                                                            
        self.lblBAIRRO.setText('BAIRRO:')                                                           
        self.lblBAIRRO.move(30, 210)                                                               
        self.lblBAIRRO.resize(300,20)                                                               
        self.lblBAIRRO.setStyleSheet('QLabel {color:#CCCCCC; font: bold; font-size:15px}')

        self.lblRUA = QLabel(self)                                                            
        self.lblRUA.setText('RUA:')                                                           
        self.lblRUA.move(30, 230)                                                               
        self.lblRUA.resize(300,20)                                                               
        self.lblRUA.setStyleSheet('QLabel {color:#CCCCCC; font: bold; font-size:15px}')
        self.load_window()

        self.lblCEP.setFont(QFont('Century Gothic',10))
        self.lblESTADO.setFont(QFont('Century Gothic',10))
        self.lblCIDADE.setFont(QFont('Century Gothic',10))
        self.lblBAIRRO.setFont(QFont('Century Gothic',10))
        self.lblRUA.setFont(QFont('Century Gothic',10))

    def load_window(self):
        self.setGeometry(self.x, self.y, self.width, self.height) 
        self.setWindowTitle(self.name) 
        
        self.show()

    def procurar(self):
        cepInfo = buscarCEP(self.formCEP.text())
        if cepInfo:
            self.lblStatus.setText('')  
            self.lblCEP.setText('CEP: ' + cepInfo[0]['cep'])
            self.lblESTADO.setText('ESTADO: ' + cepInfo[0]['estado'])
            self.lblCIDADE.setText('CIDADE: ' + cepInfo[0]['cidade'])
            self.lblBAIRRO.setText('BAIRRO: ' + cepInfo[0]['bairro'])
            self.lblRUA.setText('RUA: ' + cepInfo[0]['rua'])
        else:
            self.lblStatus.setText('CEP INVÁLIDO')  

aplicacao = QApplication(sys.argv) 
j = window()             
sys.exit(aplicacao.exec())
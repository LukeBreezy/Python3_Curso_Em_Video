import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QTextEdit


class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        # Dimensões da janela principal
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = 'Primeira Janela'

        # Definições do Botão 1
        botao1 = QPushButton('Botão 1', self)
        botao1.move(30, 60)
        botao1.resize(50, 25)
        botao1.setStyleSheet('QPushButton {background-color: green; font: bold; font-size: 12px}')
        botao1.clicked.connect(self.botao1_click)

        # Definições do Botão 2
        botao2 = QPushButton('Botão 2', self)
        botao2.move(100, 60)
        botao2.resize(50, 25)
        botao2.setStyleSheet('QPushButton {background-color: red; font: bold; font-size: 12px}')
        botao2.clicked.connect(self.botao2_click)

        # Definições da Label 1
        self.label1 = QLabel(self)
        self.label1.move(30, 30)
        self.label1.resize(150, 20)
        self.label1.setStyleSheet('QLabel {background-color: orange; font: bold; font-size: 14px; color: black; border-radius: 90px}')
        self.label1.setText('Pressione um botão')

        # Teste TExto
        self.txt = QTextEdit(self)
        self.txt.move(500, 500)
        self.txt.resize(150, 20)
        self.txt.setText('Teste Funcionando')


        self.CarregarJanela()   # Este deve ser o ultimo comando da função

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self):
        self.label1.setText('Botao 1 Clicado')
        self.label1.setStyleSheet('QLabel {background-color: green; font: bold; font-size: 14px; color: black; border-radius: 90px}')
        teste = self.txt.toPlainText()
        print(teste)

    def botao2_click(self):
        self.label1.setText('Botao 2 Clicado')
        self.label1.setStyleSheet('QLabel {background-color: red; font: bold; font-size: 14px; color: black; border-radius: 90px}')


app = QApplication(sys.argv)
jan = Janela()
sys.exit(app.exec_())

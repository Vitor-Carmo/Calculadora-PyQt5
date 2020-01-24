from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from Interface_Calculadora import Ui_Janela_inteira


class JanelaCalculadora(QMainWindow, Ui_Janela_inteira):
    Primeiro_numero = None
    Esta_digitando_segundo_numero = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        #  butões na calculadora

        self.pushButton_5.clicked.connect(self.butao_precionado)   # 9
        self.pushButton_6.clicked.connect(self.butao_precionado)   # 8
        self.pushButton_7.clicked.connect(self.butao_precionado)   # 7
        self.pushButton_9.clicked.connect(self.butao_precionado)   # 4
        self.pushButton_10.clicked.connect(self.butao_precionado)  # 5
        self.pushButton_11.clicked.connect(self.butao_precionado)  # 6
        self.pushButton_13.clicked.connect(self.butao_precionado)  # 1
        self.pushButton_14.clicked.connect(self.butao_precionado)  # 2
        self.pushButton_15.clicked.connect(self.butao_precionado)  # 3
        self.pushButton_17.clicked.connect(self.butao_precionado)  # 0

        self.pushButton_19.clicked.connect(self.decimal_precionado)  # .
        self.pushButton_3.clicked.connect(self.porcentagem_precionado)  # %
        self.pushButton.clicked.connect(self.clear)  # C
        self.pushButton_2.clicked.connect(self.porcentagem_precionado)  # +/-  ---> veja a função caso teha duvida,
                                                                        #          o nome não é intuitivo
        #  Operações

        self.pushButton_12.clicked.connect(self.operacao_precionada)  # -
        self.pushButton_8.clicked.connect(self.operacao_precionada)  # +
        self.pushButton_4.clicked.connect(self.operacao_precionada)  # *
        self.pushButton_16.clicked.connect(self.operacao_precionada)  # /

        self.pushButton_12.setCheckable(True)  # -
        self.pushButton_8.setCheckable(True)   # +
        self.pushButton_4.setCheckable(True)   # *
        self.pushButton_16.setCheckable(True)  # /

        # igual
        self.pushButton_20.clicked.connect(self.igual_precionado)  # ==

    def keyPressEvent(self, e):  # funções do teclado

        numeros_tela = self.label.text()

        if numeros_tela == '-0':
            numeros_tela = '0'
            self.label.setText(numeros_tela)

        if e.key() == Qt.Key_Backspace:          # pra apagar um por um na tela com o back espace

            if numeros_tela != '0':

                if float(numeros_tela) < 0 and len(numeros_tela) == 2:
                    numeros_tela = numeros_tela[:-2]
                else:
                    numeros_tela = numeros_tela[:-1]
                if len(numeros_tela) == 0:
                    numeros_tela = '0'

                self.label.setText(numeros_tela)

        # se apertar esc sai do aplicativo
        if e.key() == Qt.Key_Escape:
            exit()

        # numeros do teclado aparecer na tela
        if e.key() == Qt.Key_0:
            self.butao_precionado(teclado=True, valor='0')
        elif e.key() == Qt.Key_1:
            self.butao_precionado(teclado=True, valor='1')
        elif e.key() == Qt.Key_2:
            self.butao_precionado(teclado=True, valor='2')
        elif e.key() == Qt.Key_3:
            self.butao_precionado(teclado=True, valor='3')
        elif e.key() == Qt.Key_4:
            self.butao_precionado(teclado=True, valor='4')
        elif e.key() == Qt.Key_5:
            self.butao_precionado(teclado=True, valor='5')
        elif e.key() == Qt.Key_6:
            self.butao_precionado(teclado=True, valor='6')
        elif e.key() == Qt.Key_7:
            self.butao_precionado(teclado=True, valor='7')
        elif e.key() == Qt.Key_8:
            self.butao_precionado(teclado=True, valor='8')
        elif e.key() == Qt.Key_9:
            self.butao_precionado(teclado=True, valor='9')

        # operações
        if e.key() == Qt.Key_Plus:
            self.operacao_precionada(teclado=True, operacao='+')
        elif e.key() == Qt.Key_Minus:
            self.operacao_precionada(teclado=True, operacao='-')
        elif e.key() == Qt.Key_Asterisk:
            self.operacao_precionada(teclado=True, operacao='*')
        elif e.key() == Qt.Key_Slash:
            self.operacao_precionada(teclado=True, operacao='/')

        # igual
        if e.key() == Qt.Key_Enter:
            self.igual_precionado()

        # decimal
        if e.key() == Qt.Key_Period:
            self.decimal_precionado()

        elif e.key() == Qt.Key_Comma:
            self.decimal_precionado()

    def butao_precionado(self, teclado=False, valor='0'):
        if not teclado:
            butao = self.sender()

            if (
                    self.pushButton_4.isChecked() or
                    self.pushButton_8.isChecked() or
                    self.pushButton_12.isChecked() or
                    self.pushButton_16.isChecked()
            ) and (not self.Esta_digitando_segundo_numero):

                numeros_tela = format(float(butao.text()), '.15g')

                self.Esta_digitando_segundo_numero = True

            else:

                if ('.' in self.label.text()) and (butao.text() == "0"):
                    numeros_tela = format(self.label.text() + butao.text(), '.15')

                else:
                    numeros_tela = format(float(self.label.text() + butao.text()), '.15g')
        else:
            butao = valor

            if (
                    self.pushButton_4.isChecked() or
                    self.pushButton_8.isChecked() or
                    self.pushButton_12.isChecked() or
                    self.pushButton_16.isChecked()
            ) and (not self.Esta_digitando_segundo_numero):

                numeros_tela = format(float(butao), '.15g')

                self.Esta_digitando_segundo_numero = True

            else:

                if ('.' in self.label.text()) and (butao == "0"):
                    numeros_tela = format(self.label.text() + butao, '.15')

                else:
                    numeros_tela = format(float(self.label.text() + butao), '.15g')

        self.label.setText(numeros_tela)

    def decimal_precionado(self):
        tela = self.label.text()

        if '.' not in tela:
            self.label.setText(self.label.text() + '.')

    def porcentagem_precionado(self,):
        butao = self.sender()

        label_numero = float(self.label.text())

        if butao.text() == '+/-':
            label_numero *= -1
        else:
            label_numero *= 0.01

        numeros_tela = format(label_numero, '.15g')
        self.label.setText(numeros_tela)

    def clear(self):

        self.pushButton_12.setChecked(False)  # -
        self.pushButton_8.setChecked(False)  # +
        self.pushButton_4.setChecked(False)  # *
        self.pushButton_16.setChecked(False)  # /

        self.Esta_digitando_segundo_numero = False
        self.label.setText('0')

    def operacao_precionada(self, teclado=False, operacao='+'):
        if not teclado:
            butao = self.sender()

            butao.setChecked(True)

        else:

            if operacao == '+':
                self.pushButton_8.setChecked(True)
            elif operacao == '-':
                self.pushButton_12.setChecked(True)
            elif operacao == '*':
                self.pushButton_4.setChecked(True)
            elif operacao == '/':
                self.pushButton_16.setChecked(True)

        self.Primeiro_numero = float(self.label.text())

    def igual_precionado(self):

        Segundo_numero = float(self.label.text())

        if self.pushButton_8.isChecked():
            resultado = self.Primeiro_numero + Segundo_numero
            numeros_tela = format(resultado, '.15g')
            self.label.setText(numeros_tela)
            self.pushButton_8.setChecked(False)

        elif self.pushButton_12.isChecked():
            resultado = self.Primeiro_numero - Segundo_numero
            numeros_tela = format(resultado, '.15g')
            self.label.setText(numeros_tela)
            self.pushButton_12.setChecked(False)

        elif self.pushButton_4.isChecked():
            resultado = self.Primeiro_numero * Segundo_numero
            numeros_tela = format(resultado, '.15g')
            self.label.setText(numeros_tela)
            self.pushButton_4.setChecked(False)

        elif self.pushButton_16.isChecked():
            resultado = self.Primeiro_numero / Segundo_numero
            numeros_tela = format(resultado, '.15g')
            self.label.setText(numeros_tela)
            self.pushButton_16.setChecked(False)

        self.Esta_digitando_segundo_numero = False

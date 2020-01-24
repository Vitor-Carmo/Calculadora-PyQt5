import sys
from PyQt5.QtWidgets import QApplication
from calculadora import JanelaCalculadora
try:
    aplicacao = QApplication(sys.argv)

    calculadora = JanelaCalculadora()

    sys.exit(aplicacao.exec_())
except:
    sys.exit(aplicacao.exec_())
import sys
from PyQt5.QtWidgets import QApplication
from calculadora import JanelaCalculadora

aplicacao = QApplication(sys.argv)

calculadora = JanelaCalculadora()

sys.exit(aplicacao.exec_())

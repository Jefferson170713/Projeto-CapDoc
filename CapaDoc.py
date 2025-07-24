import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon
from Program_Windows.PackagesByProcedures import CapaDocPackagesByProcedures

from PyQt5.QtWidgets import QWidget

# Classe principal da aplicação
class CapaDoc(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Capa-Doc')
        self.setGeometry(100, 100, 700, 450)
        self.setWindowIcon(QIcon(r'./Arquivos/logo/logo.ico'))
        self.capa_doc = QTabWidget()
        self.create_packages_by_procedures = QWidget()
        self.package_by_procedures = CapaDocPackagesByProcedures(parent=self)

        self.createview()

    # Função para criar as abas do programa
    def createview(self):
        space = 5 * ' '
        self.setCentralWidget(self.capa_doc)
        self.capa_doc.addTab(self.create_packages_by_procedures, f'{space}Pacote por Procedimento{space}')
        self.capa_doc.setDocumentMode(True)
        self.capa_doc.setMovable(True)
        self.package_by_procedures.create_packages_by_procedures_window(self.create_packages_by_procedures)

# Loop do programa em funcionamento
def main():
    app = QApplication(sys.argv)
    window = CapaDoc()
    window.show()
    sys.exit(app.exec_())

# Verifica se o arquivo é executado diretamente
if __name__ == "__main__":
    main()
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon
# from DescredWindow import DescredWindow

from PyQt5.QtWidgets import QWidget

# Classe principal da aplicação
class CapaDoc(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Capa-Doc')
        self.setGeometry(100, 100, 700, 450)
        self.setWindowIcon(QIcon(r'./Arquivos/logo/logo.ico'))
        self.capa_doc = QTabWidget()
        self.create_capa_doc = QWidget()
        #self.procedure_descred = DescredWindow(parent=self)

        self.createview()

    # Função para criar as abas do programa
    def createview(self):
        space = 5 * ' '
        self.setCentralWidget(self.capa_doc)
        self.capa_doc.addTab(self.create_capa_doc, f'{space} Descredenciamento Total {space}')
        self.capa_doc.setDocumentMode(True)
        self.capa_doc.setMovable(True)
        #self.procedure_descred.create_descred_window(self.provider_descred)

# Loop do programa em funcionamento
def main():
    app = QApplication(sys.argv)
    window = CapaDoc()
    window.show()
    sys.exit(app.exec_())

# Verifica se o arquivo é executado diretamente
if __name__ == "__main__":
    main()
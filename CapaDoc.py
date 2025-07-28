import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon
from Program_Windows.PackagesByProcedures import CapaDocPackagesByProcedures

# Classe principal da aplicação
class CapaDoc(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('CAPA-DOC')
        self.setGeometry(100, 100, 700, 500)
        
        # Detectar se está rodando como executável ou em desenvolvimento
        if getattr(sys, 'frozen', False):
            # Executável PyInstaller
            application_path = os.path.dirname(sys.executable)
            icon_path = os.path.join(application_path, 'Arquivos', 'logo', 'simb_cap_doc-removebg-preview.ico')
        else:
            # Desenvolvimento normal
            icon_path = os.path.join(os.path.dirname(__file__), 'Arquivos', 'logo', 'simb_cap_doc-removebg-preview.ico')
        
        # Verificar se o ícone existe e aplicar
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
            print(f"Ícone carregado: {icon_path}")
        else:
            print(f"Ícone não encontrado: {icon_path}")
        
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
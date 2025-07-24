import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QGroupBox
import os
import sys
import itertools
import numpy as np
import time
import locale
# Configura a localidade para o formato brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Adiciona o diretório pai ao path para importar módulos da pasta Arquivos
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
from Program_Extractions_In_Sql.SqlPackageByProcedures import QueryPackageByProcedure

class CapaDocPackagesByProcedures:
    def __init__(self, parent=None):
        self.parent = parent
        self.file_path = None
        self.output_path = None
        self.progress_bar_process_packages_by_procedures = None
        self.df = pd.DataFrame() 
        
        # Checkboxes for list of operators
        self.checkbox_hapvida = None
        self.checkbox_ccg = None
        self.checkbox_clinipam = None
        self.checkbox_ndi_minas = None
        self.checkbox_ndi_saude = None
        
        # search fild
        self.search_input_packages_by_procedures = None
        
        # Table for displaying data
        self.table_packages_by_procedures = None
        
    def create_packages_by_procedures_window(self, packeges_by_procedures_widget):
        # Layout principal
        main_layout = QVBoxLayout()
        
        # ========== SEÇÃO Pacote pro Procediemnto ==========
        # Grupo para Status e Progresso
        group_status_progress = QGroupBox("Status e Progresso")
        layout_status_progress = QVBoxLayout()

        # Status layout
        status_layout_desc = QHBoxLayout()
        self.label_status_procedures = QLabel("Nenhum arquivo carregado - Pacote por Procedimento.")
        status_layout_desc.addWidget(self.label_status_procedures)
        status_layout_desc.addStretch()

        btn_clean_status_procedures = QPushButton("Limpar Status")
        btn_clean_status_procedures.setFixedSize(150, 35)
        btn_clean_status_procedures.clicked.connect(self.clear_status_capa)
        status_layout_desc.addWidget(btn_clean_status_procedures)
        layout_status_progress.addLayout(status_layout_desc)

        # Barra de progresso
        self.progress_bar_process_procedures = QProgressBar()
        self.progress_bar_process_procedures.setValue(0)
        self.progress_bar_process_procedures.setMinimum(0)
        self.progress_bar_process_procedures.setMaximum(100)
        layout_status_progress.addWidget(self.progress_bar_process_procedures)

        group_status_progress.setLayout(layout_status_progress)
        main_layout.addWidget(group_status_progress)
        
        # Grupo para Filtros e Pesquisa
        group_filters_search = QGroupBox("Filtros e Pesquisa")
        layout_filters_search = QVBoxLayout()

        # 5 Checkboxes
        checkboxe_layout_procedures = QHBoxLayout()
        self.checkbox_hapvida = QCheckBox("HAPVIDA")
        self.checkbox_ccg = QCheckBox("CCG")
        self.checkbox_clinipam = QCheckBox("CLINIPAM")
        self.checkbox_ndi_minas = QCheckBox("NDI MINAS")
        self.checkbox_ndi_saude = QCheckBox("NDI SAÚDE")

        checkboxe_layout_procedures.addWidget(self.checkbox_hapvida)
        checkboxe_layout_procedures.addWidget(self.checkbox_ccg)
        checkboxe_layout_procedures.addWidget(self.checkbox_clinipam)
        checkboxe_layout_procedures.addWidget(self.checkbox_ndi_minas)
        checkboxe_layout_procedures.addWidget(self.checkbox_ndi_saude)
        layout_filters_search.addLayout(checkboxe_layout_procedures)

        # Campo de pesquisa
        search_layout_capa = QHBoxLayout()
        self.search_input_capa = QLineEdit()
        self.search_input_capa.setFixedHeight(30)
        self.search_input_capa.setPlaceholderText("Digite CAPA que deseja pesquisar...")
        search_layout_capa.addWidget(self.search_input_capa)

        btn_search_capa = QPushButton("Pesquisar CAPA")
        btn_search_capa.setFixedSize(150,35)
        btn_search_capa.clicked.connect(self.search_capa)
        search_layout_capa.addWidget(btn_search_capa)
        layout_filters_search.addLayout(search_layout_capa)

        group_filters_search.setLayout(layout_filters_search)
        main_layout.addWidget(group_filters_search)
        
        # Grupo para carregar a tabela
        group_table = QGroupBox("Tabela de Procedimentos")
        layout_table = QVBoxLayout()
        self.table_packages_by_procedures = QTableWidget()
        self.table_packages_by_procedures.setMaximumHeight(150)
        layout_table.addWidget(self.table_packages_by_procedures)
        group_table.setLayout(layout_table)
        main_layout.addWidget(group_table)
        
        # Grupo específico para o botão
        group_button = QGroupBox('Processamento')
        button_layout = QHBoxLayout()
        button_layout.addStretch()  # Espaço à esquerda

        btn_process_and_save = QPushButton("Processar e Salvar")
        btn_process_and_save.setFixedSize(150, 35)
        btn_process_and_save.clicked.connect(self.process_and_save_packages_by_procedures)
        button_layout.addWidget(btn_process_and_save)

        button_layout.addStretch()  # Espaço à direita
        group_button.setLayout(button_layout)
        main_layout.addWidget(group_button)
        
        packeges_by_procedures_widget.setLayout(main_layout)
        
    def get_current_date(self):
        # Pega a data atual no formato dd_mm_yyyy
        return time.strftime("%d_%m_%Y")
    
    def get_format_int(self, value):
        return locale.format_string('%.f', value, grouping=True)
    
    def clear_status_capa(self):
        self.label_status_procedures.setText("Nenhum arquivo carregado - Pacote por Procedimento.")
        self.progress_bar_process_procedures.setValue(0)
        self.table_packages_by_procedures.clearContents()
        self.table_packages_by_procedures.setRowCount(0)
        self.table_packages_by_procedures.setColumnCount(0)
        
        
    def search_capa(self):
        search_capa = self.search_input_capa.text().strip()
        # path_drive = r'../Arquivos/Oracle_jdbc/ojdbc8.jar'
        script_dir = os.path.dirname(os.path.abspath(__file__))
        path_drive = os.path.join(script_dir, '..', 'Arquivos', 'Oracle_jdbc', 'ojdbc8.jar')
        
        if search_capa:
            try:
                list_empresa = []
                
                if self.checkbox_hapvida.isChecked():
                    list_empresa.append('1')
                if self.checkbox_ccg.isChecked():
                    list_empresa.append('8')
                if self.checkbox_clinipam.isChecked():
                    list_empresa.append('9')
                if self.checkbox_ndi_minas.isChecked():
                    list_empresa.append('10')
                if self.checkbox_ndi_saude.isChecked():
                    list_empresa.append('14')
                
                list_empresa = ', '.join(map(str, list_empresa))
                
                if not list_empresa:
                    QMessageBox.warning(self.parent, "AVISO - CAPA", "Por favor, selecione uma operadora.\n\n - HAPVIDA\n - CCG\n - CLINIPAM\n - NDI MINAS\n - NDI SAÚDE")
                    return
                
                jdbc_permission = QueryPackageByProcedure(path_drive)
                
                self.df = jdbc_permission.fetch_data(chunk_size=50000, capa=search_capa, list_empresa=list_empresa, progress_bar=self.progress_bar_process_procedures)
                
                number_lines = self.get_format_int(self.df.shape[0])
                self.label_status_procedures.setText(f"{number_lines} linhas carregadas - Capa.")
                
                self.table_packages_by_procedures.setRowCount(self.df.shape[0])
                self.table_packages_by_procedures.setColumnCount(self.df.shape[1])
                self.table_packages_by_procedures.setHorizontalHeaderLabels(self.df.columns.tolist())
                
                for row_idx, row_data in self.df.iterrows():
                    for col_idx, value in enumerate(row_data):
                        item = QTableWidgetItem(str(value))
                        self.table_packages_by_procedures.setItem(row_idx, col_idx, item)
                
            except Exception as error:
                QMessageBox.critical(self.parent, "Erro", f"Ocorreu um erro ao buscar os dados: {str(error)}")
                
        else:
            QMessageBox.warning(self.parent, "AVISO - CAPA", "Por favor, insira um termo de pesquisa válido.")
        
    def process_and_save_packages_by_procedures(self):
        ...
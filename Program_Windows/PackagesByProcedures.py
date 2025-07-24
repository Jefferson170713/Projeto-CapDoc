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
import itertools
import numpy as np
import time
import locale
# Configura a localidade para o formato brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

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
        # Grupo para Pacote pro Procediemnto
        group_package_by_procedure = QGroupBox("CAPA - Aba Pacote por Procedimento")
        layout_package_by_procedures = QVBoxLayout()
        
        # Status layout para Pacote pro Procediemnto
        status_layout_desc = QHBoxLayout()
        self.label_status_procedures = QLabel("Nenhum arquivo carregado - Pacote por Procedimento.")
        status_layout_desc.addWidget(self.label_status_procedures)
        status_layout_desc.addStretch()
        
        btn_clean_status_procedures = QPushButton("Limpar Status")
        btn_clean_status_procedures.setFixedSize(100, 35)
        btn_clean_status_procedures.clicked.connect(self.clear_status_capa)
        status_layout_desc.addWidget(btn_clean_status_procedures)
        layout_package_by_procedures.addLayout(status_layout_desc)
        
        # Barra de progresso para Pacote pro Procediemnto
        self.progress_bar_process_procedures = QProgressBar()
        self.progress_bar_process_procedures.setValue(0)
        self.progress_bar_process_procedures.setMinimum(0)
        self.progress_bar_process_procedures.setMaximum(100)
        layout_package_by_procedures.addWidget(self.progress_bar_process_procedures)
        
        # 5 Checkboxes para Pacote pro Procediemnto
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
        layout_package_by_procedures.addLayout(checkboxe_layout_procedures)
        
        # Campo de pesquisa e botão para Pacote pro Procediemnto
        search_layout_capa = QHBoxLayout()
        self.search_input_capa = QLineEdit()
        self.search_input_capa.setFixedHeight(30)
        self.search_input_capa.setPlaceholderText("Digite CAPA que deseja pesquisar...")
        search_layout_capa.addWidget(self.search_input_capa)
        
        btn_search_capa = QPushButton("Pesquisar CAPA")
        btn_search_capa.setFixedSize(100,35)
        btn_search_capa.clicked.connect(self.search_capa)
        search_layout_capa.addWidget(btn_search_capa)
        layout_package_by_procedures.addLayout(search_layout_capa)
        
        # Tabela para Pacote pro Procediemnto
        self.table_capa_package_by_procedures = QTableWidget()
        self.table_capa_package_by_procedures.setMaximumHeight(150)  # Mostra aproximadamente 5 linhas
        layout_package_by_procedures.addWidget(self.table_capa_package_by_procedures)
        
        group_package_by_procedure.setLayout(layout_package_by_procedures)
        main_layout.addWidget(group_package_by_procedure)
        
        # Grupo específico para o botão
        group_button = QGroupBox()
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
        ...
    def search_capa(self):
        ...
    def process_and_save_packages_by_procedures(self):
        ...
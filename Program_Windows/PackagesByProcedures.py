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

        btn_clean_status_procedures = QPushButton("🔄 Limpar Status")
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
                
                # Para receber a 1000 primeiras linhas do DataFrame
                if self.df.shape[0] < 1000:
                    df = self.df.copy()
                else:
                    df = self.df[self.df.index < 1000].copy()
                
                self.table_packages_by_procedures.setRowCount(df.shape[0])
                self.table_packages_by_procedures.setColumnCount(df.shape[1])
                self.table_packages_by_procedures.setHorizontalHeaderLabels(df.columns.tolist())
                
                for row_idx, row_data in df.iterrows():
                    for col_idx, value in enumerate(row_data):
                        item = QTableWidgetItem(str(value))
                        self.table_packages_by_procedures.setItem(row_idx, col_idx, item)
                
                print(self.df.columns.tolist())
                
            except Exception as error:
                QMessageBox.critical(self.parent, "Erro", f"Ocorreu um erro ao buscar os dados: {str(error)}")
                
        else:
            QMessageBox.warning(self.parent, "AVISO - CAPA", "Por favor, insira um termo de pesquisa válido.")
        
    def process_and_save_packages_by_procedures(self):
        
        save_path = QFileDialog.getExistingDirectory(self.parent, "Selecione a pasta para salvar os arquivos", os.getcwd())
        if not save_path:
            QMessageBox.warning(self.parent, "AVISO - CAPA", "Nenhuma pasta selecionada para salvar os arquivos.")
            return
        
        self.initial_treatments()
        self.df = self.group_columns(self.df)
        self.df = self.number_of_networks_and_networks(self.df)
        self.df = self.ungoroup_columns(self.df)
        name_capa = self.search_input_capa.text().strip()
        self.save_to_excel(self.df, save_path, name_capa)
        print(self.df.head())             
    
    # 1. Initial treatments for the dataframe
    def initial_treatments(self):
        print(f'1. Função de tratamento \n 1.')
        self.df.CD_PROCEDIMENTO = self.treatment_serie(self.df.CD_PROCEDIMENTO)
        print(f'1.1 ')
        self.df.CD_PROCEDIMENTO_TUSS = self.treatment_serie(self.df.CD_PROCEDIMENTO_TUSS)
        print(f'1.2 ')
        self.df.URG_ELE_TAX_MAT_MED_CIR_ANE_AUX = self.upper_columns(self.df.URG_ELE_TAX_MAT_MED_CIR_ANE_AUX)
        
    # 1.1 Function to treat a pandas Series   
    def treatment_serie(self, serie):
        serie = serie.astype(str).fillna('-')
        return serie.astype(str).str.upper().str.strip().replace(';', ': ', regex=True)

    # 1.2 Função upper para as colunas do DataFrame
    def upper_columns(self, series):
        return series.str.upper()
    
    # 2. Função para criar a chave de rede
    def group_columns(self, df):
        df['KEY'] = (
            df['TABELA'].astype(str) + '@@' +
            df['LOCAL_CAPA'].astype(str) + '@@' +
            df['CD_PROCEDIMENTO'].astype(str) + '@@' +
            df['CD_PROCEDIMENTO_TUSS'].astype(str) + '@@' +
            df['NM_PROCEDIMENTO'].astype(str) + '@@' +
            df['NM_PROCEDIMENTO_TUSS'].astype(str) + '@@' +
            df['NU_ORDEM_PACOTE'].astype(str) + '@@' +
            df['CD_TIPO_ACOMODACAO'].astype(str) + '@@' +
            df['URG_ELE_TAX_MAT_MED_CIR_ANE_AUX'].astype(str) + '@@' +
            df['VALOR'].astype(str)
        )
        columns_to_show = ['KEY', 'CD_TIPO_REDE_ATENDIMENTO']
        #df.drop_columns(columns, axis=1, inplace=True)
        df = df[columns_to_show].copy()
        print(f'Quantidade de linhas e colunas: {df.shape}')
        df.drop_duplicates(inplace=True)
        print(f'Quantidade de linhas e colunas: {df.shape}')
        df.sort_values(by='CD_TIPO_REDE_ATENDIMENTO', inplace=True)
        df.reset_index(drop=True, inplace=True)
        
        return df
    
    # 2.1 Função para contar a quantidade de redes e listar as redes
    def number_of_networks_and_networks(self, df):
        df = (
            df.groupby('KEY')['CD_TIPO_REDE_ATENDIMENTO']
            .agg([
                ('CD_TIPO_REDE_ATENDIMENTO', lambda x: ', '.join(sorted(set(x)))),
                ('QUANTIDADE_REDES', 'nunique')
            ])
            .reset_index()
        )
        columns_to_show = ['KEY', 'QUANTIDADE_REDES', 'CD_TIPO_REDE_ATENDIMENTO']
        df = df[columns_to_show].copy()
        df.drop_duplicates(inplace=True)
        df.sort_values(by='QUANTIDADE_REDES', ascending=False, inplace=True)
        df.reset_index(drop=True, inplace=True)
        return df
    
    # 2.2 Função para desagrupar as colunas
    def ungoroup_columns(self, df):
        columns = ['TABELA', 'LOCAL_CAPA', 'CD_PROCEDIMENTO', 'CD_PROCEDIMENTO_TUSS',
            'NM_PROCEDIMENTO', 'NM_PROCEDIMENTO_TUSS', 'NU_ORDEM_PACOTE',
            'CD_TIPO_ACOMODACAO', 'URG_ELE_TAX_MAT_MED_CIR_ANE_AUX', 'VALOR',]
        
        df[columns] = df['KEY'].str.split('@@', expand=True)
        
        df.drop(columns=['KEY'], inplace=True)
        print(df.columns.tolist())
        
        df.rename(columns={'CD_TIPO_REDE_ATENDIMENTO': 'REDES'}, inplace=True)
        
        columns = ['TABELA', 'LOCAL_CAPA', 'CD_PROCEDIMENTO', 'CD_PROCEDIMENTO_TUSS',
            'NM_PROCEDIMENTO', 'NM_PROCEDIMENTO_TUSS', 'NU_ORDEM_PACOTE',
            'CD_TIPO_ACOMODACAO', 'URG_ELE_TAX_MAT_MED_CIR_ANE_AUX', 'VALOR', 'QUANTIDADE_REDES', 'REDES']
        
        df = df[columns].copy()
        print(df.shape)
        
        return df
    
    # 3. Função para salvar o DataFrame em um arquivo Excel
    def save_to_excel(self, df_file, file_path, name_capa):
        name_protocolo = name_capa
        df = df_file.copy()
        columns_to_show = ['TABELA', 'LOCAL_CAPA', 'CD_PROCEDIMENTO', 'CD_PROCEDIMENTO_TUSS',
                'NM_PROCEDIMENTO', 'NM_PROCEDIMENTO_TUSS', 'NU_ORDEM_PACOTE',
                'CD_TIPO_ACOMODACAO', 'URG_ELE_TAX_MAT_MED_CIR_ANE_AUX', 'VALOR','QUANTIDADE_REDES', 'REDES']
        
        nu_ordens = df.NU_ORDEM_PACOTE.unique()
        total = len(nu_ordens)

        for idx, nu_ordem in enumerate(nu_ordens, 1):
            df_copy = df[df.NU_ORDEM_PACOTE == nu_ordem].copy()
            sheet_file_name = 'CAPA ' + str(name_protocolo) + ' ' + str(nu_ordem) + '.xlsx'
            output_file = os.path.join(file_path, sheet_file_name)
            df_copy = df_copy[columns_to_show].copy()

            with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
                aba_geral = f'GERAL {name_capa} - {nu_ordem}'[:31]
                df_copy.to_excel(writer, sheet_name=aba_geral, index=False)

                if df_copy.URG_ELE_TAX_MAT_MED_CIR_ANE_AUX.nunique() > 1:
                    print(f'NU_ORDEM_PACOTE: {nu_ordem} possui mais de uma URG_ELE_TAX_MAT_MED_CIR_ANE_AUX')
                    for num, valor in enumerate(df_copy.URG_ELE_TAX_MAT_MED_CIR_ANE_AUX.unique()):
                        aba_nome = f'NEGOCIACAO_{num + 1}'[:31]
                        df_valor = df_copy[df_copy.URG_ELE_TAX_MAT_MED_CIR_ANE_AUX == valor]
                        df_valor.to_excel(writer, sheet_name=aba_nome, index=False)
                        
        # mensagem avisando que os arquivos foram salvos com QMensageBox
        QMessageBox.information(self.parent, "Sucesso", f"Arquivo(s) salvo(s) com sucesso na pasta: {file_path}")
        
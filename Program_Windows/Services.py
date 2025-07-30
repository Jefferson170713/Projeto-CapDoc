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

# Adiciona também o diretório atual para executáveis empacotados
if getattr(sys, 'frozen', False):
    # Executável PyInstaller
    current_dir = os.path.dirname(sys.executable)
    sys.path.append(current_dir)

from Program_Extractions_In_Sql.SqlServices import QueryServices

class CapaDocServices:
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
        
    def create_services_windows(self, packeges_by_procedures_widget):
        # Layout principal
        main_layout = QVBoxLayout()
        
        # ========== SEÇÃO Pacote pro Procediemnto ==========
        # Grupo para Status e Progresso
        group_status_progress = QGroupBox("📶 Status e Progresso")
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
        group_filters_search = QGroupBox("🔎 Filtros e Pesquisa")
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

        btn_search_capa = QPushButton("🔍 Pesquisar CAPA")
        btn_search_capa.setFixedSize(150,35)
        btn_search_capa.clicked.connect(self.search_capa)
        search_layout_capa.addWidget(btn_search_capa)
        layout_filters_search.addLayout(search_layout_capa)

        group_filters_search.setLayout(layout_filters_search)
        main_layout.addWidget(group_filters_search)
        
        # Grupo para carregar a tabela
        group_table = QGroupBox("🗓️ Tabela de Procedimentos")
        layout_table = QVBoxLayout()
        self.table_packages_by_procedures = QTableWidget()
        self.table_packages_by_procedures.setMaximumHeight(150)
        layout_table.addWidget(self.table_packages_by_procedures)
        group_table.setLayout(layout_table)
        main_layout.addWidget(group_table)
        
        # Grupo específico para o botão
        group_button = QGroupBox('💾 Processamento')
        button_layout = QHBoxLayout()
        button_layout.addStretch()  # Espaço à esquerda

        btn_process_and_save = QPushButton("📂 Processar e Salvar")
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
        
        # Detecta se está rodando como executável PyInstaller
        if getattr(sys, 'frozen', False):
            # Executável PyInstaller - tenta várias localizações
            application_path = os.path.dirname(sys.executable)
            possible_paths = [
                os.path.join(application_path, 'Arquivos', 'Oracle_jdbc', 'ojdbc8.jar'),
                os.path.join(application_path, '_internal', 'Arquivos', 'Oracle_jdbc', 'ojdbc8.jar'),
                os.path.join(sys._MEIPASS, 'Arquivos', 'Oracle_jdbc', 'ojdbc8.jar') if hasattr(sys, '_MEIPASS') else None
            ]
            path_drive = None
            for path in possible_paths:
                if path and os.path.exists(path):
                    path_drive = path
                    break
            
            if not path_drive:
                path_drive = os.path.join(application_path, 'Arquivos', 'Oracle_jdbc', 'ojdbc8.jar')
        else:
            # Desenvolvimento normal
            script_dir = os.path.dirname(os.path.abspath(__file__))
            path_drive = os.path.join(script_dir, '..', 'Arquivos', 'Oracle_jdbc', 'ojdbc8.jar')
        
        # Debug: Verificar se o arquivo JAR existe
        print(f"Caminho do JAR: {path_drive}")
        print(f"JAR existe: {os.path.exists(path_drive)}")
        
        if not os.path.exists(path_drive):
            QMessageBox.critical(self.parent, "Erro", f"Arquivo JAR não encontrado em: {path_drive}")
            return
        
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
                
                jdbc_permission = QueryServices(path_drive)
                
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
        self.df['NM_PROCEDIMENTO'] = self.treatment_serie(self.df['NM_PROCEDIMENTO'])
        self.df['NM_PROCEDIMENTO_TUSS'] = self.treatment_serie(self.df['NM_PROCEDIMENTO_TUSS'])
        self.df['CD_PROCEDIMENTO_TUSS'] = self.removing_null_values_from_numbers_int(self.df['CD_PROCEDIMENTO_TUSS'])
        self.df['CD_SERV_HONORARIO'] = self.removing_null_values_from_numbers_int(self.df['CD_SERV_HONORARIO'])

        self.df['VL_ATUAL'] = self.removing_null_values_from_numbers_float(self.df['VL_ATUAL'])
        self.df['VL_DEFLATOR_PORT_ATUAL'] = self.removing_null_values_from_numbers_float(self.df['VL_DEFLATOR_PORT_ATUAL'])
        self.df['VL_DEFLATOR_UCO_ATUAL'] = self.removing_null_values_from_numbers_float(self.df['VL_DEFLATOR_UCO_ATUAL'])
        self.df['VL_FILME_ATUAL'] = self.removing_null_values_from_numbers_float(self.df['VL_FILME_ATUAL'])
        self.df['VL_PROPOSTO'] = self.removing_null_values_from_numbers_float(self.df['VL_PROPOSTO'])
        self.df['VL_DEFLATOR'] = self.removing_null_values_from_numbers_float(self.df['VL_DEFLATOR'])
        self.df['VL_DEFLATOR_UCO'] = self.removing_null_values_from_numbers_float(self.df['VL_DEFLATOR_UCO'])
        self.df['VL_FILME_PROPOSTO'] = self.removing_null_values_from_numbers_float(self.df['VL_FILME_PROPOSTO'])

        self.df['VL_ATUAL'] = self.decimal_numbers_plus_five_places(self.df['VL_ATUAL'])
        self.df['VL_DEFLATOR_PORT_ATUAL'] = self.decimal_numbers_plus_five_places(self.df['VL_DEFLATOR_PORT_ATUAL'])
        self.df['VL_DEFLATOR_UCO_ATUAL'] = self.decimal_numbers_plus_five_places(self.df['VL_DEFLATOR_UCO_ATUAL'])
        self.df['VL_FILME_ATUAL'] = self.decimal_numbers_plus_five_places(self.df['VL_FILME_ATUAL'])
        self.df['VL_PROPOSTO'] = self.decimal_numbers_plus_five_places(self.df['VL_PROPOSTO'])
        self.df['VL_DEFLATOR'] = self.decimal_numbers_plus_five_places(self.df['VL_DEFLATOR'])
        self.df['VL_DEFLATOR_UCO'] = self.decimal_numbers_plus_five_places(self.df['VL_DEFLATOR_UCO'])
        self.df['VL_FILME_PROPOSTO'] = self.decimal_numbers_plus_five_places(self.df['VL_FILME_PROPOSTO'])

        self.df['CD_UF'] = self.treatment_serie_simple(self.df['CD_UF'])
        self.df['FL_PE'] = self.treatment_serie_simple(self.df['FL_PE'])
        self.df['NM_MUNICIPIO'] = self.treatment_serie_simple(self.df['NM_MUNICIPIO'])
        self.df['CD_MUNICIPIO'] = self.removing_null_values_from_numbers_int(self.df['CD_MUNICIPIO'])
        self.df['CD_LOCAL'] = self.removing_null_values_from_numbers_int(self.df['CD_LOCAL'])
        self.df['CC'] = self.treatment_serie_simple(self.df['CC'])
        self.df['WEB'] = self.treatment_serie_simple(self.df['WEB'])
        
        
    # 1.1 Function to treat a pandas Series   
    def treatment_serie(self, serie):
        return serie.astype(str).fillna('-').str.upper().str.strip().replace(';', ': ', regex=True)
    
    # 1.3 Function to treat a pandas Series without uppercasing
    def treatment_serie_simple(self, serie):
        return serie.fillna('-')
    
    # 1.4 Function to remove null values and convert to int
    def removing_null_values_from_numbers_int(self, serie):
        return serie.fillna(0).astype(int)
    
    # 1.5 Function to remove null values and convert to float
    def removing_null_values_from_numbers_float(self, serie):
        return serie.fillna(0.0).astype(float)
    
    def decimal_numbers_plus_five_places(self, serie):
        return serie.astype(float).map(lambda x: '{:.5f}'.format(x).replace('.', ','))

    # 1.2 Função upper para as colunas do DataFrame
    def upper_columns(self, series):
        return series.str.upper()
    
    # 2. Função para criar a chave de rede
    def group_columns(self, df):
        df['KEY'] = (
        df['CD_PROTOCOLO'].astype(str) + '@@' +
        df['CD_SERV_HONORARIO'].astype(str) + '@@' +
        df['CD_PROCEDIMENTO_TUSS'].astype(str) + '@@' +
        df['CD_ANO'].astype(str) + '@@' +
        df['DT_STATUS'].astype(str) + '@@' +
        df['NM_PROCEDIMENTO'].astype(str) + '@@' +
        df['NM_PROCEDIMENTO_TUSS'].astype(str) + '@@' +
        df['VL_ATUAL'].astype(str) + '@@' +
        df['VL_DEFLATOR_PORT_ATUAL'].astype(str) + '@@' +
        df['VL_DEFLATOR_UCO_ATUAL'].astype(str) + '@@' +
        df['VL_FILME_ATUAL'].astype(str) + '@@' +
        df['VL_PROPOSTO'].astype(str) + '@@' +
        df['VL_DEFLATOR'].astype(str) + '@@' +
        df['VL_DEFLATOR_UCO'].astype(str) + '@@' +
        df['VL_FILME_PROPOSTO'].astype(str) + '@@' +
        df['CD_UF'].astype(str) + '@@' +
        df['NM_MUNICIPIO'].astype(str) + '@@' +
        df['CD_MUNICIPIO'].astype(str) + '@@' +
        df['CD_LOCAL'].astype(str) + '@@' +
        df['CC'].astype(str) + '@@' +
        df['WEB'].astype(str) + '@@' +
        df['FL_URGENCIA'].astype(str) + '@@' +
        df['FL_ELETIVA'].astype(str) + '@@' +
        df['FL_PE'].astype(str) + '@@'
        )
        columns_to_show = ['KEY', 'REDE']
        df = df[columns_to_show].copy()
        df.drop_duplicates(inplace=True)
        df.sort_values(by='REDE', inplace=True)
        df.reset_index(drop=True, inplace=True)
        
        return df
    
    # 2.1 Função para contar a quantidade de redes e listar as redes
    def number_of_networks_and_networks(self, df):
        df = (
        df.groupby('KEY')['REDE']
        .agg([
            ('REDE', lambda x: ', '.join(sorted(set(x)))),
            ('QUANTIDADE_REDES', 'nunique')
        ])
        .reset_index()
        )
        columns_to_show = ['KEY', 'QUANTIDADE_REDES', 'REDE']
        df = df[columns_to_show].copy()
        df.drop_duplicates(inplace=True)
        df.sort_values(by='QUANTIDADE_REDES', ascending=False, inplace=True)
        df.reset_index(drop=True, inplace=True)
        return df
    
    # 2.2 Função para desagrupar as colunas
    def ungoroup_columns(self, df):
        columns = ['CD_PROTOCOLO', 'CD_SERV_HONORARIO', 'CD_PROCEDIMENTO_TUSS', 'CD_ANO', 'DT_STATUS', 'NM_PROCEDIMENTO', 'NM_PROCEDIMENTO_TUSS', 'VL_ATUAL', 'VL_DEFLATOR_PORT_ATUAL', 'VL_DEFLATOR_UCO_ATUAL', 'VL_FILME_ATUAL', 'VL_PROPOSTO', 'VL_DEFLATOR', 'VL_DEFLATOR_UCO', 'VL_FILME_PROPOSTO', 'CD_UF', 'NM_MUNICIPIO', 'CD_MUNICIPIO', 'CD_LOCAL', 'CC', 'WEB', 'FL_URGENCIA', 'FL_ELETIVA', 'FL_PE']
    
        # PRIMEIRO: fazer o split
        df[columns] = df['KEY'].str.split('@@', expand=True).iloc[:, :24]

        # DEPOIS: dropar a KEY
        df.drop(columns=['KEY'], inplace=True)
        
        df.rename(columns={'REDE': 'REDES'}, inplace=True)
        
        columns = ['CD_PROTOCOLO', 'CD_SERV_HONORARIO', 'CD_PROCEDIMENTO_TUSS', 'CD_ANO', 'DT_STATUS', 'NM_PROCEDIMENTO', 'NM_PROCEDIMENTO_TUSS', 'VL_ATUAL', 'VL_DEFLATOR_PORT_ATUAL', 'VL_DEFLATOR_UCO_ATUAL', 'VL_FILME_ATUAL', 'VL_PROPOSTO', 'VL_DEFLATOR', 'VL_DEFLATOR_UCO', 'VL_FILME_PROPOSTO', 'CD_UF', 'NM_MUNICIPIO', 'CD_MUNICIPIO', 'CD_LOCAL', 'CC', 'WEB', 'FL_URGENCIA', 'FL_ELETIVA', 'FL_PE', 'QUANTIDADE_REDES', 'REDES']
        df = df[columns].copy()
        
        return df
    
    # 3. Função para salvar o DataFrame em um arquivo Excel
    def save_to_excel(self, df_file, file_path, name_capa):
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        
        file_name = f"{name_capa}_{self.get_current_date()}.xlsx"
        full_path = os.path.join(file_path, file_name)
        
        try:
            df_file.to_excel(full_path, index=False, engine='openpyxl')
            QMessageBox.information(self.parent, "Sucesso", f"Arquivo salvo com sucesso em: {full_path}")
        except Exception as e:
            QMessageBox.critical(self.parent, "Erro", f"Erro ao salvar o arquivo: {str(e)}")
        
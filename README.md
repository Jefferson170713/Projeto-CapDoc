# CapaDoc 🏥

Sistema integrado de extração e processamento de dados médicos com interface PyQt5 para análise de procedimentos e serviços de saúde.

## 📋 Descrição

O CapaDoc é uma aplicação desktop avançada desenvolvida em Python que oferece duas funcionalidades principais para análise de dados médicos:

### 📦 **Módulo Pacotes Por Procedimentos**

- 🔍 Pesquisa de dados de procedimentos médicos por CAPA
- 🏥 Filtros por operadoras (HAPVIDA, CCG, CLINIPAM, NDI MINAS, NDI SAÚDE)
- 📊 Visualização e análise de procedimentos TUSS
- 💰 Análise de valores (atuais, propostos, deflator, UCO, filme)
- 📍 Dados geográficos (UF, município, local)
- 🔗 Agrupamento por redes credenciadas

### 🔧 **Módulo Serviços**

- 🎯 Análise específica de dados de serviços médicos
- � Processamento avançado com agrupamento por chaves compostas
- 🌐 Contagem e listagem de redes por procedimento
- 📋 Tratamento especializado de dados de honorários
- 🔄 Transformação e desagrupamento de informações

## 🚀 Funcionalidades Principais

### 🖥️ **Interface e Usabilidade**

- **Interface Gráfica Moderna**: Desenvolvida com PyQt5 e símbolos Unicode (📶 📎 🗓️ 💾)
- **Navegação por Abas**: Interface tabular para alternar entre módulos
- **Pesquisa Dinâmica**: Campo de busca em tempo real
- **Barras de Progresso**: Acompanhamento visual do processamento
- **Tabelas Interativas**: Visualização de até 1000 registros por consulta

### 🗄️ **Conectividade e Dados**

- **Conexão Oracle JDBC**: Integração robusta com banco de dados Oracle
- **Consultas Otimizadas**: Processamento em chunks para grandes volumes
- **Múltiplas Operadoras**: Suporte para 5 operadoras de saúde
- **Tratamento de Dados**: Limpeza automática e formatação de valores

### 📊 **Processamento Avançado**

- **Agrupamento Inteligente**: Criação de chaves compostas para análise
- **Contagem de Redes**: Quantificação automática de redes por procedimento
- **Formatação Brasileira**: Valores monetários em formato local (R$)
- **Tratamento de Nulos**: Substituição automática de valores vazios

### 💾 **Exportação e Relatórios**

- **Excel Automatizado**: Geração de planilhas organizadas
- **Nomenclatura Inteligente**: Arquivos nomeados com data e CAPA
- **Estrutura Padronizada**: Colunas organizadas por relevância
- **Backup Automático**: Criação de diretórios quando necessário

## 🎯 O que o Programa Faz Especificamente

### 📦 **Módulo Pacotes Por Procedimentos - Detalhado**

**🎯 Objetivo**: Analisar procedimentos médicos por CAPA com foco em valores e geografia.

**📊 Dados Processados**:

- **📋 Procedimentos TUSS**: Códigos e nomes de procedimentos
- **💰 Análise Financeira**: Valores atuais vs propostos
- **🏥 Informações Médicas**: Protocolos, serviços, honorários
- **📍 Dados Geográficos**: UF, municípios, locais de atendimento
- **🔧 Configurações**: Urgência, eletiva, PE (Pronto Atendimento)

**🔄 Fluxo de Trabalho**:

1. **Entrada**: CAPA + Operadoras selecionadas
2. **Consulta**: Busca dados Oracle com filtros
3. **Visualização**: Exibe até 1000 registros em tabela
4. **Processamento**: Trata dados, formata valores, organiza informações
5. **Saída**: Arquivo Excel com análise completa

### 🔧 **Módulo Serviços - Detalhado**

**🎯 Objetivo**: Análise avançada de serviços médicos com agrupamento por redes.

**📊 Dados Processados**:

- **🔗 Chave Composta**: Combinação de 24 campos únicos
- **🌐 Análise de Redes**: Quantificação e listagem de redes por procedimento
- **💰 Honorários Médicos**: Análise especializada de valores de serviços
- **📈 Agrupamento Inteligente**: Consolidação de dados por procedimento
- **🔄 Transformação**: Reorganização de dados para análise

**🧮 Processamento Especializado**:

1. **Criação de Chave**: Concatena 24 campos com separador `@@`
   ```
   CD_PROTOCOLO@@CD_SERV_HONORARIO@@CD_PROCEDIMENTO_TUSS@@...
   ```
2. **Agrupamento por Redes**:
   - Conta quantas redes únicas atendem cada procedimento
   - Lista todas as redes separadas por vírgula
3. **Desagrupamento**:
   - Separa a chave composta novamente em colunas
   - Adiciona colunas `QUANTIDADE_REDES` e `REDES`
4. **Ordenação**: Organiza por quantidade de redes (mais redes primeiro)

**📋 Resultado Final**:

- Arquivo Excel com procedimentos ordenados por quantidade de redes
- Cada linha mostra um procedimento único com todas as redes que o atendem
- Facilita análise de cobertura e disponibilidade de serviços

### 🔍 **Diferenças Principais Entre os Módulos**:

| Aspecto             | 📦 Packages by Procedures            | 🔧 Services                            |
| ------------------- | ------------------------------------ | -------------------------------------- |
| **Foco**            | Análise de procedimentos e valores   | Análise de redes e serviços            |
| **Processamento**   | Tratamento direto dos dados          | Agrupamento por chave composta         |
| **Saída Principal** | Procedimentos com valores formatados | Procedimentos com contagem de redes    |
| **Uso Ideal**       | Análise financeira e geográfica      | Análise de cobertura e disponibilidade |
| **Complexidade**    | Simples e direto                     | Avançado com múltiplas transformações  |

## 🛠️ Tecnologias Utilizadas

### 🐍 **Backend e Processamento**

- **Python 3.12+** - Linguagem principal
- **pandas 2.0+** - Manipulação e análise de dados
- **numpy** - Operações numéricas otimizadas
- **jaydebeapi** - Conexão JDBC com Oracle
- **JPype1 1.5.2** - Bridge Java-Python (versão específica para compatibilidade)

### 🖥️ **Interface e UX**

- **PyQt5** - Framework de interface gráfica
- **QTableWidget** - Tabelas interativas
- **QProgressBar** - Barras de progresso
- **Unicode Symbols** - Ícones e símbolos modernos (📶 🔎 🗓️ 💾 📂)

### 📊 **Dados e Relatórios**

- **openpyxl** - Geração e manipulação de arquivos Excel
- **locale** - Formatação de números em padrão brasileiro
- **datetime** - Manipulação de datas e timestamps

### 🔧 **Build e Deploy**

- **PyInstaller 6.14.2** - Compilação para executável Windows
- **Oracle JDBC Driver** - ojdbc8.jar para conectividade

## 📦 Instalação

### Requisitos

- Python 3.12 ou superior
- Oracle JDBC Driver (ojdbc8.jar)

### Configuração do Ambiente

1. Clone o repositório:

```bash
git clone https://github.com/Jefferson170713/Projeto-CapDoc.git
cd Projeto-CapDoc
```

2. Crie um ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure o driver Oracle:
   - Coloque o arquivo `ojdbc8.jar` em `Arquivos/Oracle_jdbc/`

## 🎯 Como Usar

### 🖥️ **Interface Principal**

1. **Inicie a aplicação**:

   ```bash
   python CapaDoc.py
   ```

2. **Navegue pelas abas**:
   - **📦 Packages by Procedures**: Análise de procedimentos médicos
   - **🔧 Services**: Análise de serviços e honorários

### 📦 **Módulo Packages by Procedures**

1. **Selecione as operadoras**:

   - ✅ HAPVIDA
   - ✅ CCG
   - ✅ CLINIPAM
   - ✅ NDI MINAS
   - ✅ NDI SAÚDE

2. **Digite a CAPA** no campo de pesquisa

3. **Clique em "🔍 Pesquisar CAPA"**

   - Os dados aparecerão na tabela (máximo 1000 registros)
   - Status mostrará quantidade de linhas carregadas

4. **Processe e salve**:
   - Clique em "📂 Processar e Salvar"
   - Escolha a pasta de destino
   - Arquivo Excel será gerado com nome: `{CAPA}_{data}.xlsx`

### 🔧 **Módulo Services**

1. **Funcionalidade similar** ao módulo anterior
2. **Processamento especializado**:
   - Agrupamento por chaves compostas (24 campos)
   - Contagem automática de redes
   - Listagem de redes por procedimento
   - Formatação otimizada para análise de serviços

### 🔧 **Compilação para Executável**

```bash
# Ative o ambiente virtual
venv\Scripts\activate

# Compile usando PyInstaller
pyinstaller --noconfirm CapaDoc.spec

# Copie os arquivos necessários
.\copy_files.bat
```

### 💻 **Executável Standalone**

1. **Execute** `CapaDoc.exe` da pasta `dist/`
2. **Verifique** se a pasta `Arquivos/` está no mesmo diretório
3. **Use normalmente** - todas as funcionalidades disponíveis

## 📁 Estrutura do Projeto

```
CapaDoc/
├── 📄 CapaDoc.py                           # 🚀 Arquivo principal com interface de abas
├── 📁 Program_Windows/
│   ├── PackagesByProcedures.py            # 📦 Interface para análise de procedimentos
│   └── Services.py                        # 🔧 Interface para análise de serviços
├── 📁 Program_Extractions_In_Sql/
│   ├── SqlPackageByProcedures.py          # 🗄️ Conexão Oracle para procedimentos
│   └── SqlServices.py                     # 🗄️ Conexão Oracle para serviços
├── 📁 Arquivos/
│   ├── 📁 logo/
│   │   └── logo.ico                       # 🎨 Ícone da aplicação
│   └── 📁 Oracle_jdbc/
│       ├── ojdbc8.jar                     # ☕ Driver JDBC Oracle
│       ├── jdbc_permission_package_by_procedures.py  # 🔑 Credenciais procedimentos
│       └── jdbc_permission_services.py    # 🔑 Credenciais serviços
├── 📁 dist/                               # 📦 Executável compilado
│   ├── CapaDoc.exe                        # 🖥️ Aplicação executável
│   └── Arquivos/                          # 📂 Dependências copiadas
├── 🔧 CapaDoc.spec                        # ⚙️ Configuração PyInstaller
├── 🔧 build_app.bat                       # 🛠️ Script de compilação
├── 🔧 copy_files.bat                      # 📋 Script de cópia de arquivos
├── 📋 requirements.txt                     # 📦 Dependências Python
├── 📜 LICENSE                             # ⚖️ Licença MIT
└── 📖 README.md                           # 📚 Este arquivo
```

### 🧩 **Arquitetura dos Módulos**

#### 📦 **PackagesByProcedures**

```
Funcionalidades:
├── 🔍 Pesquisa por CAPA
├── 🏥 Filtro por operadoras
├── 📊 Visualização tabular
├── 💰 Análise de valores (atual/proposto)
├── 📍 Dados geográficos
└── 💾 Exportação Excel
```

#### 🔧 **Services**

```
Funcionalidades:
├── 🎯 Análise de serviços médicos
├── 🔗 Agrupamento por chave composta
├── 🌐 Contagem de redes
├── 📈 Processamento de honorários
└── 📋 Transformação de dados
```

## 🔧 Configuração e Personalização

### 🗄️ **Configuração do Banco Oracle**

#### **Para Procedimentos**:

Edite: `Arquivos/Oracle_jdbc/jdbc_permission_package_by_procedures.py`

```python
def set_credentials(self):
    return "usuario", "senha", "oracle.jdbc.driver.OracleDriver", "jdbc:oracle:thin:@host:porta:sid"

def get_query_package_by_procedure(self, capa, list_empresa):
    # Sua consulta SQL personalizada
```

#### **Para Serviços**:

Edite: `Arquivos/Oracle_jdbc/jdbc_permission_services.py`

```python
def set_credentials(self):
    return "usuario", "senha", "oracle.jdbc.driver.OracleDriver", "jdbc:oracle:thin:@host:porta:sid"

def get_query_package_by_procedure(self, capa, list_empresa):
    # Sua consulta SQL personalizada
```

### 🎨 **Personalização da Interface**

#### **Símbolos Unicode Utilizados**:

- 📶 Status e Progresso
- 🔎 Filtros e Pesquisa
- 🗓️ Tabela de Dados
- 💾 Processamento
- 📂 Salvar Arquivos
- 🔄 Limpar Status

#### **Modificar Interface**:

- **PackagesByProcedures**: `Program_Windows/PackagesByProcedures.py`
- **Services**: `Program_Windows/Services.py`
- **Ícones**: Substitua `Arquivos/logo/logo.ico`

### ⚙️ **Configurações Avançadas**

#### **Tamanho de Chunk para Consultas**:

```python
# Em SqlPackageByProcedures.py e SqlServices.py
def fetch_data(self, chunk_size=50000, ...):  # Ajuste conforme necessário
```

#### **Limite de Registros na Tabela**:

```python
# Em PackagesByProcedures.py e Services.py
if self.df.shape[0] < 1000:  # Altere o limite se necessário
```

#### **Formato de Data nos Arquivos**:

```python
def get_current_date(self):
    return time.strftime("%d_%m_%Y")  # Personalize o formato
```

## 🤝 Contribuição

Contribuições são muito bem-vindas! Siga estas etapas:

### � **Getting Started**

1. **Fork** o projeto no GitHub
2. **Clone** seu fork:
   ```bash
   git clone https://github.com/SEU_USUARIO/Projeto-CapDoc.git
   ```
3. **Crie um ambiente virtual**:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

### 🔧 **Desenvolvimento**

1. **Crie uma branch** para sua feature:
   ```bash
   git checkout -b feature/NovaFuncionalidade
   ```
2. **Faça suas modificações**
3. **Teste localmente**:
   ```bash
   python CapaDoc.py
   ```
4. **Compile e teste** o executável:
   ```bash
   pyinstaller --noconfirm CapaDoc.spec
   .\copy_files.bat
   ```

### 📝 **Padrões de Código**

- **Docstrings**: Documente todas as funções
- **Type Hints**: Use sempre que possível
- **PEP 8**: Siga os padrões Python
- **Comentários**: Explique lógicas complexas
- **Unicode**: Mantenha símbolos na interface

### 🔄 **Submissão**

1. **Commit** suas mudanças:
   ```bash
   git commit -m "✨ feat: Adiciona nova funcionalidade X"
   ```
2. **Push** para sua branch:
   ```bash
   git push origin feature/NovaFuncionalidade
   ```
3. **Abra um Pull Request** detalhado

### 🎯 **Tipos de Contribuição**

- 🐛 **Bug fixes**
- ✨ **Novas funcionalidades**
- 📚 **Documentação**
- 🎨 **Melhorias de UI/UX**
- ⚡ **Otimizações de performance**
- 🧪 **Testes**

## 🐛 Relatando Problemas

Se encontrar algum problema, por favor:

1. Verifique se não é um problema conhecido nas [Issues](https://github.com/Jefferson170713/Projeto-CapDoc/issues)
2. Crie uma nova issue com:
   - Descrição detalhada do problema
   - Passos para reproduzir
   - Sistema operacional e versão do Python
   - Logs de erro (se houver)

## 📝 Changelog

### 🔄 **v2.0.0** (2025-07-30) - Versão Atual

- ✨ **NEW**: Módulo Services com análise avançada de serviços médicos
- ✨ **NEW**: Interface de abas para navegação entre módulos
- ✨ **NEW**: Agrupamento por chaves compostas (24 campos)
- ✨ **NEW**: Contagem automática de redes por procedimento
- 🔧 **IMPROVED**: Compilação PyInstaller com ambos os módulos
- 🔧 **IMPROVED**: Estrutura modular mais organizada
- 📚 **DOCS**: README completo com fluxos de dados detalhados

### 🎉 **v1.0.0** (2025-07-28) - Versão Inicial

- ✨ Interface PyQt5 com símbolos Unicode (📶 🔎 🗓️ 💾)
- 🔗 Conexão Oracle via JDBC robusta
- 📊 Processamento de dados com pandas
- 💾 Exportação para Excel automatizada
- 📦 Compilação para executável Windows
- 🏥 Suporte para 5 operadoras de saúde
- 🔍 Pesquisa por CAPA com filtros
- 📋 Tratamento automático de dados

### 🔜 **Roadmap Futuro**

- 📈 **v2.1.0**: Dashboard com gráficos interativos
- 🌐 **v2.2.0**: Exportação para múltiplos formatos (PDF, CSV)
- 🔔 **v2.3.0**: Sistema de notificações e alertas
- 🤖 **v3.0.0**: Análise preditiva e Machine Learning

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Jefferson Almeida**

- GitHub: [@Jefferson170713](https://github.com/Jefferson170713)
- Email: jefferson.almeia05@aluno.ifce.edu.br

## 🙏 Agradecimentos

- Comunidade Python
- Desenvolvedores das bibliotecas utilizadas
- IFCE - Instituto Federal do Ceará

---

⭐ Se este projeto foi útil para você, considere dar uma estrela!

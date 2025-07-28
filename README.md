# CapaDoc

Sistema de extração e processamento de dados de procedimentos médicos com interface PyQt5.

## 📋 Descrição

O CapaDoc é uma aplicação desktop desenvolvida em Python que permite:

- 🔍 Pesquisa de dados de procedimentos médicos por CAPA
- 🏥 Filtros por operadoras (HAPVIDA, CCG, CLINIPAM, NDI MINAS, NDI SAÚDE)
- 📊 Visualização de dados em tabela
- 💾 Processamento e exportação para Excel
- 🔗 Conexão com banco de dados Oracle

## 🚀 Funcionalidades

- **Interface Gráfica**: Interface amigável desenvolvida com PyQt5
- **Conexão Oracle**: Integração com banco de dados Oracle via JDBC
- **Processamento de Dados**: Tratamento e agrupamento de dados com pandas
- **Exportação**: Geração de arquivos Excel organizados por procedimento
- **Executável**: Pode ser compilado em executável independente com PyInstaller

## 🛠️ Tecnologias Utilizadas

- **Python 3.12+**
- **PyQt5** - Interface gráfica
- **pandas** - Manipulação de dados
- **jaydebeapi** - Conexão JDBC
- **JPype1** - Bridge Java-Python
- **openpyxl** - Geração de arquivos Excel
- **PyInstaller** - Compilação para executável

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

### Modo Desenvolvimento

```bash
python CapaDoc.py
```

### Compilar Executável

```bash
# Usando o script batch
.\build_app.bat

# Ou usando PyInstaller diretamente
pyinstaller --noconfirm CapaDoc.spec
```

### Usar o Executável

1. Copie a pasta `Arquivos` para o mesmo diretório do executável
2. Execute `CapaDoc.exe`

## 📁 Estrutura do Projeto

```
CapaDoc/
├── CapaDoc.py                          # Arquivo principal
├── Program_Windows/
│   └── PackagesByProcedures.py        # Interface PyQt5
├── Program_Extractions_In_Sql/
│   ├── SqlPackageByProcedures.py      # Conexão com banco
│   └── SqlServices.py                 # Serviços de dados
├── Arquivos/
│   ├── logo/                          # Ícones da aplicação
│   └── Oracle_jdbc/                   # Driver JDBC
├── requirements.txt                    # Dependências
├── LICENSE                            # Licença MIT
└── README.md                          # Este arquivo
```

## 🔧 Configuração

### Credenciais do Banco

Configure suas credenciais em:
- `Arquivos/Oracle_jdbc/jdbc_permission_package_by_procedures.py`

### Personalizações

- **Interface**: Modifique `Program_Windows/PackagesByProcedures.py`
- **Consultas SQL**: Edite `Program_Extractions_In_Sql/`
- **Ícones**: Substitua arquivos em `Arquivos/logo/`

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 🐛 Relatando Problemas

Se encontrar algum problema, por favor:

1. Verifique se não é um problema conhecido nas [Issues](https://github.com/Jefferson170713/Projeto-CapDoc/issues)
2. Crie uma nova issue com:
   - Descrição detalhada do problema
   - Passos para reproduzir
   - Sistema operacional e versão do Python
   - Logs de erro (se houver)

## 📝 Changelog

### v1.0.0 (2025-07-28)
- ✨ Interface PyQt5 com símbolos Unicode
- 🔗 Conexão Oracle via JDBC
- 📊 Processamento de dados com pandas
- 💾 Exportação para Excel
- 📦 Compilação para executável

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

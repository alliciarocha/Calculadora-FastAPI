## Calculadora Utilizando **FastAPI** 🧮🚀
Uma **calculadora** simples implementada em Python utilizando o framework **FastAPI** para as operações básicas.

## 🔢 Operações 
- Adição 
- Subtração 
- Multiplicação 
- Divisão 
- Expotenciação 
- Potenciação  

## ⚙️ Requisitos
- 🐍 **Python 3.9** ou superior 
- 📦 Dependências listadas no arquivo `requirements.txt`:
  - `fastapi==0.95.2` 
  - `pydantic==1.10.7` 
  - `uvicorn==0.22.0` 
  
## 📥 Instalação 
1. Clone o repositório:
   ```bash
   git clone https://github.com/your-username/calculadora-fastapi.git
   cd calculadora-fastapi
   ```
2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
## ▶️ Como Executar 
1. Inicie o servidor FastAPI usando o Uvicorn:
   ```bash
   uvicorn app.main:app --reload
   ```

2. Abra o navegador e navegue para:
   ```
   http://127.0.0.1:8000/docs
   ```
   Isso abrirá a documentação interativa da API.

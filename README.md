# API-test
- Exemplo simples que demonstra o uso da biblioteca pytest do python utilizada para realizar testes em uma API
- Ambiente utilizado:
     - WIndows
## Requisitos
### 1 - Ambiente virtual
```bash
    python -m venv venv
    venv/Scripts/activate.ps1
```
- Obs: activate.ps1 para o terminal powershell. Em outros terminais pode funcionar utilizando o activate.bat

### 2 - Instalação de dependências
```bash
    pip install -r requirements.txt
```
### 3 - Execução

```bash
    py main.py
```

#### 3.1 - Execução dos testes
``` bash
    cd tests
    pytest
```

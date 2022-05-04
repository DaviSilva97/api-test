# API-test
- Exemplo simples que demonstra o uso da biblioteca pytest do python utilizada para realizar testes em uma API
- Ambiente utilizado:
     - WIndows
## Requisitos
### 1 - Ambiente virtual
Windows via powershell:
```bash
    python -m venv .venv
    .venv/Scripts/activate.ps1
```
Outros sistemas:
```bash
    python -m venv .venv
    source .venv/bin/activate
```

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

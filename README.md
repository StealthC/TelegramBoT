# Telegram Bot Python

Um simples bot escrito em Python usando a lib [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)

## Instalação
### Windows:
1. Download do Python 3 [Aqui](https://python.org/downloads)
2. Download do ZIP do Código fonte do BOT [Aqui](https://github.com/sr-pato/TelegramBoT/archive/refs/heads/main.zip)
3. Instalação dos requisitos:
```bash
pip install -r requirements.txt
```
4. Criar um arquivo `.env` (use o arquivo `.env-sample` como exemplo e coloque seu token lá)
```python
BOT_TOKEN=Token_do_BOT_Aqui
````

### Linux Debian / Ubuntu
1. Instalação dos requistos do bash:
```bash
sudo apt install python3 python3-pip git wkhtmltopdf ffmpeg
```
2. Download, Instalação e configuração do repositório:
````bash
git clone https://github.com/sr-pato/TelegramBoT
cd TelegramBoT
````
3. Editar o Token em ***bot_ofc.py***
```python
token = 'Token do BOT Aqui'
````
## Telegram Bot API
Documentação Oficial de [Telegram bot API](https://core.telegram.org/bots)

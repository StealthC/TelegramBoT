## libs nescessárias ##
import telebot
import requests
import os
import time


## Variáveis bases ##
token = 'TOKEN DO BOT AQUI'
bot = telebot.TeleBot(token, parse_mode='html')


## Comandos ##
@bot.message_handler(commands='gato')
def foto_de_gato(mensagem):
    resposta = bot.reply_to(mensagem, f'Buscando Imagem @{mensagem.from_user.username}...')
    re_gato = requests.get('https://aws.random.cat/meow').json()
    bot.send_photo(chat_id=mensagem.chat.id, reply_to_message_id=mensagem.message_id, photo=re_gato['file'], caption='Miaw🐱')
    bot.delete_message(chat_id=resposta.chat.id, message_id=resposta.message_id)

@bot.message_handler(commands='pato')
def foto_de_pato(mensagem):
    resposta = bot.reply_to(mensagem, f'Buscando Imagem @{mensagem.from_user.username}...')
    re_pato = requests.get('https://random-d.uk/api/v2/random').json()
    bot.send_photo(chat_id=mensagem.chat.id, reply_to_message_id=mensagem.message_id, photo=re_pato['url'], caption='Quack🦆')
    bot.delete_message(chat_id=resposta.chat.id, message_id=resposta.message_id)

@bot.message_handler(commands='fox')
def foto_de_raposa(mensagem):
    resposta = bot.reply_to(mensagem, f'Buscando Imagem @{mensagem.from_user.username}...')
    re_raposa = requests.get('https://randomfox.ca/floof/').json()
    re_raposa = str(re_raposa['image']).replace('\/\/', '//').replace('\/', '/', 2)
    bot.send_photo(chat_id=mensagem.chat.id, reply_to_message_id=mensagem.message_id, photo=re_raposa, caption='Raposinha🦊')
    bot.delete_message(chat_id=mensagem.chat.id, message_id=resposta.message_id)

@bot.message_handler(commands='dog')
def foto_de_dog(mensagem):
    resposta = bot.reply_to(mensagem, f'Buscando Imagem @{mensagem.from_user.username}...')
    re_cachorro = requests.get('https://dog.ceo/api/breeds/image/random').json()['message']
    bot.send_photo(chat_id=mensagem.chat.id, reply_to_message_id=mensagem.message_id, photo=re_cachorro, caption='Au au🐶')
    bot.delete_message(chat_id=mensagem.chat.id, message_id=resposta.message_id)

@bot.message_handler(commands='dolar')
def cotacao_dolar(mensagem):
    re_dolar = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL').json()
    bot.reply_to(mensagem, f'''
<b>USD ➙ BRL</b>

🤑<b>Maior Valor:</b> R$ {re_dolar['USDBRL']['high']}
✅<b>Menor Valor:</b> R$ {re_dolar['USDBRL']['low']}
👌<b>Variação de Compra:</b> R$ {re_dolar['USDBRL']['varBid']}
✔️<b>Porcentagem de Variação:</b> {re_dolar['USDBRL']['pctChange']}%
💲<b>Compra:</b> R$ {re_dolar['USDBRL']['bid']}
💠<b>Venda:</b> R$ {re_dolar['USDBRL']['ask']}
🕐<b>Data:</b> {re_dolar['USDBRL']['create_date']}
''')

@bot.message_handler(commands='bitcoin')
def cotacao_bitcoin(mensagem):
    re_bitcoin = requests.get('https://economia.awesomeapi.com.br/last/BTC-BRL').json()
    bot.reply_to(mensagem, f'''
<b>Bitcoin ➙ BRL</b>

🤑<b>Maior Valor:</b> R$ {re_bitcoin['BTCBRL']['high']}
✅<b>Menor Valor:</b> R$ {re_bitcoin['BTCBRL']['low']}
👌<b>Variação de Compra:</b> R$ {re_bitcoin['BTCBRL']['varBid']}
✔️<b>Porcentagem da Variação:</b> {re_bitcoin['BTCBRL']['pctChange']}%
💲<b>Compra:</b> R$ {re_bitcoin['BTCBRL']['bid']}
💠<b>Venda:</b> R$ {re_bitcoin['BTCBRL']['ask']}
🕐<b>Data:</b> {re_bitcoin['BTCBRL']['create_date']}
''')

@bot.message_handler(commands='slp')
def cotacao_slp(mensagem):
    re_slp = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=smooth-love-potion&vs_currencies=brl').json()
    bot.reply_to(mensagem, f'''
<b>SLP ➙ BRL

💠<b>Total:</b> {str(re_slp['smooth-love-potion']['brl']).replace('.', ',')}''')

@bot.message_handler(commands='covid19')
def dados_coronavirus(mensagem):
    dados_coronavirus = requests.get('https://xx9p7hp1p7.execute-api.us-east-1.amazonaws.com/prod/PortalGeralApi').json()
    bot.reply_to(mensagem, f'''
<b>😷Tabelda de Casos Coronavírus😷</b>

➙<b>Casos Confirmados</b>
🔴Total: {dados_coronavirus['confirmados']['total']}
🆕Novos: {dados_coronavirus['confirmados']['novos']}
👌Recuperados: {dados_coronavirus['confirmados']['recuperados']}
😷Acompanhamento: {dados_coronavirus['confirmados']['acompanhamento']}

➙<b>Óbitos</b>
👻Total: {dados_coronavirus['obitos']['total']}
😥Novos: {dados_coronavirus['obitos']['novos']}
👀Letalidade: {dados_coronavirus['obitos']['letalidade']}
☠️Mortalidade: {dados_coronavirus['obitos']['mortalidade']}

➙<b>Data de Atualização:</b> {str(dados_coronavirus['dt_updated']).replace('T', ' ').replace('Z', '')}''')

@bot.message_handler(commands='linktopdf')
def link_para_pdf(mensagem):
    resposta = bot.reply_to(mensagem, '🔴Fazendo conversão...')
    link = str(mensagem.text).replace('/linktopdf','').replace(f'@{bot.get_me().username}', '').strip()
    os.system(fr"wkhtmltopdf {link} {mensagem.from_user.id}.pdf")
    bot.edit_message_text('✔️Conversão Feita com Sucesso! Enviando Documento...', resposta.chat.id, resposta.message_id)
    bot.send_document(mensagem.chat.id, data=open(f'{mensagem.from_user.id}.pdf', 'rb').read(), reply_to_message_id=mensagem.message_id, caption=f'<b>PDF Referente ao Link:</b>\n\n<code>{link}</code>', visible_file_name=f'''{mensagem.from_user.username}.pdf''')
    os.remove(f'{mensagem.from_user.id}.pdf')
    bot.delete_message(resposta.chat.id, resposta.message_id)

@bot.message_handler(commands='rm')
def remove_mensagem(mensagem):
    def verificar_adm():      
        info_membro = bot.get_chat_member(mensagem.chat.id, mensagem.from_user.id) 
        if info_membro.status == 'administrator':
            bot.delete_message(mensagem.chat.id, mensagem.reply_to_message.message_id)
            bot.delete_message(mensagem.chat.id, mensagem.message_id)
        else:
            resposta = bot.reply_to(mensagem, 'Desculpa, você não tem permissão de executar este comando😅')
            bot.delete_message(chat_id=mensagem.chat.id, message_id=mensagem.message_id)
            time.sleep(15)
            bot.delete_message(mensagem.chat.id, resposta.message_id)
    verificar_adm()


# Poder do Dono hihi
@bot.message_handler(commands='yurm')
def poder_do_dono(mensagem):
    info_membro = bot.get_chat_member(mensagem.chat.id, mensagem.from_user.id) 
    if info_membro.user.username == 'Sr_Yuu':
        bot.delete_message(chat_id=mensagem.chat.id, message_id=mensagem.reply_to_message.message_id)
        bot.delete_message(chat_id=mensagem.chat.id, message_id=mensagem.message_id)
    else:
        return 0


bot.infinity_polling(timeout=10, skip_pending=True, long_polling_timeout=20)

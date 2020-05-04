from pyrogram import Client

api_id = 314504
api_hash = '8c64c308e6f0186d495ae1e92a1c228d'
Client.terminate()
print('tetminated!')

def bot_hunta():
    with Client('bot_hunta', api_id, api_hash) as app:
        app.send_message('wateruwant', 'botbou2hunt')

def man_hunta():
    with Client('man_hunta', api_id, api_hash) as app:
        app.send_message('me', 'manbou2hunt')

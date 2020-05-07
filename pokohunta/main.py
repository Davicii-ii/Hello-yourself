from pyrogram import Client, Audio
import os

decrate = -1001280481543
api_id = 314504
api_hash = '8c64c308e6f0186d495ae1e92a1c228d'

def de_history():
    with open('pokohunta/obj/de_record.txt', 'w') as f:
        for msg in app.iter_history(decrate):
            print(msg, file=f)

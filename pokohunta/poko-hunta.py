from pyrogram import Client, Audio
import sys, pickle, os

decrate = -1001280481543
api_id = 314504
api_hash = '8c64c308e6f0186d495ae1e92a1c228d'

def save_obj(obj, name):
    try:
        with open('obj/'+ name + '.pkl', 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
    except(FileNotFoundError) as e:
        os.system("touch obj/de_history.pkl")

def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)
                    
with Client('de_crate', api_id, api_hash) as app:
    print('glitch')
    try:
        with open('pokohunta/obj/de_his.txt', 'w') as f:
            try:
                for msg in app.iter_history(decrate):
                    if msg.media:
                        print(msg, file=f)
            except(AttributeError) as e:
                print(e)
    except(FileNotFoundError) as e:
        os.system('touch pokohunta/obj/de_hist.txt')
        print('glitch2')

"""
TODO:
    *add t.me links to file 
    *update telegra.ph

"""

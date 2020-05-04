from pyrogram import Client, Audio

decrate = -1001280481543
api_id = 314504
api_hash = '8c64c308e6f0186d495ae1e92a1c228d'

def huntadata():
    with Client('de_crate', api_id, api_hash) as app:
        print('saving decrate\'s history to obj/de_his.txt')
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
            print(e)


"""
TODO:
    *add t.me links to file 
    *update telegra.ph
    *call functions outside this file. init
"""

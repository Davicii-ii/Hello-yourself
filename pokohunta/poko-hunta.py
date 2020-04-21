from pyrogram import Client, Audio
import sys, pickle, os

jugged = -1001124792940
decrate =  -1001280481543
de_dict = {}
de_list = []

def save_obj(obj, name):
    try:
        with open('obj/'+ name + '.pkl', 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
    except(FileNotFoundError) as e:
        os.system("touch obj/de_history.pkl")

def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def history_indict():
    try:
        for message in app.iter_history(decrate):
            if not message.audio:
                pass
            else:
                de_dict.update({message.audio.title : message.audio.duration})
                save_obj(de_dict, "de_history")
    except(AttributeError) as e:
        print(e)

def get_longballs():
    for n, t in de_dict.items():
        if t >= 600:
            de_list.append(n)
                    

with Client("de_crate", config_file="de_config.ini") as app:
    de_dict.update(load_obj("de_history"))
    if len(de_dict) != 0:
        print("\nnot empty\n")
        get_longballs()
        for i in de_list:
            print(i)
        print("\nFound", len(de_list), "items.")
    else:
        print("empty")
        history_indict()
        

"""
TODO:
    we want to delete clones.
    we check for clones by time & file name & compare them to decrate-history.txt
    constantly check for updates
    find the name of the file by checking length of song
    add the song to a suitable folder
    
    """

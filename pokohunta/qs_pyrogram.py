from pyrogram import Client

api_id = 314504
api_hash = "8c64c308e6f0186d495ae1e92a1c228d"

with Client("de_crate", api_id, api_hash) as app:
    app.send_message("wateruwant", "Greetings from **Pyrogram**!")

from pyrogram import Client

api_id = 0
api_hash = ""
bot_token = "6953750855:AAEvPUtTzM9IfafZQiFFqN3J66o8GZZprZc"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

app.run()
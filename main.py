from pyrogram import Client

api_id = 29221068
api_hash = "1059aa7321cb582070917e7bac492f5f"
bot_token = "6953750855:AAEvPUtTzM9IfafZQiFFqN3J66o8GZZprZc"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)
async def main():
    async with app:
        await app.send_message("me", "Hi!")

app.run()
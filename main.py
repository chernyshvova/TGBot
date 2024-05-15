from pyrogram import Client
import json
with open("api.json") as f:
    data = json.load(f)
    api_id = data["api_id"]
    api_hash = data["api_hash"]
    bot_token = data["bot_token"]

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)
async def main():
    async with app:
        await app.send_message("me", "Hi!")

app.run()
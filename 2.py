with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("Your session string is:", client.session.save())
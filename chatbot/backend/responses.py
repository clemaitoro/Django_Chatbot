def bot_response(message):
    if message == "hello".lower():
        return "Hello there human"
    elif message == "goodbye".lower():
        return "I am dead"
    else:
        return "I do not understand"
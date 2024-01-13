import shelve

def store_chat_messages(messages):
    with shelve.open('chat_messages_db') as db:
        db['messages'] = messages

def retrieve_chat_messages():
    with shelve.open('chat_messages_db') as db:
        return db.get('messages', [])

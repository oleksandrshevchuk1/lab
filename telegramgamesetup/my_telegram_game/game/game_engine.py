user_progress = {}

def set_user_progress(chat_id, node_id):
    user_progress[chat_id] = node_id

def get_user_progress(chat_id):
    return user_progress.get(chat_id, "start")
import os

file_path = "data/messages.db"

if os.path.exists(file_path):
    os.remove(file_path)
    print("messages.db deleted successfully.")
else:
    print("messages.db doesn't exist.")

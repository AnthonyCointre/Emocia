import os

file_path = "data/users.db"

if os.path.exists(file_path):
    os.remove(file_path)
    print("users.db deleted successfully.")
else:
    print("users.db doesn't exist.")

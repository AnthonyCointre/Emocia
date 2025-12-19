import os

file_path = "data/users_admin.db"

if os.path.exists(file_path):
    os.remove(file_path)
    print("users_admin.db deleted successfully.")
else:
    print("users_admin.db doesn't exist.")

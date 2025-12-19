import os

file_path = "data/appointments.db"

if os.path.exists(file_path):
    os.remove(file_path)
    print("appointments.db deleted successfully.")
else:
    print("appointments.db doesn't exist.")

from fastapi import BackgroundTasks
from datetime import datetime, timedelta
import time

# Simpan daftar pengingat
reminders = []

def add_reminder(message: str, delay: int):
    """Menambahkan pengingat dengan delay tertentu (dalam detik)"""
    trigger_time = datetime.now() + timedelta(seconds=delay)
    reminders.append((trigger_time, message))
    print(f"Reminder ditambahkan: {message}, akan muncul pada {trigger_time}")

def check_reminders():
    """Cek dan jalankan pengingat yang waktunya sudah tiba."""
    while True:
        now = datetime.now()
        for reminder in reminders[:]:  # Loop melalui salinan list
            trigger_time, message = reminder
            if now >= trigger_time:
                print(f"Reminder: {message}")
                reminders.remove(reminder)
        time.sleep(5)  # Cek setiap 5 detik

def start_reminder_checker(background_tasks: BackgroundTasks):
    """Menjalankan pengecekan pengingat di background."""
    background_tasks.add_task(check_reminders)

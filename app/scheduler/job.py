from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

# Contoh job yang dijadwalkan
def send_reminder():
    print("🔔 Mengirim pengingat absensi!")

# Tambahkan job ke scheduler
scheduler.add_job(send_reminder, "interval", hours=1)

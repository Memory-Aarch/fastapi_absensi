from fastapi import FastAPI
from app.routers.auth import auth_router
from app.routers.attendance import attendance_router
from app.routers.admin import admin_router
from app.scheduler.job import scheduler
from app.core.config import SECRET_KEY


app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(attendance_router, prefix="/attendance", tags=["Attendance"])
app.include_router(admin_router, prefix="/admin", tags=["Admin"])


# Mulai scheduler (auto reminder)
scheduler.start()

@app.get("/")
def home():
    return {"message": "Welcome to Absensi API"}

# Menjalankan server hanya jika dijalankan sebagai skrip utama
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

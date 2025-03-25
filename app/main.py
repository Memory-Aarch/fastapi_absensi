from fastapi import FastAPI
from .database import engine, Base
from .routers import user_router

# Inisialisasi database
Base.metadata.create_all(bind=engine)

# Inisialisasi aplikasi FastAPI
app = FastAPI()

# Registrasi router
app.include_router(user_router, prefix="/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI Absensi App"}

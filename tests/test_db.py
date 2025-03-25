from app.database import SessionLocal
from sqlalchemy.sql import text  # Import text() buat raw query

# Coba buat koneksi ke database
def test_db_connection():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))  # Pakai text() biar SQLAlchemy kompatibel
        print("✅ Koneksi ke database berhasil!")
    except Exception as e:
        print(f"❌ Gagal konek ke database: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    test_db_connection()

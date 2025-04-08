from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine
from models import Base, Signal
from auth.routes import router as auth_router
from signal_engine import detect_signal

app = FastAPI()

# 🧱 Création des tables si elles n'existent pas
Base.metadata.create_all(bind=engine)

# 🌐 CORS Middleware (à sécuriser en prod)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔐 Auth routes
app.include_router(auth_router, tags=["Auth"])

# ✅ Route principale
@app.get("/")
def root():
    return {"msg": "Atomic Mansa API 🚀 operational"}

# 🎯 Génération de signal
@app.get("/generate-signal/{pair}")
def generate(pair: str):
    db = SessionLocal()
    signal_data = detect_signal(pair)
    signal_data["pdf_url"] = None

    new_signal = Signal(**signal_data)
    db.add(new_signal)
    db.commit()
    db.refresh(new_signal)
    db.close()

    return {"signal": signal_data}

# 📊 Récupération des signaux
@app.get("/get-signals")
def get_signals():
    db = SessionLocal()
    signals = db.query(Signal).all()
    db.close()
    return signals

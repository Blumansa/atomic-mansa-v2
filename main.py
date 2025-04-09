from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine
from models import Base, Signal
from signal_engine import detect_signal
from auth.routes import router as auth_router

app = FastAPI()

# 🧱 Création des tables BDD
Base.metadata.create_all(bind=engine)

# 🌐 CORS (à sécuriser pour la prod)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔐 Inclusion des routes d'authentification
app.include_router(auth_router, tags=["Auth"])

# ✅ Route principale
@app.get("/")
def root():
    return {"msg": "Atomic Mansa API v2 is 🔥 LIVE 🔐"}

# 🎯 Générer un signal pour une paire
@app.get("/generate-signal/{pair}")
def generate(pair: str):
    db = SessionLocal()
    signal_data = detect_signal(pair)
    signal_data["pdf_url"] = None  # Pas de PDF pour l'instant

    new_signal = Signal(**signal_data)
    db.add(new_signal)
    db.commit()
    db.refresh(new_signal)
    db.close()
    return {"signal": signal_data}

# 📊 Liste tous les signaux existants
@app.get("/get-signals")
def get_signals():
    db = SessionLocal()
    signals = db.query(Signal).all()
    db.close()
    return signals


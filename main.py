from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine
from models import Base, Signal
from auth.routes import router as auth_router
from auth.security import get_current_user
from signal_engine import detect_signal

app = FastAPI()

# 🧱 Création des tables si pas encore présentes
Base.metadata.create_all(bind=engine)

# 🌐 Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔒 À sécuriser en prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔐 Auth routes
app.include_router(auth_router, tags=["Auth"])

# ✅ Test route
@app.get("/")
def root():
    return {"msg": "Atomic Mansa v2 API ready."}

# 🧠 Génération de signaux
@app.get("/generate-signal/{pair}")
def generate(pair: str, user=Depends(get_current_user)):
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
def get_signals(user=Depends(get_current_user)):
    db = SessionLocal()
    signals = db.query(Signal).all()
    db.close()
    return signals

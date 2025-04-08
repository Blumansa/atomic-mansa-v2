import random

def detect_signal(pair: str):
    return {
        "pair": pair,
        "entry": random.choice(["Buy Market", "Sell Limit"]),
        "sl": str(round(random.uniform(1.1000, 1.2000), 4)),
        "tp": str(round(random.uniform(1.2100, 1.3000), 4)),
        "rr": "1:2",
        "probability": "95%",
        "status": "active",
        "cot_alignment": "yes",
        "badge": "Top Signal du Moment",
        "pdf_url": None
    }

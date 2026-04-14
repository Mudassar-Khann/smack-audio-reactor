from pathlib import Path
import json
import logging


class Config:
    """
    STATIC SYSTEM CONFIG (not user config)
    """

    BASE_DIR = Path(__file__).resolve().parent

    SETTINGS_PATH = BASE_DIR / "config" / "settings.json"
    SOUNDS_PATH = BASE_DIR / "config" / "sounds.json"

    SOUNDS_DIR = BASE_DIR / "assets" / "sounds"
    LOGS_DIR = BASE_DIR / "logs"

    SAMPLE_RATE = 44100
    CHANNELS = 1
    BLOCK_SIZE = 1024

    DEBUG = True


def ensure_json(path: Path, default: dict):
    """
    Ensures file exists.
    DOES NOT act as runtime config.
    """
    if not path.exists():
        print(f"[INIT] Creating {path}")
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(default, f, indent=4)


def load_json(path: Path):
  
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


DEFAULT_SETTINGS = {
    "detector": {
        "low_threshold": 0.055,
        "high_threshold": 0.10,
        "spike_threshold": 0.045,
        "cooldown": 1.5
    }
}

DEFAULT_SOUNDS = {
    "random": {
        "soft": ["modi-ji-bkl", "anime-ahh"],
        "hard": ["yamate-kudesai", "kya-cheda-bhosdi", "ek-jhaat-bhar-ka-aadmi"]
    },
    "fixed": {
        "soft": "modi-ji-bkl",
        "hard": "yamate-kudesai"
    }
}


ensure_json(Config.SETTINGS_PATH, DEFAULT_SETTINGS)
ensure_json(Config.SOUNDS_PATH, DEFAULT_SOUNDS)



SETTINGS = load_json(Config.SETTINGS_PATH)
SOUNDS = load_json(Config.SOUNDS_PATH)



Config.LOGS_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=Config.LOGS_DIR / "app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

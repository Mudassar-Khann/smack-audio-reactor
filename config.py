from pathlib import Path
import json
import logging


class Config:

    BASE_DIR = Path(__file__).resolve().parents[1]

    SETTINGS_PATH = BASE_DIR / "config" / "settings.json"
    SOUNDS_PATH = BASE_DIR / "config" / "sounds.json"

    # assets + logs
    SOUNDS_DIR = BASE_DIR / "assets" / "sounds"
    LOGS_DIR = BASE_DIR / "logs"

    # audio system constants
    SAMPLE_RATE = 44100
    CHANNELS = 1
    BLOCK_SIZE = 1024

    DEBUG = True


def load_json_safe(path: Path, default: dict):

    if not path.exists():
        print(f"[WARN] Missing {path}, creating default...")
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(default, f, indent=4)

        return default

    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERROR] Failed to load {path}: {e}")
        return default



DEFAULT_SETTINGS = {
    "detector": {
        "low_threshold": 0.055,
        "high_threshold": 0.15,
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


SETTINGS = load_json_safe(Config.SETTINGS_PATH, DEFAULT_SETTINGS)
SOUNDS = load_json_safe(Config.SOUNDS_PATH, DEFAULT_SOUNDS)



Config.LOGS_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=Config.LOGS_DIR / "app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# smack-audio-reactor

A real-time Python system that detects physical impacts via microphone input and triggers audio responses using an event-driven architecture.

---

## Demo

[![Watch Demo](assets/demo/thumbnail.png)](https://youtube.com/shorts/ttk5EsN_Xzk?feature=share)

---

## Overview

This project implements a low-latency pipeline that converts raw microphone input into discrete impact events and reacts with audio playback.

Pipeline:

```
Microphone → Volume Estimation → Impact Detection → Event Queue → Sound Selection → Playback
```

The system is designed to be responsive, modular, and safe for real-time execution.


---

## Key Features

* Real-time audio input processing
* Impact detection using spike and threshold logic
* Classification into soft and hard events
* Event-driven architecture using queue + worker thread
* Preloaded audio playback for low latency
* Configurable behavior via JSON
* Modular separation of concerns

---

## Architecture

```
core/
  detector.py     # impact detection logic
  listener.py     # microphone input abstraction
  config.py       # configuration loading and system constants

audio/
  manager.py      # sound selection logic
  player.py       # playback engine (pygame)

config/
  settings.json   # detector configuration
  sounds.json     # sound mappings

assets/
  sounds/         # audio files
  demo/           # demo video and thumbnail

main.py           # application entry point
```

---

## System Design

The system follows a producer–consumer model:

* **Producer (audio thread)**
  Captures microphone input and emits events

* **Consumer (worker thread)**
  Processes events and performs playback

This separation ensures:

* non-blocking audio callback
* stable real-time behavior
* easier extensibility

---

## Installation

```bash
git clone https://github.com/Mudassar-Khann/smack-audio-reactor.git
cd smack-audio-reactor
```

```bash
python -m venv .venv
.venv\Scripts\activate
```

```bash
pip install sounddevice numpy pygame
```

---

## Usage

```bash
python main.py
```

Tap the laptop surface to trigger audio responses.

---

## Configuration

### settings.json

```json
{
  "detector": {
    "low_threshold": 0.055,
    "high_threshold": 0.10,
    "spike_threshold": 0.045,
    "cooldown": 1.5
  }
}
```

### sounds.json

```json
{
  "fixed": {
    "soft": "modi-ji-bkl",
    "hard": "yamate-kudesai"
  }
}
```

Configuration changes require restarting the application.

---

## Design Considerations

* **Real-time safety**
  No blocking operations in audio callback

* **Preloading**
  Audio assets are loaded once at startup

* **Decoupling**
  Input, detection, decision, and playback are isolated

* **Config-driven behavior**
  Runtime tuning without code changes

---

## Limitations

* Sensitive to environmental noise
* Fixed threshold system (no adaptive calibration)
* Discrete classification (soft/hard only)

---

## Future Work

* Continuous intensity-based detection
* Noise filtering and signal smoothing
* Adaptive threshold calibration
* Hot-reload configuration
* Lightweight UI for tuning

---

## License

MIT License

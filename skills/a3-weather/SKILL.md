---
name: a3-weather
description: "Current conditions plus today/tomorrow forecast for any location from the free Open-Meteo API. No API key, no dependencies (Python standard library only)."
version: 1.0.0
author: Dahye Hong (stellaho0511)
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [Weather, Forecast, Briefing, Open-Meteo, No-API-Key]
---

# a3-weather

Weather for briefings and quick questions, from Open-Meteo (free, no key).
Defaults to Los Angeles; set `A3_LAT` / `A3_LON` (and `A3_TIMEZONE`) to change the default location.

## Quick reference

| Need | Command |
|------|---------|
| Today + tomorrow (one short paragraph) | `python3 ${HERMES_SKILL_DIR}/scripts/weather.py` |
| Machine-readable JSON | `python3 ${HERMES_SKILL_DIR}/scripts/weather.py --json` |
| Another place (lat lon) | `python3 ${HERMES_SKILL_DIR}/scripts/weather.py 37.77 -122.42` |

## When to use
- Morning briefings: run the default command and include the first line.
- "Do I need an umbrella / jacket?": run it and answer from `rain_chance_pct` and the low temperature.
- For a city by name, look up its coordinates first (or ask), then pass `LAT LON`.

## Output
Temperatures are Fahrenheit. Rain chance is the daily maximum precipitation probability.

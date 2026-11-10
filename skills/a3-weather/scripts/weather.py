#!/usr/bin/env python3
"""
a3-weather — today's forecast from Open-Meteo (free, no API key).

Usage: weather.py [--json] [LAT LON]      defaults: Los Angeles (34.05, -118.24)
Env:   A3_LAT, A3_LON, A3_TIMEZONE (default America/Los_Angeles)

Author: Dahye Hong (CSCI 599 A3). Draft generated with Claude Fable 5.1, reviewed by me.
"""
import json
import os
import sys
import urllib.parse
import urllib.request

WMO = {0: "clear", 1: "mostly clear", 2: "partly cloudy", 3: "overcast", 45: "fog", 48: "rime fog",
       51: "light drizzle", 53: "drizzle", 55: "heavy drizzle", 61: "light rain", 63: "rain",
       65: "heavy rain", 71: "light snow", 73: "snow", 75: "heavy snow", 80: "rain showers",
       81: "rain showers", 82: "violent showers", 95: "thunderstorm", 96: "thunderstorm w/ hail",
       99: "thunderstorm w/ hail"}


def main(argv):
    as_json = "--json" in argv
    argv = [a for a in argv if a != "--json"]
    lat = float(argv[0]) if len(argv) > 1 else float(os.environ.get("A3_LAT", "34.05"))
    lon = float(argv[1]) if len(argv) > 1 else float(os.environ.get("A3_LON", "-118.24"))
    tz = os.environ.get("A3_TIMEZONE", "America/Los_Angeles")
    q = urllib.parse.urlencode({
        "latitude": lat, "longitude": lon, "timezone": tz, "forecast_days": 2,
        "temperature_unit": "fahrenheit",
        "daily": "weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max,sunrise,sunset",
        "hourly": "temperature_2m,precipitation_probability",
        "current": "temperature_2m,weather_code"})
    url = "https://api.open-meteo.com/v1/forecast?" + q
    with urllib.request.urlopen(url, timeout=15) as r:
        d = json.load(r)
    cur, day = d["current"], d["daily"]
    out = {"location": {"lat": lat, "lon": lon}, "now_f": cur["temperature_2m"],
           "now": WMO.get(cur["weather_code"], str(cur["weather_code"])),
           "today": {"high_f": day["temperature_2m_max"][0], "low_f": day["temperature_2m_min"][0],
                     "sky": WMO.get(day["weather_code"][0], str(day["weather_code"][0])),
                     "rain_chance_pct": day["precipitation_probability_max"][0],
                     "sunrise": day["sunrise"][0][-5:], "sunset": day["sunset"][0][-5:]},
           "tomorrow": {"high_f": day["temperature_2m_max"][1], "low_f": day["temperature_2m_min"][1],
                        "sky": WMO.get(day["weather_code"][1], str(day["weather_code"][1])),
                        "rain_chance_pct": day["precipitation_probability_max"][1]}}
    if as_json:
        return print(json.dumps(out, indent=1))
    t = out["today"]
    print(f"Now {out['now_f']:.0f}°F, {out['now']}. Today: {t['sky']}, high {t['high_f']:.0f}°F / low {t['low_f']:.0f}°F, "
          f"rain {t['rain_chance_pct']}%. Sunrise {t['sunrise']}, sunset {t['sunset']}.")
    m = out["tomorrow"]
    print(f"Tomorrow: {m['sky']}, {m['high_f']:.0f}/{m['low_f']:.0f}°F, rain {m['rain_chance_pct']}%.")


if __name__ == "__main__":
    main(sys.argv[1:])

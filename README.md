# hermes-a3-skills

Custom [Hermes Agent](https://hermes-agent.nousresearch.com) skills written for
CSCI 599 (Agentic AI) Assignment 3 by Dahye Hong.

| Skill | What it does | Needs |
|-------|--------------|-------|
| `a3-weather` | Current conditions + today/tomorrow forecast from Open-Meteo | nothing (no API key) |

## Install (Hermes skill tap)

```bash
hermes skills tap add stellaho0511/hermes-a3-skills
hermes skills install stellaho0511/hermes-a3-skills/a3-weather --yes
hermes skills list | grep a3-weather
```

Then ask your agent: *"What's the weather today?"*

The script uses only the Python standard library and calls
`https://api.open-meteo.com/v1/forecast`.

## License
MIT. Development was AI-assisted (Claude); see the assignment's PROCESS_LOG.

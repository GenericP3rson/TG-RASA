# TG RASA

## How to Run

### Dependencies:
```
pip install rasa
pip install pyTigerGraph
```

### To run:
- Open a box (in the example, COVID-19)
- Adjust `self.conn = tg.TigerGraphConnection` as necessary (based on the box)
- Run `rasa train` (you just have to do this once)
- In one terminal, run `rasa run actions`.
- In another terminal, run `rasa shell`.
- Interact with your bot.

# Sub Sum Problem Game

Welcome to the **Sub Sum Problem Game**, a turn-based strategy game inspired by the **Subset Sum Problem** (an NP-Complete problem in computer science). Your goal: strategically pack valuable items into a shared bag without exceeding its weight limit — and outscore your bot opponent!

---

## Game Concept

You and an AI bot are each given a random set of 4 items. Each item has a **value** and a **weight**.

On your turn, choose an item to place in the **shared bag** — but be careful! If placing the item would exceed the bag’s weight limit, you can’t play it.

The game ends when both players pass. Whoever has the **highest total item value** in the bag wins.

---

## Opponents

- **RandomBot**: selects items completely at random.
- **GreedyBot**: always plays the highest-value item it can fit into the bag.

---

## File Structure

| File                       | Description |
|----------------------------|-------------|
| `main.py`                  | Entry point. Handles menu and opponent selection. |
| `items.txt`                | Item database with name, value, and weight. |
| `bag.py`                   | Controls the bag's state and logic. |
| `bot.py`                   | Contains both `RandomBot` and `GreedyBot`. |
| `player.py`                | Handles player actions and inventory. |
| `items.py`                 | Item class used by both players and bots. |
| `game_logic.py`            | Core game loop, rules, and flow. |
| `display.py`               | Welcome text and menu interface. |
| `welcome_instructions.txt` | Introduction shown at game start. |

---

## How to Play

1. Make sure Python 3 is installed.
2. Run the game:
   ```
   bash
   python main.py
   ```
3. Choose your opponent:
   - `1` for RandomBot
   - `2` for GreedyBot
   - `3` to Exit

4. Follow the instructions to select items or pass.

---

## Example Game Flow
```
Available opponents: 

1. RandomBot
2. GreedyBot
3. Exit Game

Please make a selection: 2
Bot will go first!

1. Add item to bag
2. Check total value
3. Pass
Please make a selection: 1

Here are the items currently in your inventory...
1, Magic Pendant - Value: 130, Weight: 2
2, Iron Sword - Value: 90, Weight: 7
...
```

---

## Notes

- The bag’s weight limit is calculated as **half the combined weight** of both inventories.
- Bots do not adapt to player strategy (by design, for simplicity and NP context).
- Ties are possible.

---

## License

This game is provided for educational and personal use only. Built as an illustrative example of NP problem modeling.

---

## Author

Created by Gage Davelaar
Inspired by classic algorithmic problems and a love of game design.

from datetime import datetime

def log_game(winner, turns, ships_sunk):
    date = datetime.now().strftime("%Y-%m-%d")

    log_entry = f"[{date}]{winner} won in {turns} turns. Computer sank {ships_sunk} ship(s) \n"

    with open("battle_log.txt", "a") as file:
        file.write(log_entry)

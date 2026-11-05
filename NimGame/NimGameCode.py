# Part 1: Implementing One of the Nim Game Extensions
# Among the 4 extensions presented in the slides (Smart Second Player, Four Piles, Pile Range 1 to 5, and the Reverse Rule),
# we select the "Smart Second Player (Smart B using Alpha-Beta)" extension.
# In the original slide code, Player A was smart while Player B made random moves.
# With this extension, both players play optimally using Alpha-Beta pruning.
# --- حلقه شبیه‌سازی با دو بازیکن هوشمند (Smart A & Smart B) ---
rows = []
for game in range(100):
    piles = tuple(int(x) for x in rng.integers(1, 5, size=3))  # سه پشته تصادفی بین ۱ تا ۴
    nodes = 0
    start_value = alphabeta(piles, "A", -2, 2, "big_first")
    
    board, player, n_moves = piles, "A", 0
    
    # هر دو بازیکن اکنون هوشمند هستند و بهترین حرکت را انتخاب می‌کنند
    while sum(board) > 0:
        board = best_move(board, player)
        player = "B" if player == "A" else "A"
        n_moves += 1
        
    winner = "B" if player == "A" else "A"
    rows.append({
        "p1": piles[0], "p2": piles[1], "p3": piles[2], 
        "total": sum(piles),
        "nim_sum": piles[0] ^ piles[1] ^ piles[2], 
        "first_wins": start_value > 0,
        "moves": n_moves,
        "winner": winner
    })

df = pd.DataFrame(rows)
# Part 1: Implementing One of the Nim Game Extensions
# Among the 4 extensions presented in the slides (Smart Second Player, Four Piles, Pile Range 1 to 5, and the Reverse Rule),
# we select the "Smart Second Player (Smart B using Alpha-Beta)" extension.
# In the original slide code, Player A was smart while Player B made random moves.
# With this extension, both players play optimally using Alpha-Beta pruning.

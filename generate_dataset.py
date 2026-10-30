"""
پروژه آزمایشگاه هوش مصنوعی - گام دوم
اسکریپت شبیه‌سازی ۱۰۰۰ بازی دوز و تولید دیتاست رسمی
توسعه‌دهنده: محمدرضا سی‌سختی
"""

import os
import numpy as np
import pandas as pd
from tictactoe_env import TicTacToeEnv

def generate_games_dataset(num_games=1000, seed=42):
    rng = np.random.default_rng(seed)
    env = TicTacToeEnv()
    dataset_rows = []

    print(f"شروع شبیه‌سازی {num_games} بازی تصادفی برای استخراج دیتاست...")

    for game_id in range(1, num_games + 1):
        state = env.reset()
        step_number = 1

        while not env.done:
            legal_actions = env.get_legal_actions()
            if not legal_actions:
                break

            action = rng.choice(legal_actions)
            player = env.current_player
            board_before_move = "".join(str(val) for val in env.board)

            next_state, winner, done, _ = env.step(action)

            dataset_rows.append({
                "game_id": game_id,
                "step": step_number,
                "player": "X" if player == 1 else "O",
                "action": action,
                "board_state_before": board_before_move,
                "winner": "X" if winner == 1 else ("O" if winner == -1 else ("Draw" if winner == 0 else "In_Progress"))
            })

            step_number += 1

        # ثبت وضعیت برنده برای تمام سطرهای همان بازی پس از پایان
        final_winner = "X" if env.winner == 1 else ("O" if env.winner == -1 else "Draw")
        for row in dataset_rows[-step_number + 1:]:
            row["winner"] = final_winner

    # تبدیل به دیتافریم
    df = pd.DataFrame(dataset_rows)

    # ساخت پوشه data و ذخیره فایل
    os.makedirs("data", exist_ok=True)
    csv_path = os.path.join("data", "tictactoe_games.csv")
    df.to_csv(csv_path, index=False, encoding="utf-8")

    print(f"دیتاست با موفقیت با {len(df)} سطر در مسیر '{csv_path}' ذخیره شد.")

    # خلاصه آماری نتایج بازی‌ها
    unique_games = df.drop_duplicates(subset=["game_id"])
    summary = unique_games["winner"].value_counts(normalize=True) * 100
    print("\nخلاصه آماری ۱۰۰۰ بازی تصادفی:")
    for outcome, pct in summary.items():
        print(f" - درصد {outcome}: {pct:.1f}%")

if name == "main":
    generate_games_dataset(num_games=1000, seed=42)

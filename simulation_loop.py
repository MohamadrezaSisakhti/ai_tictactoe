import numpy as np

class TicTacToeEnv:
    # فرض بر این است که کلاس محیط این‌گونه تعریف شده است
    def init(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1  # بازیکن ۱ (مثلاً 1) و بازیکن ۲ (مثلاً -1)

    def reset(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1
        return self.board

    def get_legal_actions(self):
        # بازگرداندن مختصات خانه‌های خالی
        return np.argwhere(self.board == 0)

    def step(self, action):
        row, col = action
        if self.board[row, col] != 0:
            raise ValueError("حرکت غیرمجاز!")
        
        self.board[row, col] = self.current_player
        
        # بررسی شرایط برد یا تساوی
        winner = self.check_winner()
        done = winner is not None or len(self.get_legal_actions()) == 0
        
        # تغییر نوبت
        self.current_player *= -1
        return self.board, winner, done

    def check_winner(self):
        # بررسی سططرها، ستون‌ها و قطرها
        for i in range(3):
            if abs(sum(self.board[i, :])) == 3:
                return self.board[i, 0]
            if abs(sum(self.board[:, i])) == 3:
                return self.board[0, i]
        if abs(self.board[0, 0] + self.board[1, 1] + self.board[2, 2]) == 3:
            return self.board[1, 1]
        if abs(self.board[0, 2] + self.board[1, 1] + self.board[2, 0]) == 3:
            return self.board[1, 1]
        return None

    def render(self):
        symbols = {0: '.', 1: 'X', -1: 'O'}
        for row in self.board:
            print(" ".join([symbols[cell] for cell in row]))
        print("-" * 5)

# --- حلقه شبیه‌سازی (Simulation Loop) ---
if name == "main":
    env = TicTacToeEnv()
    state = env.reset()
    
    print("شروع بازی تستی در محیط شبیه‌سازی:")
    env.render()
    
    done = False
    while not done:
        # انتخاب حرکت تصادفی از بین حرکات مجاز برای تست
        legal_actions = env.get_legal_actions()
        if len(legal_actions) == 0:
            break
            
        random_index = np.random.choice(len(legal_actions))
        action = legal_actions[random_index]
        
        print(f"بازیکن {env.current_player} حرکت کرد به خانه: {action}")
        state, winner, done = env.step(action)
        env.render()
        
        if done:
            if winner:
                print(f"بازی تمام شد! برنده بازیکن: {'X' if winner == 1 else 'O'}")
            else:
                print("بازی مساوی شد!")

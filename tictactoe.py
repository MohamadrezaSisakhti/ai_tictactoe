class TicTacToe:
    def init(self):
        # ایجاد صفحه بازی ۳ در ۳ خالی
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def print_board(self):
        print("\n  0   1   2")
        for idx, row in enumerate(self.board):
            print(f"{idx} " + " | ".join(row))
            if idx < 2:
                print("  ---------")
        print()

    def make_move(self, row, col):
        # بررسی محدوده مجاز و خالی بودن خانه (بهبود مدیریت خطا)
        if 0 <= row < 3 and 0 <= col < 3:
            if self.board[row][col] == " ":
                self.board[row][col] = self.current_player
                return True
        return False

    def check_winner(self):
        # بررسی سطرها و ستون‌ها برای یافتن برنده
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return self.board[0][i]

        # بررسی قطرها
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]

        return None

    def is_board_full(self):
        # بررسی پر شدن کل صفحه (حالت مساوی)
        return all(cell != " " for row in self.board for cell in row)

    def switch_player(self):
        # تغییر نوبت بین بازیکنان
        self.current_player = "O" if self.current_player == "X" else "X"

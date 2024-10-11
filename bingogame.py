import tkinter as tk
import random

class BingoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ビンゴ大会！")

        self.used_numbers = set()  # 使用した番号を記録するセット
        self.current_number = tk.StringVar()  # 現在選択されている番号
        self.history = []  # 番号履歴

        #rootのサイズと位置
        width = 600
        height = 500
        xPos = 400
        yPos = 200
        root.geometry(f'{width}x{height}+{xPos}+{yPos}')
        #色
        root.config(bg="#b0c4de")

        # 現在の番号を表示するラベル
        self.number_label = tk.Label(root, textvariable=self.current_number, font=("Helvetica", 100))
        self.number_label.pack(pady=20)

        # 履歴表示用のTextウィジェット
        self.history_text = tk.Text(root, height=5, width=40, font=("Helvetica", 14))
        self.history_text.pack(pady=20)
        self.history_text.config(state=tk.DISABLED)  # 編集不可

        # ボタン
        self.draw_button = tk.Button(root, text="●", command=self.draw_number, font=("Helvetica", 20))
        self.draw_button.pack(pady=20)

    def draw_number(self):
        if len(self.used_numbers) >= 75:
            self.current_number.set("終了")
            return

        while True:
            number = random.randint(1, 75)
            if number not in self.used_numbers:
                self.used_numbers.add(number)
                self.current_number.set(number)
                self.history.append(number)
                break

        # 履歴更新
        self.update_history()

    def update_history(self):
        self.history_text.config(state=tk.NORMAL)  # 編集可能にする
        self.history_text.delete(1.0, tk.END)  # 現在の履歴を消去

        # 履歴を改行で表示
        history_display = "履歴:\n" + ", ".join(map(str, self.history))
        self.history_text.insert(tk.END, history_display)
        self.history_text.config(state=tk.DISABLED)  # 再び編集不可に設定

if __name__ == "__main__":
    root = tk.Tk()
    app = BingoApp(root)
    root.mainloop()

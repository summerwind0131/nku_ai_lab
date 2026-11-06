import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("状态空间法与小游戏合集")
root.geometry("900x600")

# 所有页面都显示在这个容器里。
content = ttk.Frame(root, padding=30)
content.pack(fill="both", expand=True)


def clear_page():
    """删除当前页面的控件，准备显示下一个页面。"""
    for widget in content.winfo_children():
        widget.destroy()


def show_game(name):
    clear_page()
    ttk.Button(content, text="← 返回菜单", command=show_menu).pack(anchor="w")
    ttk.Label(content, text=name, font=("Microsoft YaHei", 22)).pack(pady=25)

    # 目前是页面占位，后续在这里添加棋盘或水杯等游戏画面。
    board = tk.Canvas(content, background="#f3f5f7", highlightthickness=0)
    board.pack(fill="both", expand=True)
    board.create_text(120, 60, text="游戏区域", font=("Microsoft YaHei", 16))


def show_menu():
    clear_page()
    ttk.Label(
        content, text="状态空间法与小游戏合集", font=("Microsoft YaHei", 24)
    ).pack(pady=(35, 15))
    ttk.Label(content, text="选择一个游戏开始").pack(pady=(0, 25))

    for name in ("农夫过河", "水杯问题", "N 皇后", "八数码"):
        ttk.Button(
            content,
            text=name,
            width=28,
            command=lambda game=name: show_game(game),
        ).pack(pady=8, ipady=8)


if __name__ == "__main__":
    show_menu()
    root.mainloop()

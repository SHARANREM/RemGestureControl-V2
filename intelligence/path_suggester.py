import tkinter as tk
from config import settings


class PathSuggester:
    def __init__(self, parent):
        self.root = tk.Toplevel(parent)
        self.root.withdraw()

        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.attributes("-alpha", settings.PATH_SUGGEST_ALPHA)
        self.root.configure(bg=settings.PATH_SUGGEST_BG_COLOR)

        self.label = tk.Label(
            self.root,
            text="",
            font=(
                settings.PATH_SUGGEST_FONT_FAMILY,
                settings.PATH_SUGGEST_FONT_SIZE,
                settings.PATH_SUGGEST_FONT_WEIGHT
            ),
            fg=settings.PATH_SUGGEST_TEXT_COLOR,
            bg=settings.PATH_SUGGEST_BG_COLOR,
            padx=settings.PATH_SUGGEST_PAD_X,
            pady=settings.PATH_SUGGEST_PAD_Y
        )
        self.label.pack()

        self.position_window()

    def position_window(self):
        self.root.update_idletasks()

        screen_height = self.root.winfo_screenheight()

        x = settings.PATH_SUGGEST_OFFSET_X
        y = screen_height - settings.PATH_SUGGEST_OFFSET_Y

        self.root.geometry(f"+{x}+{y}")

    def update_prediction(self, gesture, confidence):
        self.root.after(0, lambda: self._safe_update(gesture, confidence))

    def _safe_update(self, gesture, confidence):
        if not gesture:
            self.root.withdraw()
            return

        self.label.config(
            text=f"✨ {gesture} ({confidence:.2f})"
        )

        self.root.deiconify()

    def hide(self):
        self.root.after(0, self.root.withdraw)
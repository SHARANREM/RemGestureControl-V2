import math
import os
import tkinter as tk
from PIL import Image, ImageTk
from config import settings


class WandOverlay:
    """
    Stable magical wand overlay.
    Draws while holding ctrl.
    Fades only after release.
    """

    def __init__(self, parent):
        self.parent = parent

        self.overlay = tk.Toplevel(parent)
        self.overlay.withdraw()
        self.overlay.overrideredirect(True)
        self.overlay.attributes("-topmost", True)

        screen_w = self.overlay.winfo_screenwidth()
        screen_h = self.overlay.winfo_screenheight()

        self.overlay.geometry(f"{screen_w}x{screen_h}+0+0")

        self.canvas = tk.Canvas(
            self.overlay,
            width=screen_w,
            height=screen_h,
            bg="black",
            highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True)

        try:
            self.overlay.wm_attributes("-transparentcolor", "black")
        except:
            pass

        asset_path = os.path.join(
            settings.BASE_DIR,
            "data",
            "assets"
        )

        self.wand_img_raw = Image.open(
            os.path.join(asset_path, "thumb.png")
        ).convert("RGBA").resize(settings.WAND_IMAGE_SIZE)

        self.points = []

        self.current_x = 0
        self.current_y = 0
        self.current_angle = 0

        self.is_active = False
        self.is_fading = False
        self.is_drawing = False   # IMPORTANT NEW FLAG

        self.photo_refs = []

        self.overlay.after(
            settings.WAND_OVERLAY_FPS,
            self.animation_loop
        )

    def start_spell(self):
        self.is_active = True
        self.is_fading = False
        self.is_drawing = True
        self.points.clear()
        self.overlay.deiconify()

    def update_position(self, x, y):
        # Ignore late callbacks after release
        if self.is_fading:
            return

        if not self.is_active:
            self.start_spell()

        self.is_drawing = True

        if self.points:
            prev_x, prev_y = self.points[-1]

            dx = x - prev_x
            dy = y - prev_y

            if abs(dx) < 2 and abs(dy) < 2:
                return

            self.current_angle = math.degrees(
                math.atan2(dy, dx)
            )

        self.current_x = x
        self.current_y = y

        self.points.append((x, y))

        if len(self.points) > 1000:
            self.points = self.points[-1000:]

    def animation_loop(self):
        if self.is_fading:
            for _ in range(settings.WAND_FADE_SPEED):
                if self.points:
                    self.points.pop(0)

            if not self.points:
                self.overlay.withdraw()
                self.is_active = False
                self.is_fading = False
                self.is_drawing = False
                self.canvas.delete("all")

        if self.is_active:
            self.render()

        self.overlay.after(
            settings.WAND_OVERLAY_FPS,
            self.animation_loop
        )

    def render(self):
        self.canvas.delete("all")
        self.photo_refs.clear()

        self.draw_trail()
        self.draw_wand()

    def draw_trail(self):
        if len(self.points) < 2:
            return

        total = len(self.points)

        ox = settings.WAND_TRAIL_OFFSET_X
        oy = settings.WAND_TRAIL_OFFSET_Y

        for i in range(1, total):
            x1, y1 = self.points[i - 1]
            x2, y2 = self.points[i]

            x1 += ox
            y1 += oy
            x2 += ox
            y2 += oy

            width = max(
                1,
                int(settings.WAND_TRAIL_WIDTH * i / total)
            )

            self.canvas.create_line(
                x1,
                y1,
                x2,
                y2,
                fill=settings.WAND_TRAIL_COLOR,
                width=width,
                smooth=True
            )

    def draw_wand(self):
        wand = self.wand_img_raw

        photo = ImageTk.PhotoImage(wand)
        self.photo_refs.append(photo)

        self.canvas.create_image(
            self.current_x,
            self.current_y,
            image=photo
        )

    def fade_out(self):
        self.is_drawing = False
        self.is_fading = True
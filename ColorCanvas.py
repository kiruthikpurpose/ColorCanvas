import tkinter as tk
from tkinter import colorchooser, ttk
import random

class DrawApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Draw on Canvas")

        self.color = "black"
        self.brush_size = 5
        self.brush_type = "round"

        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack()

        self.controls_frame = tk.Frame(root)
        self.controls_frame.pack()

        self.color_button = tk.Button(self.controls_frame, text="Select Color", command=self.choose_color)
        self.color_button.grid(row=0, column=0, padx=5)

        self.clear_button = tk.Button(self.controls_frame, text="Clear Canvas", command=self.clear_canvas)
        self.clear_button.grid(row=0, column=1, padx=5)

        self.size_label = tk.Label(self.controls_frame, text="Brush Size:")
        self.size_label.grid(row=0, column=2, padx=5)

        self.size_slider = tk.Scale(self.controls_frame, from_=1, to=50, orient=tk.HORIZONTAL)
        self.size_slider.set(self.brush_size)
        self.size_slider.grid(row=0, column=3, padx=5)

        self.type_label = tk.Label(self.controls_frame, text="Brush Type:")
        self.type_label.grid(row=0, column=4, padx=5)

        self.brush_type_combobox = ttk.Combobox(self.controls_frame, values=["round", "square", "spray"])
        self.brush_type_combobox.set(self.brush_type)
        self.brush_type_combobox.grid(row=0, column=5, padx=5)

        self.canvas.bind("<B1-Motion>", self.paint)

    def choose_color(self):
        self.color = colorchooser.askcolor(color=self.color)[1]

    def clear_canvas(self):
        self.canvas.delete("all")

    def paint(self, event):
        self.brush_size = self.size_slider.get()
        self.brush_type = self.brush_type_combobox.get()

        if self.brush_type == "round":
            self.canvas.create_oval(event.x - self.brush_size, event.y - self.brush_size,
                                    event.x + self.brush_size, event.y + self.brush_size,
                                    fill=self.color, outline=self.color)
        elif self.brush_type == "square":
            self.canvas.create_rectangle(event.x - self.brush_size, event.y - self.brush_size,
                                         event.x + self.brush_size, event.y + self.brush_size,
                                         fill=self.color, outline=self.color)
        elif self.brush_type == "spray":
            self.spray_paint(event)

    def spray_paint(self, event):
        for _ in range(30):  # Spray intensity
            x = event.x + random.randint(-self.brush_size, self.brush_size)
            y = event.y + random.randint(-self.brush_size, self.brush_size)
            self.canvas.create_oval(x, y, x + 1, y + 1, fill=self.color, outline=self.color)

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawApp(root)
    root.mainloop()

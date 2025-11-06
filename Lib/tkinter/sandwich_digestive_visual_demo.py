import tkinter as tk
from tkinter import Canvas

# Stages of digestion
stages = [
    ("Mouth", "Ingestion: The sandwich enters the mouth."),
    ("Esophagus", "The sandwich moves down the esophagus."),
    ("Stomach", "Digestion: Stomach churns the sandwich."),
    ("Small Intestine", "Further digestion and nutrients are absorbed."),
    ("Large Intestine", "Water is absorbed; waste forms."),
    ("Rectum/Anus", "Egestion: Waste exits the body."),
]

class DigestiveDemo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sandwich Digestive Journey")
        self.geometry("600x400")
        self.current_stage = 0

        # Canvas for diagram
        self.canvas = Canvas(self, width=400, height=300, bg="lightyellow")
        self.canvas.pack(side="left", padx=10, pady=10)
        
        # Text area for instructions
        self.instruction = tk.Label(self, text="", font=("Arial", 14), wraplength=180)
        self.instruction.pack(pady=20)

        # Next button
        self.next_btn = tk.Button(self, text="Next", command=self.next_stage, font=("Arial", 12))
        self.next_btn.pack(pady=10)
        
        self.draw_system()
        self.next_stage()

    def draw_system(self):
        # Draw basic digestive path
        self.parts = {
            "Mouth": self.canvas.create_oval(180, 15, 220, 55, fill="peach puff"),
            "Esophagus": self.canvas.create_rectangle(195, 55, 205, 120, fill="tan"),
            "Stomach": self.canvas.create_oval(140, 120, 260, 190, fill="lightcoral"),
            "Small Intestine": self.canvas.create_oval(140, 195, 260, 250, fill="lightgreen"),
            "Large Intestine": self.canvas.create_rectangle(120, 250, 280, 280, fill="wheat"),
            "Rectum/Anus": self.canvas.create_oval(180, 280, 220, 300, fill="gray"),
        }
        # Place sandwich (oval)
        self.sandwich = self.canvas.create_rectangle(185, 30, 215, 50, fill="burlywood1", tags="sandwich")
    
    def move_sandwich(self, part):
        # Move sandwich to coordinates for the current organ
        coords = {
            "Mouth": (185, 30, 215, 50),
            "Esophagus": (195, 70, 205, 90),
            "Stomach": (180, 130, 220, 170),
            "Small Intestine": (180, 210, 220, 230),
            "Large Intestine": (190, 260, 210, 275),
            "Rectum/Anus": (190, 285, 210, 295),
        }
        self.canvas.coords(self.sandwich, *coords[part])

    def next_stage(self):
        if self.current_stage < len(stages):
            part, text = stages[self.current_stage]
            self.move_sandwich(part)
            self.instruction.config(text=text)
            self.current_stage += 1
            if self.current_stage == len(stages):
                self.next_btn.config(text="Restart")
        else:
            self.current_stage = 0
            self.next_btn.config(text="Next")
            self.next_stage()

if __name__ == "__main__":
    app = DigestiveDemo()
    app.mainloop()

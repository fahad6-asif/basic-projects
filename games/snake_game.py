import tkinter as tk
import random

class SnakeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Snake Game")

        self.size = 20
        self.width = 400
        self.height = 400

        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height, bg="black")
        self.canvas.pack()

        self.snake = [(200, 200), (180, 200), (160, 200)]
        self.food = self.spawn_food()
        self.direction = "Right"
        self.running = True

        self.window.bind("<Up>", lambda e: self.change_dir("Up"))
        self.window.bind("<Down>", lambda e: self.change_dir("Down"))
        self.window.bind("<Left>", lambda e: self.change_dir("Left"))
        self.window.bind("<Right>", lambda e: self.change_dir("Right"))

        self.update()
        self.window.mainloop()

    def spawn_food(self):
        x = random.randrange(0, self.width, self.size)
        y = random.randrange(0, self.height, self.size)
        return (x, y)

    def change_dir(self, d):
        opposites = {"Up":"Down", "Down":"Up", "Left":"Right", "Right":"Left"}
        if d != opposites[self.direction]:
            self.direction = d

    def move(self):
        x, y = self.snake[0]
        if self.direction == "Up":
            y -= self.size
        elif self.direction == "Down":
            y += self.size
        elif self.direction == "Left":
            x -= self.size
        elif self.direction == "Right":
            x += self.size
        new_head = (x, y)

        if new_head in self.snake or x < 0 or y < 0 or x >= self.width or y >= self.height:
            self.running = False
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.spawn_food()
        else:
            self.snake.pop()

    def draw(self):
        self.canvas.delete("all")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x+self.size, y+self.size, fill="green")
        fx, fy = self.food
        self.canvas.create_rectangle(fx, fy, fx+self.size, fy+self.size, fill="red")

    def update(self):
        if self.running:
            self.move()
            self.draw()
            self.window.after(120, self.update)
        else:
            self.canvas.create_text(200, 200, text="Game Over", fill="white", font=("Arial", 20))

SnakeGame()

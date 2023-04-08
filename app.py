import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        self.counter = 0

        # Create a button that increments the counter when clicked
        self.button = tk.Button(master, text="Click me!", command=self.increment_counter)
        self.button.pack()

        # Create a label to display the current value of the counter
        self.label = tk.Label(master, text="Counter: 0")
        self.label.pack()

    def increment_counter(self):
        # Increment the counter and update the label
        self.counter += 1
        self.label.config(text="Counter: " + str(self.counter))

# Create the main window and start the event loop
root = tk.Tk()
app = App(root)
root.mainloop()

import tkinter as tk

LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
SMALL_FONT = ("Arial", 16)
LARGE_FONT = ("Arial", 40, "bold")
DIGITS_FONT = ("Arial", 24, "bold")


class Calculator:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("357x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")
        self.total_expresion = "0"
        self.display_frame = self.create_display_frame()
        self.button_frame = self.create_button_frame()
        self.curent_expresion = "0"
        self.total_label, self.label = self.create_display_labels()
        self.digits = {
            7:(1,1),8:(1,2),9:(1,3),
            4:(2,1),5:(2,2),6:(2,3),
            1:(3,1),2:(3,2),3:(3,3),
            0:(4,2),".":(4,3)
        }

    def run(self):
        self.window.mainloop()

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg="#F5F5F5")
        frame.pack(expand=True, fill="both")
        return frame

    def create_button_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text = self.total_expresion, anchor = tk.E, bg = LIGHT_GRAY, fg = LABEL_COLOR, padx=24, font = SMALL_FONT)
        total_label.pack(expand=True, fill="both")
        label = tk.Label(self.display_frame, text = self.curent_expresion, anchor = tk.E, bg = LIGHT_GRAY, fg = LABEL_COLOR, padx=24, font = LARGE_FONT)
        label.pack(expand=True, fill="both")
        return total_label, label

    def create_digits_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.button_frame, text = str(digit), bg="#FFFFFF", fg = LABEL_COLOR,font = DIGITS_FONT,borderwidth=0)

if __name__ == "__main__":
    calc = Calculator()
    calc.run()



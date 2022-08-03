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
        self.total_expresion = ""
        self.display_frame = self.create_display_frame()
        self.button_frame = self.create_button_frame()
        self.curent_expresion = "0"
        self.total_label, self.label = self.create_display_labels()
        self.digits = {
            7:(1,1),8:(1,2),9:(1,3),
            4:(2,1),5:(2,2),6:(2,3),
            1:(3,1),2:(3,2),3:(3,3),
            0:(4,2),".":(4,1)
        }
        self.create_digits_buttons()
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.create_operator_buttons()
        self.create_clear_button()
        self.button_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.button_frame.rowconfigure(x, weight = 1)
            self.button_frame.columnconfigure(x, weight = 1)
        self.create_equal_button()


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

    def clear_labels(self):
        self.total_expresion = ""
        self.curent_expresion = "0"
        self.update_total_label()
        self.update_label()

    def evaluate(self):
        self.total_expresion += self.curent_expresion
        self.update_total_label()
        try:
            self.curent_expresion = "{:.5f}".format(eval(self.total_expresion))
            self.total_expresion = ""
        except ZeroDivisionError:
            self.curent_expresion = "ERROR"
        finally:
            self.update_label()
            self.update_total_label()

    def create_digits_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.button_frame, text = str(digit), bg="#FFFFFF", fg = LABEL_COLOR,font = DIGITS_FONT, borderwidth = 0, command = lambda x = digit: self.add_to_expression(x))
            button.grid(row = grid_value [0], column=grid_value[1], sticky=tk.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.button_frame, text=(symbol), bg="#F8FAFF", fg=LABEL_COLOR, font=DIGITS_FONT, borderwidth=0, command=lambda x = operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def create_clear_button(self):
        button = tk.Button(self.button_frame, text=("C"), bg="#F8FAFF", fg=LABEL_COLOR, font=DIGITS_FONT, borderwidth=0, command = lambda: self.clear_labels())
        button.grid(row=0, column=1, sticky=tk.NSEW, columnspan=3)

    def create_equal_button(self):
        button = tk.Button(self.button_frame, text=("="), bg="#CCEDFF", fg=LABEL_COLOR, font=DIGITS_FONT, borderwidth=0, command = lambda: self.evaluate())
        button.grid(row=4, column=3, sticky=tk.NSEW, columnspan=3)

    def update_total_label(self):
        self.total_label.config(text=self.total_expresion)


    def update_label(self):
        self.label.config(text=self.curent_expresion)

    def add_to_expression(self, value):
        if(self.curent_expresion == "0" and value != ".") or self.curent_expresion == "ERROR":
           self.curent_expresion = ""
        self.curent_expresion += str(value)
        self.update_label()

    def append_operator(self, operator):
        self.curent_expresion += operator
        self.total_expresion += self.curent_expresion
        self.curent_expresion = ""
        self.update_total_label()
        self.update_label()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()



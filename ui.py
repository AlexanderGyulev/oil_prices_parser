import tkinter as tk

class OilPriceApp:
    def __init__(self, root, basket_data):
        self.root = root
        self.basket_data = basket_data
        self.root.title("Oil Price App")
        self.root.geometry("300x130")
        self.build_ui()

    def build_ui(self):
        self.input_label = tk.Label(self.root, text="Please enter the date in the format YYYY-MM-DD:")
        self.input_label.pack(pady = 5)
        self.text_entry = tk.Entry(self.root)
        self.text_entry.pack(pady = 5 )
        self.search_button = tk.Button(self.root, text="Search", command=self.on_search)
        self.search_button.pack(pady = 5)
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady = 5)

    def on_search(self):
        entered_date = self.text_entry.get()
        price = self.basket_data.get_price(entered_date)
        if price is not None:
            self.result_label.configure(text="The price is: ${}".format(price))
        else:
            self.result_label.configure(text="The entered date doesn't exist")

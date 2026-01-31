import xml.etree.ElementTree as ET
from ui import OilPriceApp
import tkinter as tk

class BasketData:
    def __init__(self, xml_path):
        self.xml_path = xml_path
        self.prices_by_date = {}
        self._load()

    def _load(self):
        tree = ET.parse(self.xml_path)
        root = tree.getroot()

        for each in root.findall("BasketList"):
            date_str = each.attrib.get("data")
            value = each.attrib.get("val")

            if date_str is not None and value is not None:
                self.prices_by_date[date_str] = value

    def get_price(self, date_str):

        return self.prices_by_date.get(date_str)


if __name__ == "__main__":
    basket = BasketData("oil_prices.xml")
    root = tk.Tk()
    app = OilPriceApp(root, basket)
    root.mainloop()


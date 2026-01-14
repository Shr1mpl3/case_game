class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, name: str, value: float):
        self.items.append((name, value))
        self.sort_by_value()

    def sort_by_value(self):
        self.items.sort(key=lambda x: x[1], reverse=True)

    def total_value(self):
        return sum(item[1] for item in self.items)

    def show(self):
        if not self.items:
            return "Inventar ist leer."
        text = ""
        for name, value in self.items:
            text += f"- {name} ({value}€)\n"
        text += f"\nGesamtwert: {self.total_value():.2f}€"
        return text

    def sell_item(self, index: int):
        if index < 0 or index >= len(self.items):
            return None

        item = self.items.pop(index)
        return item  # (name, value)

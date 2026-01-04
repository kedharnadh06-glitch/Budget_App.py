class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:.2f}"
            items += f"{desc:<23}{amt:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    withdrawals = []
    total_spent = 0

    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += -item["amount"]
        withdrawals.append(spent)
        total_spent += spent

    percentages = [int((spent / total_spent) * 10) * 10 for spent in withdrawals]

    chart = "Percentage spent by category\n"
    for level in range(100, -1, -10):
        chart += f"{level:>3}|"
        for percent in percentages:
            chart += " o " if percent >= level else "   "
        chart += " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        chart += "     "
        for cat in categories:
            if i < len(cat.name):
                chart += cat.name[i] + "  "
            else:
                chart += "   "
        chart += "\n"

    return chart.rstrip()


# Test usage example
if __name__ == "__main__":
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")

    clothing = Category("Clothing")
    food.transfer(50, clothing)

    auto = Category("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15, "fuel")

    print(food)
    print(clothing)
    print(auto)

    print(create_spend_chart([food, clothing, auto]))

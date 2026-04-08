# 💰 BudgetTracker

A Python terminal application for managing personal finances. Track your income and expenses, view summaries by category, and visualize your spending with charts.

---

## 📋 Features

- Add income and expense transactions
- View current balance
- Import/Export transactions from JSON files
- View transaction history (all, income only, expenses only)
- Analyze spending and income by category
- Visualize expenses and income with bar charts (matplotlib)
- Input validation with error handling

---

## 🛠️ Requirements

- Python 3.x
- matplotlib

Install dependencies:
```bash
pip install matplotlib
```

---

## 🚀 How to Run

```bash
python main.py
```

---

## 📁 Project Structure

```
BudgetTracker/
│
├── main.py        # Main program and menu logic
├── tracker.py     # User and Transaction classes
├── expenses.json  # Exported expenses (auto-generated)
└── incomes.json   # Exported incomes (auto-generated)
```

---

## 🖥️ Usage

When you run the program you will be asked for your name and initial balance. Then you can:

**Main Menu:**
- `1` → Add a transaction (income or expense)
- `2` → Show current balance
- `3` → Import incomes from JSON
- `4` → Import expenses from JSON

**History Menu:**
- `1` → History of incomes
- `2` → History of expenses
- `3` → All transactions
- `4` → Expenses by category
- `5` → Incomes by category

**Export Menu:**
- `1` → Export expenses to JSON
- `2` → Export incomes to JSON
- `3` → Plot expenses by category
- `4` → Plot incomes by category

---

## 📊 Example Output

```
Hello Chris
1000.0 of money has been added to your account.
The reason is salary and the date is 08/04/2026 21:30.
You now have 1000.0 into your account
```

---

## 👨‍💻 Author

Built as a portfolio project for the Codecademy CS101 Python course.

---

## 🔮 Future Plans

- SQLite database integration
- FastAPI web app version
- Rich terminal UI
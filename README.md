# Account Balance Tracker

A Python terminal application for tracking personal income and expenses. Supports categorised transactions, JSON import/export, and bar chart visualisation.

---

## Requirements

- Python 3.10+
- matplotlib

```bash
pip install matplotlib
```

---

## Running

```bash
python main.py
```

---

## Project Structure

```
Account-Balance/
├── main.py        # CLI menu and program entry point
├── tracker.py     # User, Transaction, and InsufficientFundsError
├── expenses.json  # Auto-generated on export
└── incomes.json   # Auto-generated on export
```

---

## Usage

On startup you enter your name and starting balance. Then:

**Main menu**
- `1` Add a transaction (deposit or withdrawal)
- `2` Show current balance
- `3` Import income from JSON
- `4` Import expenses from JSON

**History menu**
- `1` Income history
- `2` Expense history
- `3` All transactions
- `4` Expenses by category
- `5` Income by category

**Export menu**
- `1` Export expenses to JSON
- `2` Export income to JSON
- `3` Plot expenses by category
- `4` Plot income by category

---

## API

### `Transaction(amount, category, date)`

| Parameter  | Type    | Description                      |
|------------|---------|----------------------------------|
| `amount`   | `float` | Monetary value                   |
| `category` | `str`   | Label, e.g. `"Salary"` or `"Rent"` |
| `date`     | `str`   | Date string, e.g. `"2026-06-01"` |

### `User(name, initial_balance)`

| Method | Description |
|--------|-------------|
| `deposit(transaction)` | Add income; returns summary string |
| `withdraw(transaction)` | Deduct expense; raises `InsufficientFundsError` if balance is insufficient |
| `get_balance()` | Returns balance summary string |
| `get_transactions()` | All transactions |
| `get_income()` | Income transactions |
| `get_expenses()` | Expense transactions |
| `get_income_by_category()` | Dict of income totals per category |
| `get_expenses_by_category()` | Dict of expense totals per category |
| `export_income(path)` | Write income to JSON file |
| `export_expenses(path)` | Write expenses to JSON file |
| `import_income(path)` | Load income from JSON file |
| `import_expenses(path)` | Load expenses from JSON file |
| `plot_income()` | Bar chart of income by category |
| `plot_expenses()` | Bar chart of expenses by category |

---

## Future Plans

- SQLite database integration
- FastAPI web app version
- Rich terminal UI

---

## Author

Built as a portfolio project for the Codecademy CS101 Python course.

---

## License

MIT

import pytest
import sys
from backend import db_helper


print("current path :",sys.path)

def test_fetch_expenses_for_date():
    data = db_helper.fetch_expenses_for_date("2024-08-15")

    assert len(data) == 1
    assert data[0]['category'] == "Shopping"
    assert data[0]['amount'] == 10

def test_invalid_date_ranges():
    expenses = db_helper.fetch_expense_summary("2099-10-09", "2099-10-20")
    assert len(expenses) == 0



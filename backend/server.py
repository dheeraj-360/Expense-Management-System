from fastapi import FastAPI, HTTPException
from datetime import date
from typing import List
from pydantic import BaseModel
from unicodedata import category

import db_helper

app = FastAPI()

class Expense(BaseModel):
    amount : float
    category : str
    notes : str

class DateRange(BaseModel):
    start_date : date
    end_date : date


@app.get("/expenses/{expense_date}", response_model= List[Expense])
def get_expense(expense_date: date):
    data = db_helper.fetch_expenses_for_date(expense_date)
    if data is None:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve expense data for date : {expense_date}")
    return data

@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date, expenses: List[Expense]):
    db_helper.delete_expense_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)
    return "Successfully updated the Expenses"

# For Analytics Tab

@app.post("/analytics/")
def get_analytics(date_range : DateRange):
    data = db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)

    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from data")



    total = sum([row["total"] for row in data])

    breakdown={}
    for row in data:
        percentage = (row["total"] / total) * 100 if total !=0 else 0
        breakdown[row["category"]] = {
            "total": row["total"]*1.0,
            "percentage": percentage,
        }

    return breakdown

# For Analytics by Months

@app.get("/analytics/months")
def get_analytics_months():
    data = db_helper.fetch_analytics_by_months()
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from data")
    return data














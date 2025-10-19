import streamlit as st
from datetime import datetime
import requests

API_URL = "http://127.0.0.1:8000"
def add_update_expense_tab():
    date = st.date_input("Expense Date", datetime(2024, 8, 1), label_visibility="collapsed")
    st.write(f"Fetching expense details for date :{date}")
    response = requests.get(f"{API_URL}/expenses/{date}")
    if response.status_code == 200:
        existing_expenses = response.json()
        # st.write(existing_expenses)
    else:
        st.error("failed to fetch expense details")
        existing_expenses = []  # Intialize it to empty

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    with st.form(key="expense_form"):
        # Display Column headers
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("Amount")
        with col2:
            st.subheader("Category")
        with col3:
            st.subheader("notes")

        Expenses = []

        for i in range(5):

            if i < len(existing_expenses):
                amount = existing_expenses[i]["amount"]
                category = existing_expenses[i]['category']
                notes = existing_expenses[i]['notes']
            else:
                amount = 0.0
                category = "Shopping"
                notes = ""

            col1, col2, col3 = st.columns(3)
            with col1:
                amount_input = st.number_input(label="Amount", min_value=0.0, step=1.0, value=amount,
                                               key=f"Amount_{date}_{i}", label_visibility="collapsed")
            with col2:
                category_input = st.selectbox(label="Category", options=categories, index=categories.index(category),
                                              key=f"Category_{date}_{i}", label_visibility="collapsed")
            with col3:
                notes_input = st.text_input(label="notes", value=notes, key=f"Notes_{date}_{i}",
                                            label_visibility="collapsed")

            # st.write("🔍 Session State:", st.session_state)

            # st.write(amount,category,notes)
            Expenses.append({
                "amount": amount_input,
                "category": category_input,
                "notes": notes_input,
            })

        submit_btn = st.form_submit_button()

        if submit_btn:
            filtered_expensed = [exp for exp in Expenses if exp['amount'] > 0]
            response = requests.post(f"{API_URL}/expenses/{date}", json=filtered_expensed)
            if response.status_code == 200:
                st.success("Successfully updated expense")
            else:
                st.error("Failed to update expense")


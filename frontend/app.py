import streamlit as st
from add_update_tab import add_update_expense_tab
from analytics_by_category_tab import expense_analytics_tab
from analytics_by_month import expense_analytics_by_months_tab

API_URL = "http://127.0.0.1:8000"

st.title("Expense Tracking System")

tab1, tab2, tab3 = st.tabs(["Add/Update", "Analytics By Category", "Analytics By Months"])

with tab1:
    add_update_expense_tab()

with tab2:
    expense_analytics_tab()

with tab3:
    expense_analytics_by_months_tab()

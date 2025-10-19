import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

def expense_analytics_tab():
    col1 ,col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1))
    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 5))

    if st.button("Get Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
        }
        response = requests.post(f"{API_URL}/analytics", json=payload)
        response = response.json()
        #st.write(response)


        data =pd.DataFrame({
            "Category": list(response.keys()),
            "total":[response[category]["total"] for category in response],
            "percentage":[response[category]["percentage"] for category in response],

        })

        #df_sorted = pd.DataFrame(data)
        df_sorted = data.sort_values("percentage", ascending=False)


        st.title("Expense Breakdown by Categories")
        st.bar_chart(df_sorted.set_index("Category")["total"], use_container_width=True)

        df_sorted["total"] = df_sorted["total"].map('{:,.2f}'.format)
        #df_sorted["percentage"] = df_sorted["percentage"].round(2)
        df_sorted["percentage"] = df_sorted["percentage"].map('{:,.2f}'.format)


        st.table(df_sorted)








        #st.write([response.keys()])
        #st.write(response.keys())










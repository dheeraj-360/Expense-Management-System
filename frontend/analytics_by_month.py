import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

def expense_analytics_by_months_tab():
    st.title("Expense breakdown by months")
    response = requests.get(f"{API_URL}/analytics/months")
    response = response.json()
    #st.write(response)






    df = pd.DataFrame({
        "month": [response[i]["month"] for i in range(len(response))],
        "total": [response[i]["total"] for i in range(len(response))]
    })

    st.bar_chart(df.set_index("month")["total"], use_container_width=True)

    df["total"] = df["total"].map('{:,.2f}'.format)
    st.table(df)


# Expense Management System

A full-stack Expense Management System built with Streamlit, FastAPI, and MySQL that allows users to manage daily expenses, analyze spending patterns and store expense data in a database. This project gave me hands-on experience in frontend development, backend API creation, database integration, and end-to-end application design.

## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.

## Project Structure

```text
Expense-Management-System/
├── backend/                   # FastAPI backend
│   ├── server.py              # FastAPI server entry point
│   ├── db_helper.py           # Database helper functions (CRUD)
│   ├── logging_setup.py       # Backend logging configuration
│   └── tests/                 # Backend test cases
│       ├── test_server.py     
│       └── test_db_helper.py
│
├── frontend/                  # Streamlit frontend
│   ├── app.py                 # Main Streamlit app
│   ├── add_update_tab.py      # Add/Update Expense tab
│   ├── analytics_by_category.py  # Show Analytics by category
│   ├── analytics_by_month.py     # Show Analytics by month
│   
│
│
├── tests/                     # Integration tests
│   └── backend/
│       └── test_db_helper.sql
│   └── frontend/
│   └── conftest.py
│    
│
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation




## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/dheeraj-360/Expense-Management-System.git
   cd expense-management-system
   ```
1. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
1. **Run the FastAPI server:**:   
   ```commandline
    uvicorn server:app --reload
   ```
1. **Run the Streamlit app:**:   
   ```commandline
    streamlit run app.py

   ```

## Features

- Add, update, and manage daily expenses with details like amount, category, and notes.
- View analytics by date range, category, or monthly summary.
- Store and retrieve data from a MySQL database.
- Backend powered by FastAPI for handling API requests.
- Frontend built with Streamlit for an interactive user experience.
- Logging implemented for monitoring backend activity.

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI, Uvicorn
- **Database**: MySQL
- **Other Libraries**: Pydantic, Requests, Pytest, Logging

## API Endpoints

- **GET /expenses/{expense_date}**: Fetch expenses for a specific date.
- **POST /expenses/{expense_date}**: Add or Update expenses for a specific date.
- **POST /analytics/**: Fetch expense summary for a date range.
- **GET /analytics/months**: Fetch Total Expenses by Months

## Key Learnings

1. **Building Full-Stack Python Applications**  
   Gained hands-on experience designing and developing a complete end-to-end application — integrating frontend, backend, and database layers.

2. **Handling Frontend State with Streamlit (`st.session_state`)**  
   Learned how Streamlit re-runs scripts and how to persist widget data using `st.session_state` with unique keys.

3. **Creating REST APIs with FastAPI (GET & POST Requests)**  
   Built RESTful APIs for data communication between frontend and backend, using Pydantic for request validation and response modelling.

4. **Integrating Database CRUD Operations with MySQL**  
   Implemented Create, Read, Update, and Delete (CRUD) operations safely and efficiently.

5. **Logging and Debugging for Backend Applications**  
   Configured logging in FastAPI for tracking API usage and debugging issues.

6. **Data Visualization and Analytics**  
   Built expense analytics dashboards to visualize spending patterns and trends.

---
## Acknowledgement

This project was inspired by the **Codebasics Bootcamp**. While the core idea originated from their learning materials, I have extended and customized the implementation with additional features, integrations, and improvements to deepen my understanding of end-to-end application development.


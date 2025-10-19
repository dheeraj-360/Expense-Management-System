import mysql.connector as mysql
from contextlib import contextmanager
from logging_setup import setup_logging

logger = setup_logging("db_helper")


@contextmanager
def dbconnection_get_cursor(commit = False):
    connection = mysql.connect(host="localhost",
                               user="root",
                               password="root",
                               database="expense_manager")


    cursor = connection.cursor(dictionary=True)
    yield cursor

    if commit:
        connection.commit()

    cursor.close()
    connection.close()




def get_all_expenses():
    with dbconnection_get_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()
        return expenses



def fetch_expenses_for_date(date):
    logger.info(f"fetch_expenses_for_date: {date}")
    with dbconnection_get_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses where expense_date = %s", (date,))
        expenses = cursor.fetchall()
        return expenses

def insert_expense(expense_date,amount, category,notes):
    logger.info(f"insert_expense called for : {expense_date}, {amount}, {category}, {notes}")
    with dbconnection_get_cursor(commit = True) as cursor:
        cursor.execute("INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s) ",
                       (expense_date, amount, category, notes))

def delete_expense_for_date(expense_date):
    logger.info(f"delete_expense called for : {expense_date}")
    with dbconnection_get_cursor(commit = True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))


def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetch_expense_summary called for : {start_date}, {end_date}")
    with dbconnection_get_cursor() as cursor:
        cursor.execute(
            '''select category, SUM(amount) as total
               from expenses
               WHERE expense_date BETWEEN %s AND %s 
               GROUP BY category''', (start_date, end_date))
        data = cursor.fetchall()
        return data

def fetch_analytics_by_months():
    logger.info(f"fetch_analytics_by_months called")
    with dbconnection_get_cursor() as cursor:
        cursor.execute('''select monthname(expense_date) as month , sum(amount) as total from expenses
group by monthname(expense_date) 
order by monthname(expense_date) ''')
        data = cursor.fetchall()
        return data



if __name__ == "__main__":
    expense_data = fetch_expenses_for_date("2024-08-01")
    print(expense_data)
    #insert_expense("2024-08-25",40,"Food","Eat Tasty samosa Chat")
    #delete_expense_for_date("2024-08-25")
    summary = fetch_expense_summary("2024-08-01","2024-08-05")
    for row in summary:
        print(row)
    by_months = fetch_analytics_by_months()
    print(by_months)

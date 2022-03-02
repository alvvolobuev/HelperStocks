import sqlite3

def get_price(name_stocks):
    try:
        sqlite_connection = sqlite3.connect('database.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = "SELECT price FROM stocks where name_stocks = ?"
        cursor.execute(sqlite_select_query, (name_stocks,))
        records = cursor.fetchall()
        cursor.close()
        for row in records:
            return row[0]

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


def get_technikal_5min(name_stocks):
    try:
        sqlite_connection = sqlite3.connect('database.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = "SELECT result_5_min FROM stocks where name_stocks = ?"
        cursor.execute(sqlite_select_query, (name_stocks,))
        records = cursor.fetchall()
        cursor.close()
        for row in records:
            return row[0]

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

def get_technikal_15min(name_stocks):
    try:
        sqlite_connection = sqlite3.connect('database.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = "SELECT result_15_min FROM stocks where name_stocks = ?"
        cursor.execute(sqlite_select_query, (name_stocks,))
        records = cursor.fetchall()
        cursor.close()
        for row in records:
            return row[0]

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


def get_technikal_1hour(name_stocks):
    try:
        sqlite_connection = sqlite3.connect('database.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = "SELECT result_1_hour FROM stocks where name_stocks = ?"
        cursor.execute(sqlite_select_query, (name_stocks,))
        records = cursor.fetchall()
        cursor.close()
        for row in records:
            return row[0]

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


def get_technikal_1day(name_stocks):
    try:
        sqlite_connection = sqlite3.connect('database.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = "SELECT result_1_day FROM stocks where name_stocks = ?"
        cursor.execute(sqlite_select_query, (name_stocks,))
        records = cursor.fetchall()
        cursor.close()
        for row in records:
            return row[0]

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


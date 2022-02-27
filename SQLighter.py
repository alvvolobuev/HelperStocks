import sqlite3


def get_link_stocks(name_stocks):
    try:
        sqlite_connection = sqlite3.connect('database.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = "SELECT link FROM stocks where name_stocks = ?"
        cursor.execute(sqlite_select_query, (name_stocks,))
        records = cursor.fetchall()
        cursor.close()
        for row in records:
            return row[0]

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)



def update_price_stocks(name_stocks, price):
    try:
        sqlite_connection = sqlite3.connect('database.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = "UPDATE stocks SET price = ? WHERE name_stocks = ?"
        cursor.execute(sqlite_select_query, (price, name_stocks))
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)



def update_technical_analysis(name_stocks, technical_analysis):
    try:
        sqlite_connection = sqlite3.connect('database.db')
        cursor = sqlite_connection.cursor()
        result = ('result_5_min', 'result_15_min', 'result_1_hour', 'result_1_day')

        for i in range(0, 4):
            sqlite_select_query = f"UPDATE stocks SET {result[i]} = ? WHERE name_stocks = ?"
            cursor.execute(sqlite_select_query, (technical_analysis[i], name_stocks))

        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


def parsing(name_stocks):
    try:
        sqlite_connection = sqlite3.connect('database.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = "SELECT parsing FROM stocks where name_stocks = ?"
        cursor.execute(sqlite_select_query, (name_stocks,))
        records = cursor.fetchall()
        cursor.close()
        for row in records:
            return row[0]

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
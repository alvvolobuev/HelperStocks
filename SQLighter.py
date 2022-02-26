import sqlite3


def get_link_stocks(name_stocks):
    global sqlite_connection
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
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def update_price_stocks(name_stocks, price):
    global sqlite_connection

    try:
        sqlite_connection = sqlite3.connect('database.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = "UPDATE stocks SET price = ? WHERE name_stocks = ?"
        cursor.execute(sqlite_select_query, (price, name_stocks))
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


# Тестовые данные
#link_stock = get_link_stocks("Sberbank")
#for row in link_stock:
#    print(row[0])

#update_price_stocks("Sberbank", 131.12)

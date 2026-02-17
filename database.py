from pymysql import connect, cursors


def register_user(telegram_id, full_name):
    database_connection = connect(
        database='n74_bot',
        user='root',
        password='Nilufaroy@6',
        host='localhost',
        port=3306,
        cursorclass=cursors.DictCursor
    )

    cursor = database_connection.cursor()

    sql = "INSERT INTO users (telegram_id, full_name) VALUES (%s, %s)"
    cursor.execute(sql, (telegram_id, full_name))

    database_connection.commit()
    cursor.close()
    database_connection.close()


def get_user_info(telegram_id):
    database_connection = connect(
        database='n74_bot',
        user='root',
        password='Nilufaroy@6',
        host='localhost',
        port=3306,
        cursorclass=cursors.DictCursor
    )

    cursor = database_connection.cursor()

    sql = "SELECT telegram_id, full_name FROM users WHERE telegram_id = %s"
    cursor.execute(sql, (telegram_id,))
    user = cursor.fetchone()

    cursor.close()
    database_connection.close()

    return user

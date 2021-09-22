import psycopg2
from Test2 import host, user, password, db_name

try:
    #Подключение к базе данных
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    #Также нам нужно создать переменную курсор(cursor) - это обьект который содержит в себе методы в SQLcommand
    #Можно положить его значение в переменную
    cursor = connection.cursor()

    #или воспользоваться контекстным менеджером with
    with connection.cursor as cursor:
        #чтобы запросить что то у cursor нужен метод execute
        cursor.execute(
            #передаем в него запрос - SELECT VERSION
            "SELECT version();"
        )

        #также здесь используем метод fetchone, который должен вернуть кортеж или num если запрос будет пустым
        print(f"Server version(): {cursor.fetchone()}")
except Exception as _ex:
    print("[INFO]Error while working with PostgreesSQL", _ex)
finally:
    if connection:
        #Если ложить курсор в переменную без метода with, то в finnaly нужна строчка ниже закрывающая его
        #cursor.close()
        connection.close() # Закрытое соединение
        print("[INFO]PostgreSQL connection closed")
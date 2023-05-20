import db_config
import psycopg2

class Author:
    def __init__(self, id: int) -> None:
        self.id = id
        self.nickname = ""
        self.role = ""

        try:
            print(f"[+] Opened database connection to create author object with id = {self.id}")
            conn = psycopg2.connect(database=db_config.db_name, user=db_config.user, password=db_config.password)
            cursor = conn.cursor()

            cursor.execute(f"SELECT nickname, role from author where id = {self.id} LIMIT 1 OFFSET 0")
            data_row = cursor.fetchone()
            self.nickname = str(data_row[0])
            self.role = str(data_row[1])

        except Exception as Ex:
            print(f"[!] Caught exception: {Ex}")

        finally:
            cursor.close()
            conn.close()
            print(f"[-] Closed author database connection from object with id = {self.id}")

class Category:
    def __init__(self, id: int) -> None:
        self.id = id
        self.icon = ""
        self.description = ""

        try:
            print(f"[+] Opened database connection to create category object with id = {self.id}")
            conn = psycopg2.connect(database=db_config.db_name, user=db_config.user, password=db_config.password)
            cursor = conn.cursor()

            cursor.execute(f"SELECT icon, description from category where id = {self.id} LIMIT 1 OFFSET 0")
            data_row = cursor.fetchone()
            self.icon = str(data_row[0])
            self.description = str(data_row[1])

        except Exception as Ex:
            print(f"[!] Caught exception: {Ex}")

        finally:
            cursor.close()
            conn.close()
            print(f"[-] Closed category database connection from object with id = {self.id}")

class Post:
    def __init__(self, id: int) -> None:
        self.id = id
        self.title = ""
        self.description = ""
        self.date = ""
        self.category_id = 0
        self.author_id = 0

        try:
            print(f"[+] Opened database connection to create post object with id = {self.id}")
            conn = psycopg2.connect(database=db_config.db_name, user=db_config.user, password=db_config.password)
            cursor = conn.cursor()

            cursor.execute(f"SELECT title, description, date, category_id, author_id from post where id = {self.id} LIMIT 1 OFFSET 0")
            data_row = cursor.fetchone()
            self.title = str(data_row[0])
            self.description = str(data_row[1])
            self.date = str(data_row[2])
            self.category_id = str(data_row[3])
            self.author_id = str(data_row[4])

        except Exception as Ex:
            print(f"[!] Caught exception: {Ex}")

        finally:
            cursor.close()
            conn.close()
            print(f"[-] Closed post database connection from object with id = {self.id}")        

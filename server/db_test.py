import json
import db_config as db_config
import psycopg2

def data_add_author(uuid, nickname, role):
    try:
        conn = psycopg2.connect(database=db_config.db_name, user=db_config.user, password=db_config.password)
        cursor = conn.cursor()
        cursor.execute(f""" INSERT INTO author (uuid, nickname, role) values ('{uuid}', '{nickname}', '{role}')""")
        conn.commit()


    except Exception as Ex:
        print(Ex)
    finally:
        cursor.close()
        conn.close() 

def create_author_table():
    try:
        conn = psycopg2.connect(database=db_config.db_name, user=db_config.user, password=db_config.password)
        cursor = conn.cursor()
        # cursor.execute('SELECT version();')
        create_table = '''CREATE TABLE author (ID BIGSERIAL, UUID TEXT NOT NULL, NICKNAME TEXT, ROLE TEXT)'''
        
        cursor.execute(create_table)
        conn.commit()

        # print(version)
    except Exception as Ex:
        print(Ex)
    finally:
        cursor.close()
        conn.close() 

def create_category_table():
    try:
        conn = psycopg2.connect(database=db_config.db_name, user=db_config.user, password=db_config.password)
        cursor = conn.cursor()
        # cursor.execute('SELECT version();')
        create_table = '''CREATE TABLE category (ID BIGSERIAL, ICON TEXT NOT NULL, DESCRIPTION TEXT NOT NULL)'''
        
        cursor.execute(create_table)
        conn.commit()
        cursor.execute(""" INSERT INTO category (icon, description) values ('*', 'Общая категория')""")
        cursor.execute(""" INSERT INTO category (icon, description) values ('!', 'Тех. работы')""")
        cursor.execute(""" INSERT INTO category (icon, description) values ('@', 'Ивенты')""")
        cursor.execute(""" INSERT INTO category (icon, description) values ('$', 'Баннеры')""")
        conn.commit()

        # print(version)
    except Exception as Ex:
        print(Ex)
    finally:
        cursor.close()
        conn.close() 

def create_post_table():
    try:
        conn = psycopg2.connect(database=db_config.db_name, user=db_config.user, password=db_config.password)
        cursor = conn.cursor()

        create_table = '''CREATE TABLE post (ID BIGSERIAL, DATE TEXT NOT NULL, TITLE TEXT NOT NULL, DESCRIPTION TEXT NOT NULL, CATEGORY_ID INTEGER NOT NULL, AUTHOR_ID BIGINT NOT NULL)'''
        
        cursor.execute(create_table)
        conn.commit()
    except Exception as Ex:
        print(Ex)
    finally:
        cursor.close()
        conn.close() 

def delete_table(table_name):
    try:
        conn = psycopg2.connect(database=db_config.db_name, user=db_config.user, password=db_config.password)
        cursor = conn.cursor()
        cursor.execute(f"""DROP TABLE {table_name}""")
        conn.commit()


    except Exception as Ex:
        print(Ex)
    finally:
        cursor.close()
        conn.close() 

def create_posts():
    conn = psycopg2.connect(database=db_config.db_name, user=db_config.user, password=db_config.password)
    cursor = conn.cursor()

    try:
        with open("./server/test.json", "rt+", encoding="UTF-8") as file:
            data = json.loads(file.read())
            # print(data)
            for post in data:
                cursor.execute(f""" INSERT INTO post (date, title, description, category_id, author_id) values ('{str(post["date"])}', '{str(post["title"])}', '{str(post["content"])}', {int(post["category_id"])}, {int(post["author_id"])})""")
        conn.commit()

        # print(version)
    except Exception as Ex:
        print(Ex)
    finally:
        cursor.close()
        conn.close() 

# delete_table("post")
# create_category_table()
# create_author_table()
# create_post_table()
# create_posts()
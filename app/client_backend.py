from flet import *
import db_config
import psycopg2

class Author:
    def __init__(self, id: int) -> None:
        self.id = id
        self.uuid = None
        self.nickname = None
        self.icon = None
        self.role = None
        self.card = None

        try:
            print(f"[+] Opened database client connection to create author object with id = {self.id}")
            conn = psycopg2.connect(database=db_config.db_name, user=db_config.user, password=db_config.password)
            cursor = conn.cursor()

            cursor.execute(f"SELECT uuid, nickname, role from author where id = {self.id} LIMIT 1 OFFSET 0")
            data_row = cursor.fetchone()
            self.uuid = str(data_row[0])
            self.nickname = str(data_row[1])
            self.role = str(data_row[2])
            self.icon = f"https://mc-heads.net/head/{self.nickname}/48"
            self.card = f"https://127.0.0.1/generate_tab/author/{self.id}"

        except Exception as Ex:
            print(f"[!] Caught exception: {Ex}")

        finally:
            cursor.close()
            conn.close()
            print(f"[-] Closed author client database connection from object with id = {self.id}")

class Category:
    def __init__(self, id: int) -> None:
        self.id = id
        self.icon = None
        self.description = None
        self.card = None

        try:
            print(f"[+] Opened database client connection to create category object with id = {self.id}")
            conn = psycopg2.connect(database=db_config.db_name, user=db_config.user, password=db_config.password)
            cursor = conn.cursor()

            cursor.execute(f"SELECT icon, description from category where id = {self.id} LIMIT 1 OFFSET 0")
            data_row = cursor.fetchone()
            self.icon = str(data_row[0])
            self.description = str(data_row[1])
            self.card = f"https://127.0.0.1/generate_tab/category/{self.id}"

        except Exception as Ex:
            print(f"[!] Caught exception: {Ex}")

        finally:
            cursor.close()
            conn.close()
            print(f"[-] Closed category database client connection from object with id = {self.id}")

class SmallPost():
    def __init__(self, id: int) -> None:
        self.id = id
        self.title = None
        self.category_id = None

        try:
            print(f"[+] Opened database client connection to create small post object with id = {self.id}")
            conn = psycopg2.connect(database=db_config.db_name, user=db_config.user, password=db_config.password)
            cursor = conn.cursor()

            cursor.execute(f"SELECT title, category_id from post where id = {self.id} LIMIT 1 OFFSET 0")
            data_row = cursor.fetchone()
            self.title = str(data_row[0])
            self.category_id = str(data_row[1])

        except Exception as Ex:
            print(f"[!] Caught exception: {Ex}")

        finally:
            cursor.close()
            conn.close()
            print(f"[-] Closed small post database client connection from object with id = {self.id}")

        self.post = Container(
            width=900,
            height=120,
            image_src="assets/title_small.png",
            on_click=self.show_post,
            on_hover=self.show_category,
            content=Column(
                controls=[
                    Text(
                        value=self.title,
                        text_align="center",
                        font_family="main",
                        size=20,
                    )
                ],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        )

    def show_post(self, e: TapEvent):
        e.control.width = 900
        e.control.height = 600
        e.control.image_src = "assets/post_bg.png"
        e.control.content = Post(self.id).post.content
        e.control.update()

    def show_category(self, e: HoverEvent):
        if e.data == "true":
            pass
        else:
            pass

class Post():
    def __init__(self, id: int) -> None:
        self.id = id
        self.date = None
        self.title = None
        self.description = None
        self.category_id = None
        self.author_id = None
        self.author = None
        self.category = None
        

        try:
            print(f"[+] Opened database client connection to create post object with id = {self.id}")
            conn = psycopg2.connect(database=db_config.db_name, user=db_config.user, password=db_config.password)
            cursor = conn.cursor()

            cursor.execute(f"SELECT title, description, date, category_id, author_id from post where id = {self.id} LIMIT 1 OFFSET 0")
            data_row = cursor.fetchone()
            self.title = str(data_row[0])
            self.description = str(data_row[1])
            self.date = str(data_row[2])
            self.category_id = str(data_row[3])
            self.author_id = str(data_row[4])
            self.author = Author(self.author_id)
            self.category = Category(self.category_id)

        except Exception as Ex:
            print(f"[!] Caught exception: {Ex}")

        finally:
            cursor.close()
            conn.close()
            print(f"[-] Closed post database client connection from object with id = {self.id}")       

        self.post = Container(  # post
            width=900,
            height=600,
            image_src="assets/post_bg.png",
            content=Column(
                controls=[
                    Container(  # title
                        padding=padding.only(
                            left=36,
                            top=33,
                        ),
                        content=Row(
                            controls=[
                                Stack(  # post type
                                    controls=[
                                        Column(
                                            width=48,
                                            height=48,
                                            alignment=MainAxisAlignment.CENTER,
                                            horizontal_alignment=CrossAxisAlignment.CENTER,
                                            controls=[
                                                Text(
                                                    value=self.category.icon,
                                                    text_align="center",
                                                    font_family='main',
                                                    size=30,
                                                )
                                            ]
                                        ),
                                        Container(
                                            width=48,
                                            height=48,
                                            bgcolor="white",
                                            opacity=0,
                                            on_hover=self.category_button_hover,
                                        )
                                    ]
                                ),
                                Container(  # post title
                                    margin=margin.only(
                                        left=2,
                                    ),
                                    width=696,
                                    height=48,
                                    content=Column(
                                        alignment=MainAxisAlignment.CENTER,
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                        controls=[
                                            Text(
                                                value=self.title,
                                                text_align="center",
                                                font_family='main',
                                                max_lines=1,
                                                size=20,
                                            ),
                                        ]
                                    )
                                ),
                                Container(  # post author
                                    margin=margin.only(
                                        left=14,
                                        top=2,
                                    ),
                                    width=48,
                                    height=51,
                                    content=Stack(
                                        controls=[
                                            Image(
                                                src=self.author.icon
                                            ),
                                            Container(
                                                width=48,
                                                height=51,
                                                bgcolor="white",
                                                opacity=0,
                                                on_hover=self.author_button_hover
                                            )
                                        ]
                                    ),
                                )
                            ]
                        )
                    ),
                    Container(  # description
                        width=840,
                        height=464,
                        padding=padding.only(
                            left=8,
                            right=8,
                            top=4,
                            bottom=4
                        ),
                        margin=margin.only(
                            top=8,
                            left=32
                        ),
                        content=Column(
                            scroll='auto',
                            controls=[
                                Text(
                                    value=self.description,
                                    font_family='main',
                                    size=20
                                )
                            ]
                        )
                    ),
                    Container(  # date
                        height=20,
                        width=172,
                        # bgcolor="red",
                        margin=margin.only(
                            left=40,
                            top=-6
                        ),
                        content=Column(
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                Text(
                                    value=self.date,
                                    font_family='main',
                                    size=16
                                )
                            ]
                        )
                    )
                ]
            )
        )

    def category_button_hover(self, e: HoverEvent):
        if e.data == "true":
            e.control.opacity = 0.1
            e.control.bgcolor = "white"
            e.control.update()
        else:
            e.control.opacity = 1
            e.control.bgcolor = None
            e.control.update()

    def author_button_hover(self, e: HoverEvent):
        if e.data == "true":
            e.control.opacity = 0.1
            e.control.bgcolor = "white"
            e.control.update()
        else:
            e.control.opacity = 1
            e.control.bgcolor = None
            e.control.update()
import sqlite3 as sql

class Commands():
    def __init__(self):
        self.create_database()

    def create_database(self):
        db = sql.connect("../DataBaseTelegram.db")
        cursor = db.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user(
            id TEXT,
            name TEXT,
            class INTEGER
            )
        """)
        db.commit()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS lessons(
            user_id TEXT,
            lesson1 TEXT,
            lesson2 TEXT,
            lesson3 TEXT,
            lesson4 TEXT,
            )
        """)
        db.commit()


    def add_new_user(self, user_id, user_name, user_class):
        self.db = sql.connect("../DataBaseTelegram.db")
        self.cursor = self.db.cursor()
        self.cursor.execute(f"""
        SELECT * FROM user WHERE id=? and class=?
        """, (user_id, user_class))

        replay =self.cursor.fetchone()

        if not(replay):
            self.cursor.execute("""
            INSERT INTO user (id, name, class) VALUES (?, ?, ?)
            """, (int(user_id), str(user_name), user_class))
            self.db.commit()

    def add_new_lessons(self, user_id, lesson_name):
        self.db = sql.connect("../DataBaseTelegram.db")
        self.cursor = self.db.cursor()
        self.cursor.execute(f"""
        SELECT * FROM lessons WHERE id=?
        """, (user_id))

        replay =self.cursor.fetchone()

        if not(replay):
            self.cursor.execute("""
            INSERT INTO lessons (user_id, lesson1, lesson2, lesson3, lesson4) VALUES (?, ?, ?, ?, ?)
            """, (int(user_id), lesson_name))
            self.db.commit()
import psycopg2


class DataBase:
    def __init__(self):
        self.database = psycopg2.connect(
            database='news',
            user='postgres',
            host='localhost',
            password='1'
        )

    def manager(self, sql, *args, commit=False, fetchone=False, fetchall=False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    result = db.commit()
                elif fetchone:
                    result = cursor.fetchone()
                elif fetchall:
                    result = cursor.fetchall()
            return result

    def create_table_categories(self):
        sql = '''CREATE TABLE IF NOT EXISTS categories(
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            description TEXT
        );'''
        self.manager(sql, commit=True)

    def create_table_news(self):
        sql = '''CREATE TABLE IF NOT EXISTS news(
            id SERIAL PRIMARY KEY,
            category_id INTEGER REFERENCES categories(id) ON DELETE SET NULL,
            title VARCHAR(200) NOT NULL,   
            content TEXT NOT NULL,
            published_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            is_published BOOLEAN DEFAULT False
        );'''
        self.manager(sql, commit=True)

    def create_table_comments(self):
        sql = '''CREATE TABLE IF NOT EXISTS comments(
            id SERIAL PRIMARY KEY,
            news_id INTEGER REFERENCES news(id) ON DELETE CASCADE,
            author_name VARCHAR(100),
            comment_text TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );'''
        self.manager(sql, commit=True)

    def alter_table_news(self):
        sql = '''ALTER TABLE news
        ADD COLUMN views INTEGER DEFAULT 0;'''
        self.manager(sql, commit=True)

    def alter_table_comments(self):
        sql = '''ALTER TABLE comments ALTER COLUMN author_name TYPE TEXT;'''
        self.manager(sql, commit=True)

    def insert_categories(self, name, description):
        sql = '''INSERT INTO categories(name, description) VALUES (%s, %s) ON CONFLICT DO NOTHING'''
        self.manager(sql, name, description, commit=True)

    def insert_news(self, category_id, title, content):
        sql = '''INSERT INTO news(category_id, title, content) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING'''
        self.manager(sql, category_id, title, content, commit=True)

    def insert_comments(self, news_id, author_name, comment_text):
        sql = '''INSERT INTO comments(news_id, author_name, comment_text) VALUES (%s, %s, %s)
        ON CONFLICT DO NOTHING'''
        self.manager(sql, news_id, author_name, comment_text, commit=True)

    def increase_news(self):
        sql = '''UPDATE news SET views = views + 1;'''
        self.manager(sql, commit=True)

    def update_is_published(self):
        sql = '''UPDATE news
        SET is_published = TRUE
        WHERE published_at <= CURRENT_TIMESTAMP - INTERVAL '1 day';'''
        self.manager(sql, commit=True)

    def delete_old_comments(self):
        sql = '''delete from comments where created_at < current_date - interval '1 year';
        '''
        self.manager(sql, commit=True)

    def select_alias(self):
        sql = '''SELECT n.id, n.title AS news_title, c.name AS category_name FROM news
        AS n JOIN categories AS c ON c.id = n.category_id;
        '''
        return self.manager(sql, fetchall=True)

    def select_technology(self):
        sql = '''select news.title, news.content, news.published_at, categories.name
        from news join categories on categories.id = news.category_id where name = 'Technology';
        '''
        return self.manager(sql, fetchall=True)

    def sorted_news(self):
        sql = '''SELECT * FROM news ORDER BY published_at DESC LIMIT 5;
        '''
        return self.manager(sql, fetchall=True)

    def select_views(self):
        sql = '''select * from news where views between 10 and 100;
        '''
        return self.manager(sql, fetchall=True)

    def select_capital_a(self, value):
        sql = '''SELECT * FROM comments WHERE author_name LIKE %s;
        '''
        return self.manager(sql, value, fetchall=True)

    def select_null(self):
        sql = '''SELECT * FROM comments WHERE author_name IS NULL'''
        return self.manager(sql, fetchall=True)

    def select_categories(self):
        sql = '''SELECT categories.name AS category_name, COUNT(news.category_id) FROM categories
        JOIN news ON categories.id = news.category_id GROUP BY categories.name;'''
        return self.manager(sql, fetchall=True)

    def add_constraint(self):
        sql = '''ALTER TABLE news ADD CONSTRAINT new_title UNIQUE(title);'''
        self.manager(sql, commit=True)


db = DataBase()

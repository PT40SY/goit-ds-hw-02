import sqlite3
from faker import Faker

fake = Faker()

connection = sqlite3.connect('tasks_management.db')
cursor = connection.cursor()

statuses = [('new',), ('in progress',), ('completed',)]
cursor.executemany('INSERT INTO status (name) VALUES (?)', statuses)

users = [(fake.name(), fake.unique.email()) for _ in range(10)]
cursor.executemany('INSERT INTO users (fullname, email) VALUES (?, ?)', users)

tasks = [
    (
        fake.sentence(nb_words=3),
        fake.text(),
        fake.random_int(min=1, max=len(statuses)),
        fake.random_int(min=1, max=10)
    )
    for _ in range(20)
]
cursor.executemany('INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)', tasks)

connection.commit()
connection.close()

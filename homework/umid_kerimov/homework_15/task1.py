import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)
cursor = db.cursor(dictionary=True)

cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)",
               ('Umid', 'Kerimov', None))
student_id = cursor.lastrowid
db.commit()

cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
               ('Students Umid', '16 April', '17 April'))
group_id = cursor.lastrowid
db.commit()

cursor.execute("UPDATE students SET group_id = %s WHERE id = %s", (group_id, student_id))
db.commit()

books_data = [
    ('Маша и Медведь', student_id),
    ('Колобок', student_id),
    ('Репка', student_id)
]

book_ids = []
for title, taken_by in books_data:
    cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)",
                   (title, taken_by))
    book_id = cursor.lastrowid
    book_ids.append(book_id)
db.commit()

subjects_data = ['Музыка', 'История', 'Информатика']
subject_ids = {}

for title in subjects_data:
    cursor.execute("INSERT INTO subjects (title) VALUES (%s)", (title,))
    subject_id = cursor.lastrowid
    subject_ids[title] = subject_id
db.commit()

lessons_data = [
    ('Музыка', subject_ids['Музыка']),
    ('Музыка', subject_ids['Музыка']),
    ('Информатика', subject_ids['Информатика']),
    ('Информатика', subject_ids['Информатика']),
    ('История', subject_ids['История']),
    ('История', subject_ids['История'])
]

lesson_ids = {'Музыка': [], 'Информатика': [], 'История': []}
for title, subject_id in lessons_data:
    cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
                   (title, subject_id))
    lesson_id = cursor.lastrowid
    lesson_ids[title].append(lesson_id)
db.commit()

marks_data = [
    (5, lesson_ids['Музыка'][0], student_id),
    (4, lesson_ids['Музыка'][0], student_id),
    (2, lesson_ids['Информатика'][0], student_id),
    (3, lesson_ids['Информатика'][0], student_id),
    (4, lesson_ids['История'][0], student_id),
    (5, lesson_ids['История'][0], student_id)
]

for value, lesson_id, stud_id in marks_data:
    cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
                   (value, lesson_id, stud_id))
db.commit()

cursor.execute("SELECT value FROM marks WHERE student_id = %s", (student_id,))
marks = cursor.fetchall()
print("Оценки:", [mark['value'] for mark in marks])

cursor.execute("SELECT * FROM books WHERE taken_by_student_id = %s", (student_id,))
books = cursor.fetchall()
for book in books:
    print(f"  ID={book['id']}, '{book['title']}', taken_by={book['taken_by_student_id']}")

query = """
SELECT
    s.id AS student_id,
    s.name,
    s.second_name,
    g.title AS group_title,
    b.title AS book_title,
    m.value AS mark_value,
    l.title AS lesson_title,
    sub.title AS subject_title
FROM students s
LEFT JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON b.taken_by_student_id = s.id
LEFT JOIN marks m ON m.student_id = s.id
LEFT JOIN lessons l ON l.id = m.lesson_id
LEFT JOIN subjects sub ON sub.id = l.subject_id
WHERE s.id = %s
"""
cursor.execute(query, (student_id,))
results = cursor.fetchall()

print("Полная информация о студенте:")
print("ID | Имя | Фамилия | Группа | Книга | Оценка | Урок | Предмет")
print("-" * 80)
for row in results:
    print(
        f"{row['student_id']:2} | {row['name']:3} | {row['second_name']:9} | "
        f"{row['group_title'] or '-':6} | {row['book_title'] or '-':10} | "
        f"{row['mark_value'] or '-':6} | {row['lesson_title'] or '-':6} | "
        f"{row['subject_title'] or '-':10}")

db.close()

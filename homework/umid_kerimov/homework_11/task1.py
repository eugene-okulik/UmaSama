class Book:
    page_material = "Бумага"
    presence_of_text = True

    def __init__(self, name_book, author, count_page, isbn, reserve_book):
        self.name_book = name_book
        self.reserve_book = reserve_book
        self.author = author
        self.count_page = count_page
        self.ISBN = isbn


book1 = Book('Идиот', 'Достоевский', 500, 1231231, True)
book2 = Book('Великий Гэтсби', 'Скотт Фицджеральд', 300, 3213112, False)
book3 = Book('Гордость и предубеждение', 'Джейн Остин', 400, 4535251,
             False)
book4 = Book('Убить пересмешника', 'Харпер Ли', 150, 7373771, False)
book5 = Book('Мастер и Маргарита', 'Булгаков', 600, 18818181, False)

books = [book1, book2, book3, book4, book5]
for book in books:
    if book.reserve_book:
        print(
            f'Название: {book.name_book}, '
            f'Автор: {book.author}, '
            f'Страниц: {book.count_page}, '
            f'Материал: {Book.page_material},'
            f' Зарезервирована')
    else:
        print(
            f'Название: {book.name_book}, '
            f'Автор: {book.author}, '
            f'Страниц: {book.count_page},'
            f' Материал: {Book.page_material}')


class SchoolBook(Book):
    def __init__(self, name_book, author, count_page, isbn, reserve_book, num_class, subject):
        super().__init__(name_book, author, count_page, isbn, reserve_book)
        self.num_class = num_class
        self.subject = subject


mathematics = SchoolBook('Алгебра', 'Петров', '200', 1231232132, True,
                         9, 'Математика')
history = SchoolBook('История', 'Иванов', 100, 91919191, False,
                     8, 'История')
geography = SchoolBook('География', 'Сидоров', 300, 2191919, False,
                       10, 'География', )

subjects = [mathematics, history, geography]

for theme in subjects:
    if theme.reserve_book:
        print(
            f'Название: {theme.name_book}, '
            f'Автор: {theme.author}, '
            f'Страниц: {theme.count_page}, '
            f'Предмет: {theme.subject}, '
            f'Класс: {theme.num_class}, Зарезервирована')
    else:
        print(
            f'Название: {theme.name_book}, '
            f'Автор: {theme.author}, '
            f'Страниц: {theme.count_page}, '
            f'Предмет: {theme.subject}, '
            f'Класс: {theme.num_class}')

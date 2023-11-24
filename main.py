import sqlite3

# Подключение БД
conn = sqlite3.connect('library.db')
cursor = conn.cursor()


# Создание таблицы в БД
def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            description TEXT,
            genre TEXT
        )
    ''')
    conn.commit()


# Добавление книги
def add_book():
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    description = input("Введите описание книги: ")
    genre = input("Введите жанр книги: ")

    cursor.execute('INSERT INTO books (title, author, description, genre) VALUES (?, ?, ?, ?)',
                   (title, author, description, genre))
    conn.commit()
    print("Книга успешно добавлена!")


# Просмотр книг в библиотеке
def view_books():
    cursor.execute('SELECT id, title, author FROM books')
    books = cursor.fetchall()

    if not books:
        print("Библиотека пуста.")
    else:
        print("Список книг:")
        for book in books:
            print(f"{book[0]}. {book[1]} - {book[2]}")

# Показ деталей книги
def view_book_details(book_id):
    cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
    book = cursor.fetchone()

    if book:
        print(f"Название: {book[1]}")
        print(f"Автор: {book[2]}")
        print(f"Описание: {book[3]}")
        print(f"Жанр: {book[4]}")
    else:
        print("Книга не найдена.")
# Поиск по жанру
def search_by_genre(genre):
    cursor.execute('SELECT id, title, author FROM books WHERE genre = ?', (genre,))
    books = cursor.fetchall()
    if not books:
        print("Книги не найдены.")
    else:
        print("Результаты поиска:")
        for book in books:
            print(f"{book[0]}. {book[1]} - {book[2]}")
# Поиск в библиотеке
def search_books(keyword):
    cursor.execute('SELECT id, title, author FROM books WHERE title LIKE ? OR author LIKE ?',
                   (f'%{keyword}%', f'%{keyword}%'))
    books = cursor.fetchall()

    if not books:
        print("Книги не найдены.")
    else:
        print("Результаты поиска:")
        for book in books:
            print(f"{book[0]}. {book[1]} - {book[2]}")


# Удаление книги
def delete_book(book_id):
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()
    print("Книга успешно удалена.")


# Поиск книги по ключевому слову
def book_search():
    keyword = input("Введите ключевое слово для поиска: ")
    search_books(keyword)

# Запуск с основного файла
if __name__ == "__main__":
    create_table()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Просмотреть список книг")
        print("3. Просмотреть подробности книги")
        print("4. Поиск книги")
        print("5. Поиск книги по жанру")
        print("6. Удалить книгу")
        print("0. Выход")

        choice = input("Выберите действие: ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            book_id = input("Введите ID книги для просмотра подробностей: ")
            view_book_details(book_id)
        elif choice == '4':
            keyword = input("Введите ключевое слово для поиска: ")
            search_books(keyword)
        elif choice == '5':
            genre = input("Введите жанр для поиска: ")
            search_by_genre(genre)
        elif choice == '6':
            book_id = input("Введите ID книги для удаления: ")
            delete_book(book_id)
        elif choice == '0':
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из списка.")






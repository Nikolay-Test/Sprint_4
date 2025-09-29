# Тесты для приложения BooksCollector

## Описание
Данный проект содержит набор автоматизированных тестов для класса `BooksCollector`, который позволяет управлять коллекцией книг, устанавливать жанры и добавлять книги в избранное.

## Структура проекта
- `main.py` - исходный код класса BooksCollector
- `tests.py` - тесты для проверки функциональности
- `conftest.py` - фикстуры для подготовки тестовых данных
- `README.md` - документация по тестам

## Реализованные тесты

### 1. Тесты для метода `add_new_book`
- **test_add_new_book_add_two_books** - проверка добавления двух книг
- **test_add_new_book_name_length_validation** - параметризованный тест валидации длины названия книги
  - Проверяет названия длиной 0, 1, 40, 41 символ и нормальное название
- **test_add_new_book_duplicate_not_added** - проверка защиты от дубликатов
- **test_add_new_book_no_genre_by_default** - проверка отсутствия жанра по умолчанию

### 2. Тесты для метода `set_book_genre`
- **test_set_book_genre_valid_genre** - параметризованный тест установки валидных жанров
  - Проверяет все доступные жанры: Фантастика, Ужасы, Детективы, Мультфильмы, Комедии
- **test_set_book_genre_invalid_genre_not_set** - проверка обработки невалидного жанра
- **test_set_book_genre_nonexistent_book** - проверка установки жанра для несуществующей книги

### 3. Тесты для метода `get_book_genre`
- **test_get_book_genre_existing_book** - получение жанра существующей книги
- **test_get_book_genre_nonexistent_book** - получение жанра несуществующей книги

### 4. Тесты для метода `get_books_with_specific_genre`
- **test_get_books_with_specific_genre_existing_genre** - поиск книг по существующему жанру
- **test_get_books_with_specific_genre_invalid_genre** - поиск по невалидному жанру
- **test_get_books_with_specific_genre_empty_collector** - поиск в пустой коллекции

### 5. Тесты для метода `get_books_genre`
- **test_get_books_genre_returns_original_dict** - проверка возврата оригинального словаря

### 6. Тесты для метода `get_books_for_children`
- **test_get_books_for_children_excludes_age_rated_genres** - проверка исключения книг с возрастным рейтингом
- **test_get_books_for_children_no_books_without_genre** - проверка исключения книг без жанра
- **test_get_books_for_children_empty_collection** - проверка пустой коллекции

### 7. Тесты для метода `add_book_in_favorites`
- **test_add_book_in_favorites_valid_book** - добавление валидной книги в избранное
- **test_add_book_in_favorites_duplicate_not_added** - защита от дубликатов в избранном
- **test_add_book_in_favorites_nonexistent_book** - добавление несуществующей книги в избранное

### 8. Тесты для метода `delete_book_from_favorites`
- **test_delete_book_from_favorites_existing_book** - удаление существующей книги из избранного
- **test_delete_book_from_favorites_nonexistent_book** - удаление несуществующей книги из избранного

### 9. Тесты для метода `get_list_of_favorites_books`
- **test_get_list_of_favorites_books_returns_original_list** - проверка возврата оригинального списка
- **test_get_list_of_favorites_books_empty** - проверка пустого списка избранного

## Фикстуры

### `collector`
Базовый экземпляр BooksCollector для тестов

### `collector_with_books`
BooksCollector с предварительно добавленными книгами различных жанров:
- Книга 1 (Фантастика)
- Книга 2 (Ужасы) 
- Книга 3 (Детективы)
- Книга 4 (Мультфильмы)
- Книга 5 (Комедии)
- Книга 6 (без жанра)

### `collector_with_favorites`
BooksCollector с книгами в избранном:
- Книга 1
- Книга 2  
- Книга 3

## Запуск тестов
```bash
pytest -v tests.py
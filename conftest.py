import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    # Базовый экземпляр BooksCollector для тестов
    return BooksCollector()


@pytest.fixture
def collector_with_books():
    # BooksCollector с предварительно добавленными книгами
    collector = BooksCollector()
    books = [
        ('Книга 1', 'Фантастика'),
        ('Книга 2', 'Ужасы'),
        ('Книга 3', 'Детективы'),
        ('Книга 4', 'Мультфильмы'),
        ('Книга 5', 'Комедии'),
        ('Книга 6', '')  # без жанра
    ]
    for name, genre in books:
        collector.add_new_book(name)
        if genre:
            collector.set_book_genre(name, genre)
    return collector


@pytest.fixture
def collector_with_favorites():
    # BooksCollector с книгами в избранном
    collector = BooksCollector()
    books = ['Книга 1', 'Книга 2', 'Книга 3']
    for book in books:
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
    return collector
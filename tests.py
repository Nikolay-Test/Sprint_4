import pytest
from main import BooksCollector


class TestBooksCollector:

    # Тесты для add_new_book
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('book_name, expected', [
        ('Книга с очень длинным названием которое превышает лимит в 40 символов', False),
        ('Нормальная книга', True),
        ('', False),  # пустое название
        ('К', True),  # 1 символ
        ('К' * 40, True),  # 40 символов
        ('К' * 41, False),  # 41 символ
    ])
    def test_add_new_book_name_length_validation(self, collector, book_name, expected):
        collector.add_new_book(book_name)
        assert (book_name in collector.get_books_genre()) == expected

    def test_add_new_book_duplicate_not_added(self, collector):
        collector.add_new_book('Дубликат')
        collector.add_new_book('Дубликат')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_no_genre_by_default(self, collector):
        collector.add_new_book('Книга без жанра')
        assert collector.get_book_genre('Книга без жанра') == ''

    # Тесты для set_book_genre
    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_valid_genre(self, collector, genre):
        collector.add_new_book('Тестовая книга')
        collector.set_book_genre('Тестовая книга', genre)
        assert collector.get_book_genre('Тестовая книга') == genre

    def test_set_book_genre_invalid_genre_not_set(self, collector):
        collector.add_new_book('Тестовая книга')
        collector.set_book_genre('Тестовая книга', 'Несуществующий жанр')
        assert collector.get_book_genre('Тестовая книга') == ''

    def test_set_book_genre_nonexistent_book(self, collector):
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert 'Несуществующая книга' not in collector.get_books_genre()

    # Тесты для get_book_genre
    def test_get_book_genre_existing_book(self, collector_with_books):
        assert collector_with_books.get_book_genre('Книга 1') == 'Фантастика'

    def test_get_book_genre_nonexistent_book(self, collector):
        assert collector.get_book_genre('Несуществующая книга') is None

    # Тесты для get_books_with_specific_genre
    def test_get_books_with_specific_genre_existing_genre(self, collector_with_books):
        books = collector_with_books.get_books_with_specific_genre('Фантастика')
        assert 'Книга 1' in books
        assert len(books) == 1

    def test_get_books_with_specific_genre_invalid_genre(self, collector_with_books):
        books = collector_with_books.get_books_with_specific_genre('Несуществующий жанр')
        assert books == []

    def test_get_books_with_specific_genre_empty_collector(self, collector):
        books = collector.get_books_with_specific_genre('Фантастика')
        assert books == []

    # Тесты для get_books_genre
    def test_get_books_genre_returns_original_dict(self, collector):
        # Проверяем, что метод возвращает оригинальный словарь (не копию)
        collector.add_new_book('Книга')
        books_genre = collector.get_books_genre()
        # Проверяем, что изменения в возвращенном объекте влияют на оригинал
        books_genre['Изменение'] = 'Жанр'
        assert 'Изменение' in collector.get_books_genre()

    # Тесты для get_books_for_children
    def test_get_books_for_children_excludes_age_rated_genres(self, collector_with_books):
        children_books = collector_with_books.get_books_for_children()
        assert 'Книга 2' not in children_books  # Ужасы - с возрастным рейтингом
        assert 'Книга 3' not in children_books  # Детективы - с возрастным рейтингом
        assert 'Книга 1' in children_books  # Фантастика - без рейтинга
        assert 'Книга 4' in children_books  # Мультфильмы - без рейтинга
        assert 'Книга 5' in children_books  # Комедии - без рейтинга

    def test_get_books_for_children_no_books_without_genre(self, collector_with_books):
        children_books = collector_with_books.get_books_for_children()
        assert 'Книга 6' not in children_books  # Книга без жанра не должна попасть

    def test_get_books_for_children_empty_collection(self, collector):
        assert collector.get_books_for_children() == []

    # Тесты для add_book_in_favorites
    def test_add_book_in_favorites_valid_book(self, collector):
        collector.add_new_book('Книга для избранного')
        collector.add_book_in_favorites('Книга для избранного')
        assert 'Книга для избранного' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_duplicate_not_added(self, collector):
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.add_book_in_favorites('Книга')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_nonexistent_book(self, collector):
        collector.add_book_in_favorites('Несуществующая книга')
        assert 'Несуществующая книга' not in collector.get_list_of_favorites_books()

    # Тесты для delete_book_from_favorites
    def test_delete_book_from_favorites_existing_book(self, collector_with_favorites):
        collector_with_favorites.delete_book_from_favorites('Книга 1')
        assert 'Книга 1' not in collector_with_favorites.get_list_of_favorites_books()

    def test_delete_book_from_favorites_nonexistent_book(self, collector_with_favorites):
        initial_favorites = collector_with_favorites.get_list_of_favorites_books().copy()
        collector_with_favorites.delete_book_from_favorites('Несуществующая книга')
        assert collector_with_favorites.get_list_of_favorites_books() == initial_favorites

    # Тесты для get_list_of_favorites_books
    def test_get_list_of_favorites_books_returns_original_list(self, collector_with_favorites):
        # Проверяем, что метод возвращает оригинальный список (не копию)
        favorites = collector_with_favorites.get_list_of_favorites_books()
        # Проверяем, что изменения в возвращенном объекте влияют на оригинал
        favorites.append('Новая книга')
        assert 'Новая книга' in collector_with_favorites.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_empty(self, collector):
        assert collector.get_list_of_favorites_books() == []
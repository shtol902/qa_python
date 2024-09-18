import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_init_books_genre_empty(self):
        collector = BooksCollector()
        assert collector.books_genre == {}

    def test_init_favorites_empty(self):
        collector = BooksCollector()
        assert collector.favorites == []

    def test_init_genre_have_data(self):
        collector = BooksCollector()
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_init_genre_age_rating_have_data(self):
        collector = BooksCollector()
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_add_new_book_with_name_less_40_symbol(self):
        collector = BooksCollector()
        collector.add_new_book('Луна и грош')
        assert 'Луна и грош' in collector.books_genre

    def test_add_new_book_with_empty_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert '' not in collector.books_genre

    def test_add_new_book_with_name_more_40_symbol(self):
        collector = BooksCollector()
        long_name = '100 советов мэру. Книга рецептов хорошего города'
        collector.add_new_book(long_name)
        assert long_name not in collector.books_genre

    def test_add_new_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Луна и грош')
        collector.add_new_book('Луна и грош')
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize('book1, book2', [('Белые ночи', 'Знак четырех')])
    def test_add_new_book_add_two_books(self, book1, book2):
        collector = BooksCollector()
        collector.add_new_book(book1)
        collector.add_new_book(book2)
        assert len(collector.books_genre) == 2

    def test_set_book_genre_success(self):
        collector = BooksCollector()
        book_name = "Знак четырех"
        genre = "Детективы"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre[book_name] == genre

    def test_set_book_genre_book_not_in_books_genre(self):
        collector = BooksCollector()
        book_name = "Знак четырех"
        genre = "Детективы"
        collector.set_book_genre(book_name, genre)
        assert book_name not in collector.books_genre

    def test_set_genre_book_not_in_genre(self):
        collector = BooksCollector()
        book_name = "Луна и грош"
        genre = "Роман"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre[book_name] == ""

    def test_get_book_genre_success(self):
        collector = BooksCollector()
        book_name = "Десять негритят"
        genre = "Детективы"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_books_with_specific_genre_success(self):
        collector = BooksCollector()

        collector.add_new_book("Понедельник начинается в субботу")
        collector.set_book_genre("Понедельник начинается в субботу", "Фантастика")

        collector.add_new_book("Десять негритят")
        collector.set_book_genre("Десять негритят", "Детективы")

        collector.add_new_book("Трудно быть богом")
        collector.set_book_genre("Трудно быть богом", "Фантастика")

        books_with_fantasy_genre = collector.get_books_with_specific_genre("Фантастика")
        assert books_with_fantasy_genre == ["Понедельник начинается в субботу", "Трудно быть богом"]

    @pytest.mark.parametrize("books_and_genres, expected_books_genre", [
        ({"Трудно быть богом": "Фантастика", "Знак четырех": "Детективы"},
         {"Трудно быть богом": "Фантастика", "Знак четырех": "Детективы"})
    ])
    def test_get_books_genre_success(self, books_and_genres, expected_books_genre):
        collector = BooksCollector()

        for book, genre in books_and_genres.items():
            collector.add_new_book(book)
            if genre:
                collector.set_book_genre(book, genre)

        assert collector.get_books_genre() == expected_books_genre

    def test_get_books_for_children_success(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        collector.add_new_book("Знак четырех")
        collector.set_book_genre("Знак четырех", "Детективы")
        expected_books_for_children = ["Гарри Поттер"]
        books_for_children = collector.get_books_for_children()
        assert books_for_children == expected_books_for_children

    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book("Трудно быть богом")
        collector.set_book_genre("Трудно быть богом", "Фантастика")
        collector.add_book_in_favorites("Трудно быть богом")
        assert "Трудно быть богом" in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book("Трудно быть богом")
        collector.set_book_genre("Трудно быть богом", "Фантастика")
        collector.add_book_in_favorites("Трудно быть богом")
        collector.delete_book_from_favorites("Трудно быть богом")
        assert "Трудно быть богом" not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_success(self):
        collector = BooksCollector()
        collector.add_new_book("Трудно быть богом")
        collector.set_book_genre("Трудно быть богом", "Фантастика")
        collector.add_book_in_favorites("Трудно быть богом")
        favorites_list = collector.get_list_of_favorites_books()
        assert sorted(favorites_list) == ["Трудно быть богом"]
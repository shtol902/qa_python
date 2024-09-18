# Автотесты 
## init
В первую очередь нужно протестировать метод __init__, для этого нужно проверить каждое из полей

## add_new_book
1) Добавление книги с названием менее 40 символов. Название книги может содержать максимум 40 символов.
2) Добавление книги с пустым названием.
3) Добавление книги с названием более 40 символов.
4) Добавление книги с одним названием дважды. Одну и ту же книгу можно добавить только один раз.
5) Добавление двух книг с праметризацией.

## set_book_genre
1) Добавление жанра для книги, которая уже добавлена в словарь.
2) Добавление жанра для книги, которой нет в словаре.
3) Неудачное добавление жанра. Жанр не входит в список.

## get_book_genre
Успешное получение жанра.

## get_books_with_specific_genre
Успешное получение списока книг с определённым жанром.

## get_books_genre
Успешный вывод текущего словаря.

## get_books_for_children
Успешно возвращает книги, которые подходят детям.

## add_book_in_favorites
Успешно добавляет книгу в избранное.

## delete_book_from_favorites
Успешно удаляет книгу из избранного.

## get_list_of_favorites_books
Успешное получение списка избранных книг.

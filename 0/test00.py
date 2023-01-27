books = [
	{
		'название': '1',
		'автор': '1_1',
		'год издания': 1900,
	},
	{
		'название': '2',
		'автор': '2_1',
		'год издания': 1910,
	}
]


def hub(books: list):
	print('Библиотека деревни «Гадюкино»:  ')
	print()
	print('')


def show_all(books: list):
	for num, book in enumerate(books, 1):
		print(
			f'номер на полке: {num}'
		)
		print(
			f'название: {book["название"]}'
		)
		print(
			f'автор: {book["автор"]}'
		)
		print(
			f'год издания: {book["год издания"]}'
		)
		print()

def show_one(books: list):
	c_book = input("какую книгу показать? ")
	
	print(
		f'номер на полке: {books.index(c_book)}'
	)
	print(
		f'название: {books[c_book]["название"]}'
	)
	print(
		f'автор: {books[c_book]["автор"]}'
	)
	print(
		f'год издания: {books[c_book]["год издания"]}'
	)
	print()

def add_book(books: list):
	title = input('введите название книги: ')
	if not title:
		print('введите название')
		return hub(books)

	name = input('введите автора книги: ')
	if not name:
		print('введите имя автора')
		return hub(books)

	year = input('введите год издания книги: ')
	if year.isdigit():
		year = int(year)
	else: 
		print('введите число!')
		return hub(books)

	book = {
		'название': title,
		'автор': name,
		'год издания': year,
		}

	if book in books:
		print('Такая книга уже есть!')
		return hub(books)

	books.append(book)

def del_book(books: list):
	c_book = input('введите номер книги, которую нужно удалить: ')#принимает > 0
	books.pop(c_book)
	if year.isdigit() and c_book > 0:
		year = int(year)

def name_s(books:list):
	name = input('введите название книги: ')
	for book in books:
		if 'название' == name:
			print(
				'номер на полке: {}'
			)
			print(
				f'название: {books[c_book]["название"]}'
			)
			print(
				f'автор: {books[c_book]["автор"]}'
			)
			print(
				f'год издания: {books[c_book]["год издания"]}'
			)
			print()

show_one(books)
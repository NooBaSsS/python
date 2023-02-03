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


def hub() -> None:
	print()
	print('Библиотека деревни «Гадюкино»:  ')
	a = ['Показать все книги', 
		'Показать книгу', 
		'Добавить книгу', 
		'Удалить книгу', 
		'Найти книгу по названию',
		'Найти книгу по автору',
		'Найти книгу по году',
		'Найти книгу по порядковому номеру',
	]
	for b in enumerate(a, 1):
		print(f'{b[0]})', b[1])

	u_c = input('введите номер действия: ')
	if u_c.isdigit():
		u_c = int(u_c)

	if u_c == 1:
		return show_all(books)
	if u_c == 2:
		return show_one(books)
	if u_c == 3:
		return add_book(books)
	if u_c == 4:
		return del_book(books)
	if u_c == 5:
		return s_b_key('название')
	if u_c == 6:
		return s_b_key('автор')
	if u_c == 7:
		return s_b_key('год издания')
	if u_c == 8:
		return s_b_num(books)

def show_all(books: list) -> None:
	if not books:
		print('библиотека пуста')
		return

	for num, book in enumerate(books, 1):
		print()
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
	return hub()

def show_one(books: list) -> None:
	num = input('введите порядковый номер книги: ')
	if not num.isdigit():
		print('введите число!')
		return hub()
	num = int(num)
	idx = num - 1
	if idx < 0:
		print('число должно быть положительным')
		return hub()
	if idx >= len(books):
		print('такой книги нет')
		return hub()
	book = books[idx]
		
	
	print(
		f'номер на полке: {books.index(book) + 1}'
	)
	print(
		f'название: {books[book]["название"]}'
	)
	print(
		f'автор: {books[book]["автор"]}'
	)
	print(
		f'год издания: {books[book]["год издания"]}'
	)
	print()
	return hub()

def add_book(books: list) -> None:
	title = input('введите название книги: ')
	if not title:
		print('введите название')
		return hub()

	name = input('введите автора книги: ')
	if not name:
		print('введите имя автора')
		return hub()

	year = input('введите год издания книги: ')
	if year.isdigit():
		year = int(year)
	else: 
		print('введите число!')
		return hub()

	book = {
		'название': title,
		'автор': name,
		'год издания': year,
		}

	if book in books:
		print('Такая книга уже есть!')
		return hub()

	books.append(book)
	print(f"книга {book['название']} добавлена")
	return hub()

def del_book(books: list) -> None:
	if not books:
		print('библиотека пуста')
		return
	c_book = input('введите номер книги, которую нужно удалить: ')#принимает > 0

	if c_book.isdigit():
		c_book = int(c_book)
	else: 
		print('введите число!')
		return hub()

	idx = c_book - 1

	if idx < 0 or idx >= len(books):
		print("неправильное число")
		return hub()
	
	print(f'книга {books[idx]["название"]} удалена')
	books.pop(idx)
	return hub()
	
def s_b_num(books:list) -> None:
	if not books:
		print('библиотека пуста')
		return hub()
	num = input('введите порядковый номер книги: ')
	if not num.isdigit():
		print('введите число!')
		return hub()
	num = int(num)
	idx = num - 1
	if idx < 0:
		print('число должно быть положительным')
		return hub()
	if idx >= len(books):
		print('такой книги нет')
		return hub()
	book = books[idx]
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
	return hub()

def s_b_key(u_key: str) -> None:
	if not books:
		print('библиотека пуста')
		return hub()
	u_val = input(f'введите {u_key}: ')
	if not u_val:
		print(f'введите {u_key}')
		return hub()
	if u_key == 'год издания':
		if u_val.isdigit():
			u_val = int(u_val)
	for book in books:
		if book[u_key] == u_val:
			print(
				f'номер на полке: {books.index(book) + 1}'
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
	return hub()

hub()

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


def hub(books: list) -> None:
	print('Библиотека деревни «Гадюкино»:  ')
	print()
	print('')



def show_all(books: list) -> None:
	if not books:
		print('библиотека пуста')
		return

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


def show_one(books: list) -> None:
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

def add_book(books: list) -> None:
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
	print(f"книга {book['название']} добавлена")


def del_book(books: list) -> None:
	if not books:
		print('библиотека пуста')
		return
	c_book = input('введите номер книги, которую нужно удалить: ')#принимает > 0

	if c_book.isdigit():
		c_book = int(c_book)
	else: 
		print('введите число!')
		return hub(books)

	idx = c_book - 1

	if idx < 0 or idx >= len(books):
		print("неправильное число")
		return hub(books)
	
	print(f'книга {books[idx]["название"]} удалена')
	books.pop(idx)
	
	
def s_b_num(books:list) -> None:
	if not books:
		print('библиотека пуста')
		return
	num = input('введите порядковый номер книги: ')
	if not num:
		print('введите целое число')
		return hub(books)
	if num.isdigit():
		num = int(num)
	else: 
		print('введите число!')
		return hub(books)
	if num <= 0 or num >= len(books):
		print("неправильное число")
		return hub(books)
	


show_all(books)
s_b_num(books)
show_all(books)
import os
from sys import exit

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
	},
	{
		'название': '3',
		'автор': '1_1',
		'год издания': 1900,
	},
	{
		'название': '4',
		'автор': '1_1',
		'год издания': 1900,
	}


]


def hub() -> None:
	os.system('cls')
	print('Библиотека деревни «Гадюкино»:  ')
	print()
	options = [
		('Показать все книги', lambda: show_all()),
		('Добавить книгу', lambda: add_book()),
		('Удалить книгу', lambda: del_book()),
		('Найти книгу по названию', lambda: s_b_key('название')),
		('Найти книгу по автору', lambda: s_b_key('автор')),
		('Найти книгу по году', lambda: s_b_key('год издания')),
		('Найти книгу по порядковому номеру', lambda: s_b_num()),
		('Выход', lambda: close())
	]

	for i, option in enumerate(options, 1):
		print(f'{i}) {option[0]}')
	
	option = input('Введите номер варианта: ')
	if not option.isdigit():
		print('Введите число')
		input('нажмите ENTER для продолжения')
		return hub()
	if not option:
		print('введите число!')
		input('нажмите ENTER для продолжения')
		return hub()
	idx = int(option) - 1
	if idx + 1 > len(options):
		print('слишком большое число')
		input('нажмите ENTER для продолжения')
		return hub()
	options[idx][1]()

def show_all() -> None:
	if not books:
		print('библиотека пуста')
		return

	for num, book in enumerate(books, 1):
		print()
		print(f'номер на полке: {num}')
		print(f'название: {book["название"]}')
		print(f'автор: {book["автор"]}')
		print(f'год издания: {book["год издания"]}')
		print()
	input('нажмите ENTER для продолжения')
	return hub()

def show_book(book: dict) -> None:
	idx = books.index(book)
	print(
		f'номер на полке: {books.index(book) + 1}'
	)
	print(
		f'название: {books[idx]["название"]}'
	)
	print(
		f'автор: {books[idx]["автор"]}'
	)
	print(
		f'год издания: {books[idx]["год издания"]}'
	)

def show_one() -> None:
	num = input('введите порядковый номер книги: ')
	if not num.isdigit():
		print('введите число!')
		input("Нажмите ENTER чтобы продолжить")
		return hub()
	num = int(num)
	idx = num - 1
	if idx < 0:
		print('число должно быть положительным')
		input('нажмите ENTER для продолжения')
		return hub()
	if idx >= len(books):
		print('такой книги нет')
		input('нажмите ENTER для продолжения')
		return hub()
	book = books[idx]
	idx_ = books.index(book)
	
	show_book(idx_)
	print()
	input('нажмите ENTER для продолжения')
	return hub()

def add_book() -> None:
	title = input('введите название книги: ')
	if not title:
		print('введите название')
		input('нажмите ENTER для продолжения')
		return hub()

	name = input('введите автора книги: ')
	if not name:
		print('введите имя автора')
		input('нажмите ENTER для продолжения')
		return hub()

	year = input('введите год издания книги: ')
	if year.isdigit():
		year = int(year)
	else: 
		print('введите число!')
		input('нажмите ENTER для продолжения')
		return hub()

	book = {
		'название': title,
		'автор': name,
		'год издания': year,
		}

	if book in books:
		print('Такая книга уже есть!')
		input('нажмите ENTER для продолжения')
		return hub()

	books.append(book)
	print(f"книга {book['название']} добавлена")
	input('нажмите ENTER для продолжения')
	return hub()

def del_book() -> None:
	if not books:
		print('библиотека пуста')
		return
	c_book = input('введите номер книги, которую нужно удалить: ')#принимает > 0

	if c_book.isdigit():
		c_book = int(c_book)
	else: 
		print('введите число!')
		input('нажмите ENTER для продолжения')
		return hub()

	idx = c_book - 1

	if idx < 0 or idx >= len(books):
		print("неправильное число")
		input('нажмите ENTER для продолжения')
		return hub()
	
	print(f'книга {books[idx]["название"]} удалена')
	books.pop(idx)
	input('нажмите ENTER для продолжения')
	return hub()
	
def s_b_num() -> None:
	if not books:
		print('библиотека пуста')
		input('нажмите ENTER для продолжения')
		return hub()
	num = input('введите порядковый номер книги: ')
	if not num.isdigit():
		print('введите число!')
		input('нажмите ENTER для продолжения')
		return hub()
	num = int(num)
	idx = num - 1
	if idx < 0:
		print('число должно быть положительным')
		input('нажмите ENTER для продолжения')
		return hub()
	if idx >= len(books):
		print('такой книги нет')
		input('нажмите ENTER для продолжения')
		return hub()
	book = books[idx]
	print()
	show_book(book)
	print()
	input('нажмите ENTER для продолжения')
	return hub()

def s_b_key(u_key: str) -> None:
	if not books:
		print('библиотека пуста')
		input('нажмите ENTER для продолжения')
		return hub()
	u_val = input(f'введите {u_key}: ')
	if not u_val:
		print(f'введите {u_key}')
		input('нажмите ENTER для продолжения')
		return hub()
	if u_key == 'год издания':
		if u_val.isdigit():
			u_val = int(u_val)

	found_books = []
	for book in books:
		if book[u_key] == u_val:
			found_books.append(book)
	
	if not found_books:
		print('книг не найдено')
		input('нажмите ENTER для продолжения')
		return hub()

	for book in found_books:
		print()
		show_book(book)



			
	input('нажмите ENTER для продолжения')
	return hub()

def close() -> None:
	print('ы')
	exit()

hub()

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


def show_all(books: list):
	for book in books:
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
	c_book = int(input("какую книгу показать? "))
	
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
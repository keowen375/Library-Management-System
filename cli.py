# cli.py

import click
from models import Session, Author, Book

@click.group()
def cli():
    pass
@cli.command()
@click.argument('book_id', type=int)
def delete_book(book_id):
    session = Session()
    book = session.query(Book).get(book_id)
    if book:
        session.delete(book)
        session.commit()
        session.close()
        print(f'Deleted book: {book.title}')
    else:
        print(f'Book with id {book_id} not found')

@cli.command()
@click.argument('author_id', type=int)
def delete_author(author_id):
    session = Session()
    author = session.query(Author).get(author_id)
    if author:
        session.delete(author)
        session.commit()
        session.close()
        print(f'Deleted author: {author.name}')
    else:
        print(f'Author with id {author_id} not found')
        
@cli.command()
@click.argument('name')
def add_author(name):
    session = Session()
    author = Author(name=name)
    session.add(author)
    session.commit()
    session.close()
    print(f'Added author: {name}')

@cli.command()
@click.argument('title')
@click.argument('author_id', type=int)
def add_book(title, author_id):
    session = Session()
    author = session.query(Author).get(author_id)
    if author:
        book = Book(title=title, author=author)
        session.add(book)
        session.commit()
        session.close()
        print(f'Added book: {title} by {author.name}')
    else:
        print(f'Author with id {author_id} not found')

@cli.command()
def list_books():
    session = Session()
    books = session.query(Book).all()
    session.close()
    if books:
        for book in books:
            print(f'Book: {book.title}, Author: {book.author.name}')
    else:
        print('No books found')

if __name__ == '__main__':
    cli()

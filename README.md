# Library-Management-System
# Library-Management-System

This is a command-line interface (CLI) application for managing a library with books and authors. It allows you to add, list, and delete books and authors from a database.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Contributing](#contributing)
- [License](#license)

## Features

- Add authors to the library.
- Add books to the library and associate them with authors .
- List all books in the library.
- Delete books and authors from the library.

## Installation

To run this CLI application, you'll need Python and Pipenv installed on your system .

1. Clone the repository:

   ```bash
   git clone git@github.com:keowen375/Library-Management-System.git
   cd Library-Management-System

    Create a virtual environment and install dependencies using Pipenv:

    bash

pipenv install

Activate the virtual environment:

bash

pipenv shell

Create the SQLite database and tables:

bash

    python models.py

Usage

Once you have set up the environment, you can use the CLI to manage your library.
Adding an Author.

To add an author to the library, use the add_author command:

bash

python cli.py add_author "Author Name"

Replace "Author Name" with the name of the author you want to add.

*Adding a Book*
To add a book to the library and associate it with an author, use the add_book command:

bash

python cli.py add_book "Book Title" author_id

Replace "Book Title" with the title of the book and author_id with the ID of the author.
Listing Books

To list all books in the library, use the list_books command:

bash

python cli.py list_books

Deleting a Book

To delete a book from the library, use the delete_book command:

bash

python cli.py delete_book book_id

Replace book_id with the ID of the book you want to delete.
Deleting an Author

To delete an author from the library, use the delete_author command:

bash

python cli.py delete_author author_id

Replace author_id with the ID of the author you want to delete
Contributing


This project is licensed under the MIT License - see the LICENSE file for details.


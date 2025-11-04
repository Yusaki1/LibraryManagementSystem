class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def add_book(self):
        print(f"添加图书：{self.title}（作者：{self.author}）")

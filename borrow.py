class BorrowRecord:
    def __init__(self, record_id, user_id, book_id):
        self.record_id = record_id
        self.user_id = user_id
        self.book_id = book_id

    def create_record(self):
        print(f"创建借阅记录：用户{self.user_id}借阅图书{self.book_id}")

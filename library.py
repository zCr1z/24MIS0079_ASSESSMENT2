class Book:
    def __init__(self, title, author, available_copies, borrowed_count):
        self.title = title
        self.author = author
        self.available_copies = available_copies
        self.borrowed_count = borrowed_count


books = [
    Book("Python Basics", "John", 5, 25),
    Book("Data Science", "Alice", 0, 40),
    Book("AI Handbook", "Bob", 2, 35),
    Book("Machine Learning", "David", 0, 50),
    Book("Algorithms", "Charles", 4, 20),
]
most_borrowed = max(books, key=lambda x: x.borrowed_count)

print("Most Borrowed Book")
print(f"{most_borrowed.title} ({most_borrowed.borrowed_count} times)")
print("\nBooks with Zero Available Copies")
for book in books:
    if book.available_copies == 0:
        print(book.title)
total = sum(book.available_copies for book in books)
print("\nTotal Available Books:", total)
books.sort(key=lambda x: x.borrowed_count, reverse=True)

print("\nBooks Sorted by Popularity")
for book in books:
    print(f"{book.title} - Borrowed {book.borrowed_count} times")
print("\nLibrary Summary Report")
for book in books:
    print(f"Title: {book.title}")
    print(f"Author: {book.author}")
    print(f"Available Copies: {book.available_copies}")
    print(f"Borrowed Count: {book.borrowed_count}")
    print("-" * 30)

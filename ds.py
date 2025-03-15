books = []  

books.append(("101", "Bangla", "michale modhu"))
books.append(("102", "English", "George bush"))
books.append(("103", "Data Structure", "andrew"))
books.append(("104", "DBMS", "stan lee"))


for book in books:
    print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}")

members = {
    "M001": {"name": "Fahim", "borrowed_books": ["101","103"]},
    "M002": {"name": "Raisul", "borrowed_books": ["102", "103","104"]}
}

member_id = "M002"
print(f"Member Name: {members[member_id]['name']}")
print(f"Borrowed Books: {members[member_id]['borrowed_books']}")

book1 = ("101", "bangla", "william carry")
book2 = ("102", "History", "sayed abu mia")
book3 = ("103", "Computer programming I", "henry duke")
book4 = ("104", "Computer Programming II", "klassan smith")

print(book1)
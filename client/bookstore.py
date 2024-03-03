import grpc
import bookstore_pb2
import bookstore_pb2_grpc

def run():
	with grpc.insecure_channel('localhost:50051') as channel:
		stub = bookstore_pb2_grpc.BookServiceStub(channel)

		# Menambahkan buku baru
		print("Adding new book...")
		new_book = stub.AddBook(bookstore_pb2.Book(
			title="Learning gRPC",
			author="Habibie",
			isbn="12345",
			price=39.99
		))
		print(f"Added book: {new_book.id}\n")

		# Mendapatkan detail buku
		print("Getting book details...")
		book = stub.GetBook(bookstore_pb2.GetBookRequest(id=new_book.id))
		print(f"Book Details: ID={book.id}, Title={book.title}, Author={book.author}, ISBN={book.isbn}, Price={book.price}\n")

		# Menampilkan semua buku
		print("Listing all books...")
		books = stub.ListBooks(bookstore_pb2.Empty())
		for book in books.books:
			print(f"ID={book.id}, Title={book.title}, Author={book.author}, ISBN={book.isbn}, Price={book.price}")
		print()

		# Menghapus buku
		print("Deleting a book...")
		delete_response = stub.DeleteBook(bookstore_pb2.DeleteBookRequest(id=new_book.id))
		if delete_response.success:
			print(f"Book with ID {new_book.id} has been deleted.\n")
		else:
			print(f"Failed to delete book with ID {new_book.id}.\n")

if __name__=='__main__':
	run()

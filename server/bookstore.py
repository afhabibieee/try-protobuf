import grpc
from concurrent import futures
import bookstore_pb2
import bookstore_pb2_grpc
import uuid


class BookService(bookstore_pb2_grpc.BookServiceServicer):
	def __init__(self):
		self.books = {}

	def AddBook(self, request, context):
		book_id = str(uuid.uuid4())
		new_book = bookstore_pb2.Book(
			id=book_id,
			title=request.title,
			author=request.author,
			isbn=request.isbn,
			price=request.price
		)
		self.books[book_id] = new_book
		return new_book

	def GetBook(self, request, context):
		book_id = request.id
		if book_id in self.books:
			return self.books[book_id]
		else:
			context.abort(grpc.StatusCode.NOT_FOUND, "Book not found")

	def DeleteBook(self, request, context):
		book_id = request.id
		if book_id in self.books:
			del self.books[book_id]
			return bookstore_pb2.DeleteBookResponse(
				id=book_id,
				success=True
			)
		else:
			return bookstore_pb2.DeleteBookResponse(
				id=book_id,
				success=False
			)

	def ListBooks(self, request, context):
		all_books = [self.books[book_id] for book_id in self.books]
		print("Sending books:", all_books)
		return bookstore_pb2.ListBooksResponse(
			books=all_books
		)

def serve():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	bookstore_pb2_grpc.add_BookServiceServicer_to_server(BookService(), server)
	server.add_insecure_port('[::]:50051')
	print("Server starting on port 50051...")
	server.start()
	server.wait_for_termination()

if __name__=='__main__':
	serve()

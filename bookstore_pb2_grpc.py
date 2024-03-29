# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import bookstore_pb2 as bookstore__pb2


class BookServiceStub(object):
    """Service untuk mendapatkan buku
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddBook = channel.unary_unary(
                '/bookstore.BookService/AddBook',
                request_serializer=bookstore__pb2.Book.SerializeToString,
                response_deserializer=bookstore__pb2.Book.FromString,
                )
        self.GetBook = channel.unary_unary(
                '/bookstore.BookService/GetBook',
                request_serializer=bookstore__pb2.GetBookRequest.SerializeToString,
                response_deserializer=bookstore__pb2.Book.FromString,
                )
        self.DeleteBook = channel.unary_unary(
                '/bookstore.BookService/DeleteBook',
                request_serializer=bookstore__pb2.DeleteBookRequest.SerializeToString,
                response_deserializer=bookstore__pb2.DeleteBookResponse.FromString,
                )
        self.ListBooks = channel.unary_unary(
                '/bookstore.BookService/ListBooks',
                request_serializer=bookstore__pb2.Empty.SerializeToString,
                response_deserializer=bookstore__pb2.ListBooksResponse.FromString,
                )


class BookServiceServicer(object):
    """Service untuk mendapatkan buku
    """

    def AddBook(self, request, context):
        """Menambahkan buku baru ke sistem
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBook(self, request, context):
        """Mendapatkan detail buku berdasarkan ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteBook(self, request, context):
        """Menghapus buku dari sistem
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListBooks(self, request, context):
        """Menampilkan semua buku
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BookServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddBook': grpc.unary_unary_rpc_method_handler(
                    servicer.AddBook,
                    request_deserializer=bookstore__pb2.Book.FromString,
                    response_serializer=bookstore__pb2.Book.SerializeToString,
            ),
            'GetBook': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBook,
                    request_deserializer=bookstore__pb2.GetBookRequest.FromString,
                    response_serializer=bookstore__pb2.Book.SerializeToString,
            ),
            'DeleteBook': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteBook,
                    request_deserializer=bookstore__pb2.DeleteBookRequest.FromString,
                    response_serializer=bookstore__pb2.DeleteBookResponse.SerializeToString,
            ),
            'ListBooks': grpc.unary_unary_rpc_method_handler(
                    servicer.ListBooks,
                    request_deserializer=bookstore__pb2.Empty.FromString,
                    response_serializer=bookstore__pb2.ListBooksResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'bookstore.BookService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BookService(object):
    """Service untuk mendapatkan buku
    """

    @staticmethod
    def AddBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bookstore.BookService/AddBook',
            bookstore__pb2.Book.SerializeToString,
            bookstore__pb2.Book.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bookstore.BookService/GetBook',
            bookstore__pb2.GetBookRequest.SerializeToString,
            bookstore__pb2.Book.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bookstore.BookService/DeleteBook',
            bookstore__pb2.DeleteBookRequest.SerializeToString,
            bookstore__pb2.DeleteBookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListBooks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bookstore.BookService/ListBooks',
            bookstore__pb2.Empty.SerializeToString,
            bookstore__pb2.ListBooksResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

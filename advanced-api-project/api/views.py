from rest_framework import permissions

class BookListView(...):
    permission_classes = [permissions.AllowAny]  #  Open to all

class BookDetailView(...):
    permission_classes = [permissions.AllowAny]  #  Open to all

class BookCreateView(...):
    permission_classes = [permissions.IsAuthenticated]  # Auth only

class BookUpdateView(...):
    permission_classes = [permissions.IsAuthenticated]  #  Auth only

class BookDeleteView(...):
    permission_classes = [permissions.IsAuthenticated]  #  Auth only

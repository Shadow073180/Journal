from .models import Journal, Entry
from .serializers import JournalSerializer, EntrySerializer
from rest_framework import viewsets

class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
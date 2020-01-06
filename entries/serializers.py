from rest_framework import serializers
from .models import Journal, Entry

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ['id', 'name', 'author']
        depth = 1
       


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id', 'entry_text', 'date_time', 'journal']
# notesapp - views.py
from django.views.generic import ListView
from notesapp.models import NotesDB

class NotesListView( ListView ) :
    model = NotesDB
    queryset = NotesDB.objects.all().order_by("-modified_at")
    template_name = "notesapp/notes.html"

    # Add or modify list-item dictionary fields here
    def get_context_data(self, **kwargs):
        context = super(NotesListView, self).get_context_data(**kwargs)
        return context
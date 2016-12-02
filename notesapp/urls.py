# notesapp - urls.py - delcygnus
from django.conf.urls import url
from django.views.generic import DetailView

from notesapp.models import NotesDB
from notesapp.views import NotesListView

# Route notesapp urls through these view methods
urlpatterns = [
    url(r'^$', NotesListView.as_view(), name='notes_list' ),
    url(r'^(?P<pk>\d+)$',
        DetailView.as_view( model=NotesDB,
                            template_name='notesapp/note.html' ))
]
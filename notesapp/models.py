# notesapp - models.py
from django.db import models

class NotesDB( models.Model ) :
    title = models.CharField( max_length=80 )
    text = models.TextField( )
    created_at = models.DateTimeField( auto_now_add=True )
    modified_at = models.DateTimeField( auto_now=True )

    def __str__(self) :
        return self.title

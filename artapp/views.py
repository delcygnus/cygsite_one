#   artapp - views.py
from django.shortcuts import render, redirect


bgtiles = [
    "delcyg_green3_tile_512.jpg",
    "delcyg_cloud_tile_edit_512.jpg",
    "delcyg_rockface_tile_512.jpg",
    "delcyg_gray03b_tile_512.jpg",
    "delcyg_blue_tile_512.jpg",
]

art_titles = [
    "Art Piece I",
    "Art Piece II",
    "Art Piece III",
    "Art Piece IV",
    "Art Piece V",
]

art_pieces = [
    "delcyg_spykus2_50ms.gif",
    "delcyg_nail_50ms.gif",
    "delcyg_shark_42ms.gif",
    "ArtGoesHere.png",
    "ArtGoesHere.png",
]

#   URL parsing

def art_strip_ID( request ) :
    #   <WSGIRequest: GET '/art---01'>
    request_s = str( request )
    position = request_s.find( "---" )
    if position < 0 :
        return -1

    position += 3
    id_s = request_s[ position : position + 2 ]
    if id_s.isdigit() == False :
        return -1

    index = int( id_s )
    # Convert base 1 to base 0
    index -= 1
    return index

# Parse http request for art piece number.
#   art---01.html view
def artapp( request ) :
    work_title = 'unknown'
    bgtile = 'static/artapp/img/'
    art_piece = 'static/artapp/img/'
    art_index = art_strip_ID( request )
    # print( "art index is " + str( art_index ) )
    if art_index < 0 or art_index >= 5 :
        return redirect( '/' )

    work_title = art_titles[art_index]
    bgtile += bgtiles[art_index]
    art_piece += art_pieces[art_index]

    return render( request, 'artapp/artapp.html',
        {'work_title' : work_title, 'bgtile' : bgtile, 'piece' : art_piece } )

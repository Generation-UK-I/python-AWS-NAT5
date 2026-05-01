# exercice 5 Function with dictionary
 
def  make_album(artist_name, album_title, tracks=""):
    album = {"artist":artist_name, "album":album_title,"tracks":tracks}
    return album
 
#  "tracks":tracks_songs
#  track_songs= ""
  
# create variable with Function and arguments
album1 = make_album("Rihana","Anti")
print(album1)
# call it in loop
for x,y in album1.items():
    print(y)
 
album2 = make_album("Adele","21")
print(album2)
 
for x,y in album2.items():
    print(y)
 
album3 = make_album("Pink floyd","The wall")
print(album3)
 
for x,y in album3.items():
    print(y)
 
album4 = make_album("Adele","21","13")
print(album4)
 
for x,y in album4.items():
    print(y)
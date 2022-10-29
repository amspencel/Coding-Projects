# Andrew's Song of the Day Generator from his 'Ye' Spotify Playlist
# Made with contributions from Samantha Verdi, code from CS 1112, and viewers like you, thank you!
import random
# random.seed()
input( 'Press enter for your new song: ')
# aesthetically pleasing dashes
print( '-' + "\n" + "-" + "\n" + "-" )
# opens text file with list of songs on playlist and puts them in a list
list = []
with open('spotify_list.txt', 'r') as playlist:
    clean_line = playlist.read().split()
    for line in clean_line:
        list.append( line )
song_of_the_day = random.choice( list )
# opens text file with past chosen songs and puts them in a list
past_songs = []
with open('pastsongs.txt', 'r') as pastlist:
    clean_list = pastlist.read().split()
    for song in clean_list:
        past_songs.append(song)
    if song_of_the_day in past_songs:
        print( "Song already chosen, run again." )
    else:
         with open( 'pastsongs.txt', 'a' ) as l:
            l.write( song_of_the_day + "\n" ) # adds the random song to the text file and creates a new line
            print( "Your song of the day is:", song_of_the_day )

#!/usr/bin/env python3
"""
This program takes command line arguments of a
band/artist name and goes to their rym page.

Later modify this for films and releases as well.

Unfortunately, you cannot make requests on 
rym––they will block you. So some things that could
easily be done by first making a request to check if
it returns a 404 is not possible. 

Usage: 
    Artist Search: rym.py names of artist/band seperated by spaces
    Film Search: rym.py film name of film seperated by spaces

    Conversely if no arguments are given, artist name in clipboard will be searched.

TODO:
    add search for albums/singles/eps/charts/lists/genres/literally anything its pretty easy
    to expand upon.
"""
import sys, pyperclip, webbrowser

def searchFilm(funFilm):
    urlFilm = f'https://rateyourmusic.com/film/{funFilm}'
    return urlFilm
def searchArtist(coolArtist):
    urlArtist = f'https://rateyourmusic.com/artist/{coolArtist}'
    return urlArtist

def searchRym():
    if len(sys.argv) > 1:
        # check if user wants to search for things besides artists
        if (sys.argv[1] == "film"):
            film = '_'.join(sys.argv[2:])
            lowerFilm = film.lower()
            search = searchFilm(lowerFilm)
        else:
            artist = '_'.join(sys.argv[1:])             # join artist name by _ if necessary
            lowerArtist = artist.lower()                # set to lower
            search = searchArtist(lowerArtist)
    else:   
        # if no arguments given just use the clipboard
        artist = pyperclip.paste()                  # paste from clipboard
        splitArtist = artist.split()                # split artist by whitespace
        joinedArtist = '_'.join(splitArtist)        # join by _ if necessary 
        lowerArtist = joinedArtist.lower()          # set to lower
        searchArtist(lowerArtist)

    webbrowser.open(search)                      # search web for artist

def main():
    searchRym()

if __name__ == '__main__':
    main()

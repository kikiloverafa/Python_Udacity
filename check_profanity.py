import urllib.request
from urllib.parse import urlencode

def read_text():
    quotes = open("C:\Python\movie_quotes.txt")
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    text_new = urlencode({'':text_to_check})
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text_new)
    output = connection.read()
    #print(output)
    connection.close()
    if b"true" in output:
        print("Profanity Alert!")
    elif b"false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")
    

read_text()
    

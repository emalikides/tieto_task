# tieto_task
Browser script task.

# Description :

As a user I want use command line tool to parse file of urls and see raw html

Command line tool has options -i <input-file>

Input file is csv file with separator semicolon, example of a file

neti;http://www.neti.ee

google;http://www.google.com

 

CSV first column is name and second is url.

As a user I want to see the raw html in console like this

 

./download.py -i urls.csv

HTML “neti”

<raw html>

HTML “google”

<raw html>

 

option -h will show the help of the script.

If page is not reachable in 3 seconds print "Skipping <url>"

 

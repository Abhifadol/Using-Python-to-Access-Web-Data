##

Reading Web Data From Python
TOTAL POINTS 13


1.Question 1
Which of the following Python data structures is most similar to the value returned in this line of Python:
x = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

(a) dictionary
(b) regular expression
(c) socket
(d) list
(e) file handle

Ans :- file handle

2.Question 2
In this Python code, which line actually reads the data?
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

(a) mysock.recv()
(b) socket.socket()
(c) mysock.close()
(d) mysock.connect()
(e) mysock.send()

Ans :- mysock.recv()

3.Question 3
Which of the following regular expressions would extract the URL from this line of HTML:
<p>Please click <a href="http://www.dr-chuck.com">here</a></p>

(a) href="(.+)"
(b) href=".+"
(c) http://.*
(d) <.*>

Ans :- href="(.+)"

4.Question 4
In this Python code, which line is most like the open() call to read a file:
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

(a) mysock.connect()
(b) import socket
(c) mysock.recv()
(e) mysock.send()
(f) socket.socket()

Ans :- mysock.connect()

5.Question 5
Which HTTP header tells the browser the kind of document that is being returned?

(a) HTML-Document:
(b) Content-Type:
(c) ETag:
(e) Metadata:
(f) Document-Type:

Ans :- Content-Type:

6.Question 6
What should you check before scraping a web site?

(a) That the web site allows scraping
(b) That the web site only has links within the same site
(c) That the web site returns HTML for all pages
(e) That the web site supports the HTTP GET command

Ans :- That the web site allows scraping

7.Question 7
What is the purpose of the BeautifulSoup Python library?

(a) It optimizes files that are retrieved many times
(b) It allows a web site to choose an attractive skin
(c) It animates web operations to make them more attractive
(d) It builds word clouds from web pages
(e) It repairs and parses HTML to make it easier for a program to understand

Ans :- It repairs and parses HTML to make it easier for a program to understand

8.Question 8
What ends up in the "x" variable in the following code:
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
x = soup('a')

(a) A list of all the anchor tags (<a..) in the HTML from the URL
(b) True if there were any anchor tags in the HTML from the URL
(c) All of the externally linked CSS files in the HTML from the URL
(d) All of the paragraphs of the HTML from the URL

Ans :- A list of all the anchor tags (<a..) in the HTML from the URL

9.Question 9
What is the most common Unicode encoding when moving data between systems?

(a) UTF-64
(b) UTF-128
(c) UTF-8
(d) UTF-16
(e) UTF-32

Ans :- UTF-8

10.Question 10
What is the decimal (Base-10) numeric value for the upper case letter "G" in the ASCII character set?

(a) 71
(b) 7
(c) 103
(d) 25073
(e) 14

Ans :- 71

11.Question 11
What word does the following sequence of numbers represent in ASCII:
108, 105, 110, 101

(a) ping
(b) tree
(c) lost
(d) line
(e) func

Ans :- line

12.Question 12
How are strings stored internally in Python 3?

(a) UTF-8
(b) Byte Code
(c) EBCDIC
(d) Unicode
(e) ASCII

Ans :- Unicode

13.Question 13
When reading data across the network (i.e. from a URL) in Python 3, what method must be used to convert it to the internal format used by strings?

(a) trim()
(b) upper()
(c) find()
(d) decode()
(e) encode()

Ans :- decode()

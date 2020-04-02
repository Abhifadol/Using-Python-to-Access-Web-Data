##

1.Question 1
What is "serialization" when we are talking about web services?

(a) The act of taking data stored in a program and formatting it so it can be sent across the network
(b) Marking each network packet so it can be put back into order on the receiving system
(c) Sorting all the data stored in a tuple
(d) Making it so that dictionaries can maintain their keys in sorted order

Ans :- The act of taking data stored in a program and formatting it so it can be sent across the network

2.Question 2
What is the method to cause Python to parse XML that is stored in a string?

(a) fromstring()
(b) parse()
(c) readall()
(d) extract()
(e) xpath()

Ans :- fromstring()

3.Question 3
In this XML, which are the "simple elements"?
<people>
    <person>
       <name>Chuck</name>
       <phone>303 4456</phone>
    </person>
    <person>
       <name>Noah</name>
       <phone>622 7421</phone>
    </person>
</people>

(a) Noah
(b) name
(c) people
(d) person
(e) phone

Ans :- phone, name

4.Question 4
In the following XML, which are attributes?
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>

(a) type
(b) email
(c) name
(d) person
(e) hide

Ans :- hide, type

5.Question 5
In the following XML, which node is the parent node of node e
<a>
  <b>X</b>
  <c>
    <d>Y</d>
    <e>Z</e>
  </c>
</a>

(a) a
(b) c
(c) b
(d) e

Ans :- c

6.Question 6
Looking at the following XML, what text value would we find at path "/a/c/e"
<a>
  <b>X</b>
  <c>
    <d>Y</d>
    <e>Z</e>
  </c>
</a>

(a) Y
(b) Z
(c) b
(d) e
(e) a

Ans :- Z

7.Question 7
What is the purpose of XML Schema?

(a) To transfer XML data reliably during network outages
(b) To establish a contract as to what is valid XML
(c) A Python program to tranform XML files
(e) To compute SHA1 checksums on data to make sure it is not modified in transit

Ans :- To establish a contract as to what is valid XML

8.Question 8
For this XML Schema:
<xs:complexType name=”person”>
  <xs:sequence>
    <xs:element name="lastname" type="xs:string"/>
    <xs:element name="age" type="xs:integer"/>
    <xs:element name="dateborn" type="xs:date"/>
  </xs:sequence>
</xs:complexType>

And this XML,
<person>
   <lastname>Severance</lastname>
   <Age>17</Age>
   <dateborn>2001-04-17</dateborn>
</person>

Which tag is incorrect?

(a) person
(b) Age
(c) lastname
(d) age
(e) dateborn

Ans :- 

9.Question 9
What does the "Z" mean in this representation of a time:
2002-05-30T09:30:10Z

(a) This time is in the UTC timezone
(b) The hours value is in the range 0-12
(c) The local timezone for this time is New Zealand
(d) This time is Daylight Savings Time

Ans :- This time is in the UTC timezone

10.Question 10
Which of the following dates is in ISO8601 format?

(a) 2002-05-30T09:30:10Z
(b) May 30, 2002
(c) 2002-May-30
(d) 05/30/2002

Ans :- 2002-05-30T09:30:10Z

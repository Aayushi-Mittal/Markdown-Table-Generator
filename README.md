# π Markdown-Table-Generator

> Convert your csv files into markdown syntax easily.

## π CSV Files 
A CSV (comma-separated values) file is a text file that has a specific format which allows data to be saved in a table structured format. Each line of the file is a data record. Each record consists of one or more fields, separated by commas. CSV is human readable and easy to edit manually. It is simple to implement and parse and smaller in size.

## π Markdown Syntax 
Markdown is a lightweight markup language for creating formatted text using a plain-text editor. Markdown allows you to write using an easy-to-read, easy-to-write plain text format, then convert it to structurally valid XHTML (or HTML). Markdown is widely used in blogging, instant messaging, online forums, collaborative software, documentation pages, and readme files.

- **Markdown Syntax for Tables**
  : To add a table, use three or more hyphens (---) to create each columnβs header, and use pipes (|) to separate each column. You can optionally add pipes on either end of the table.

## π Demo 
<p align="center"><img src="https://imgur.com/e8Gnq5j.gif" alt="demo" width=80%></p>

## β¨ Requirements
- python 3

## π How to use?
 - Fork the repository.
 - Open Command Prompt/Terminal and copy-paste the following command and type  ``git clone https://github.com/user-name/Markdown-Table-Generator.git`` to clone the repository on your system. π
 - Now copy paste your csv file to ``Markdown-Table-Generator`` folder. π
 - Run ``Markdown-Table-Generator.py`` on your system and enter the required details- file name and whether you want the contents of the file to be centered or not.
 - Now, check ``table.md`` and copy the text and paste it to .md file to see the output. π
 - Hope, It helped you in some way! π

##### πinput.csv
```
header1,header2,header3
Value1,Value2,Value3
Value1,Value2,Value3
Value1,Value2,Value3
Value1,Value2,Value3
Value1,Value2,Value3
```

##### πtable.md
```
| 	header1	 | 	header2	 | 	header3	 | 
| 	:-----:	 | 	:-----:	 | 	:-----:	 | 
| 	Value1	| 	Value2	| 	Value3	 | 
| 	Value1	| 	Value2	| 	Value3	 | 
| 	Value1	| 	Value2	| 	Value3	 | 
| 	Value1	| 	Value2	| 	Value3	 | 
| 	Value1	| 	Value2	| 	Value3	 | 
```
###### Rendered Output: 
| 	header1	 | 	header2	 | 	header3	 | 
| 	:-----:	 | 	:-----:	 | 	:-----:	 | 
| 	Value1	| 	Value2	| 	Value3	 | 
| 	Value1	| 	Value2	| 	Value3	 | 
| 	Value1	| 	Value2	| 	Value3	 | 
| 	Value1	| 	Value2	| 	Value3	 | 
| 	Value1	| 	Value2	| 	Value3	 | 

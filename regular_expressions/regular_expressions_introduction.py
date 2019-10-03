import re 


def is_legit_integer_string(s):
    k = 0 
    if s[0] in ["+","-"]:
        k += 1 ##skip any sign 
    while k < len(s):
        if not s[k].isdigit():
            return False 
        k += 1
    return True 

def is_legit_integer_string(s):
	seeker = re.compile("^[+\-]?[0-9]+$")
	return bool(seeker.search(s))

for i in ["1","23232","+32","-15","3a","4.5","48."]:
	print(is_legit_integer_string(i))

"""
Re is "the language of character classes

Notes on the Character class:

This is character wildcard 

a-this is the character 'a'/
if a char is not magic (\char) it stands for itself 
[Aaqmx5] any of A,a,q,m,x or 5 (list character class)
[a-z] any of a-z this is a range character class (range is asciigraphical)
[a-zA-Z0-9] any alphanumerical character
[^a-z] anything but a lowercase character (snotty character classes) 
.  is any character except for newline
* postfix unary operator, multiplicity operator (variable)

re is within vim, javascript, and many other languages

magic:
	[      beings list/range cc 
	]      ends list/range cc
	-      indicates a range
	\ 	(toggles magic)


Regular Expressions are character classes glued together 

justaposition: "and them immediately" 

example, type this into unix       grep -E '[abcd][efgh][ijkl][mnop]' path/file

This is saying print all lines which contain one of the letters from each list cc 


Special magic character classes: 

^  <---  means "start of line"  
$  <--- means "end of line" 

Example grep -E '^zyg' path/ file

The following above returns all lines which start with 'zyg' 

Example grep -E 't$' path/file 

The line above returns all lines which end with t 

grep -E '^.a...g.$.' word 

Returns all lines _a___g_


grep -e 'a.*e.*k.*j' path/file 


More Magic Characters: 
	(
	) override orders of ops
	\ toggles magic 
	\. (a period)


example: ^(ab)*$ 

	this means starting with ab and repeating n times 

another postfix unary operator: + one or more times 
				? at most once or zero times




"""






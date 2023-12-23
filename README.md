# wordwrap
sample code for word wrap
wrodwrap.py has function word_wrap 

def word_wrap(para, width) 
// function takes two arguments 
//para : string paragraph input parameter
//width: integer width greater than 0

sample input and output

para = "This is a sample paragraph for testing word_wrap function."
width = 20
expected_output = [
    'This   is  a  sample',
    'paragraph        for',
    'testing    word_wrap',
    'function.           '
    ]

sample test cases written for word_wrap
in testwordwrap.py can be executed

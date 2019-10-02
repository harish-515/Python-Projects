# syntax Errors
print(1)
int(9)
#int 9
int(999)
print(2)
#print 3
print(3)
#a = [1,2,3)
a= [1,2,3]

"""
PS E:\Python-Projects\Python-Projects\ErrorDebugging> python errors.py
  File "errors.py", line 4
    int 9
        ^
SyntaxError: invalid syntax
"""

"""
PS E:\Python-Projects\Python-Projects\ErrorDebugging> python errors.py
  File "errors.py", line 7
    print 3
          ^
SyntaxError: Missing parentheses in call to 'print'. Did
you mean print(3)?
"""
"""
PS E:\Python-Projects\Python-Projects\ErrorDebugging> python errors.py
  File "errors.py", line 9
    a = [1,2,3)
              ^
SyntaxError: invalid syntax
"""

This program allows to check if your passwords have been pwned. 
While starting the program, name of the text file containing passwords have to be given after the name of the py file (in this case:  _"python passwordchecker.py paswwords.txt"_).

Passwords in the text file may be given:
  -with blank spaces between them, 
  -every password in new line,
  -mix of the two methods above.

Program connects with https://api.pwnedpasswords.com/range/ and gives the first 5 symbols of the hashed password (SHA-1).
API return iterable object with all pwned passwords that starts with the same 5 symbols.
Then program checks if our password matches any received password and how many times.
Message with the result is printed in the terminal.

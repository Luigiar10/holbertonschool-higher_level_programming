#!/usr/bin/python3
def remove_char_at(str, n):
       new_string = str
       for i in new_string:
              if i == n:
                     new_string[i].remove()
       return new_string

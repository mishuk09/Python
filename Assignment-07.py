 
"""Assignment-07


Mahadi Hasan Mishuk
 
21SOECE11694

Roll:54

1.   Create an empty dictionary and write a program to add single and multiple elements onto the dictionary.
"""

student_id={
    12:"Mahadi Hasan Mishuk",
    13:"Mahabub Alom"
}
print(student_id.get(12))

"""  2. Operations on Dictionary: copy(), fromkeys(), get(), items(), keys(), values()"""

seq = ('a', 'b', 'c')
print(dict.fromkeys(seq, None))
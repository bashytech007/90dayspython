print("hello world")

name="2pac"
print(name)
name_length=len(name)
print(name_length)

name,name_length="neut",4

print(type(name))
print(type(name_length))

name_length=int("4")
# print(name)

name_length=4
Name_length=5

print(name_length)
print(Name_length)

name_list=["neut","ELCHAPO-007","asd"]
print(type(name_list))

name1,name2,name3=name_list

print(name1)
print(name2)
print(name3)

name_tuple=("neut","ELCHAPO-007")
print(type(name_tuple))

name_dictionary={"neut":4,"Elchapo-007":6}
print(type(name_dictionary))

name_boolean=False
print(type(name_boolean))

name_range=range(6)
print(type(name_range))

name_bytes=b"2pac7"
print(type(name_bytes))
# project day1

print("Hello World")
print(2+2,5*3)
# Numbers
tl_int=1 
print(tl_int)
tl_float=1.0
print(tl_float)
t1_complex=3.14j

print(type(tl_int))
print(type(tl_float))
print(type(t1_complex))
t1_hex=0xa
print(t1_hex)
print(type(t1_hex))
t1_octal=0o10
print(t1_octal)
print(type(t1_octal))

print(1+0x1+0o1)

print(abs(4))
print(abs(-4))

print(round(8.4))

print(round(8.5))
print(round(8.6))

print(bin(8))
print(hex(8))
#booleans
valid=True 
not_valid=False 
print(valid,not_valid)
print(valid==True)
print(not_valid==True)
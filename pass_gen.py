#generating random password.
import random
lc="abcdefghijklmnopqrstuvwxyz"
uc=lc.upper()
num="0123456789"
sym="!@#$%^&*()"

pass_len=8
password=lc+uc+num+sym

main_password="".join(random.sample(password,pass_len))#it takes 8 random characters from "password" and join them.
print("THE RANDOM PASSWORD IS "+main_password)
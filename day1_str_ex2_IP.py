#! /usr/bin/env python
my_IP = input("please provide IP address:")
print(my_IP)
new_var = my_IP.split(".")
print(f"{new_var[0]:<12}{new_var[1]:<12}{new_var[2]:<12}{new_var[3]:<12}")
print()

"""
import datetime

x = datetime.datetime.now()
"""
from datetime import datetime
x= datetime.now()
print(x)
print(x.strftime("%d-%m-%Y %I:%M:%S %p"))



print("YEAR")
print("%Y =", x.strftime("%Y"))
print("%y =", x.strftime("%y"))

print("\nMONTH")
print("%m =", x.strftime("%m"))
print("%B =", x.strftime("%B"))
print("%b =", x.strftime("%b"))

print("\nDAY")
print("%d =", x.strftime("%d"))
print("%A =", x.strftime("%A"))
print("%a =", x.strftime("%a"))
print("%w =", x.strftime("%w"))
print("%j =", x.strftime("%j"))

print("\nTIME")
print("%H =", x.strftime("%H"))
print("%I =", x.strftime("%I"))
print("%p =", x.strftime("%p"))
print("%M =", x.strftime("%M"))
print("%S =", x.strftime("%S"))
print("%f =", x.strftime("%f"))

print("\nWEEK")
print("%U =", x.strftime("%U"))
print("%W =", x.strftime("%W"))

print("\nCOMBINED")
print("%c =", x.strftime("%c"))
print("%x =", x.strftime("%x"))
print("%X =", x.strftime("%X"))
print("%D =", x.strftime("%D"))
print("%F =", x.strftime("%F"))
print("%r =", x.strftime("%r"))






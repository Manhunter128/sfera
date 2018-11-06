import math

def volumeSfera(r):
  return ((4./3.)*math.pi*r**3)


# main

r = input("Inserire raggio: ")
r = int(r)

print("Il volume è", volumeSfera(r))
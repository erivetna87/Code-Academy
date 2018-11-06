"""Codeacademy - Learn Python
Area Calculator
"""

print "Area Calculator is Running!"

option = raw_input ("Enter C for Circle or T for Triangle: ")

if option == 'C':
  radius = float(raw_input("Enter a Radius: "))
  area = 3.14 * radius ** 2
  print 'The area of a circle with radius %.2f Area is %.2f' % (radius, area)
  
elif option == 'T':
  base = float(raw_input("Enter Base: "))
  height = float(raw_input("Enter Height: "))
  area = .5*(base*height)
  print area
else:
  print "Invalid Shape"

print "Exiting Program"

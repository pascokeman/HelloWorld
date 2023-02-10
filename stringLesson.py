course = "Python for Beginners"
print(course.lower())
print(course.upper())
print(course.find('o'))
print(course.replace("for", "4"))
#strings are immutable i.e they cannot be changed but can only modify its form
 #after all functions used, the string course still remain the same.

print(course)
print("Python" in course)

place = course.find("for")
print(place)
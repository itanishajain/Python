marks = [84, 77, 50, 97, 78]

# (1) Append Operation
print("Append Operation")
marks.append(65)
print(marks)
print()

# (2) Insert Operation
print("Insert Operation")
marks.insert(2,88)
print(marks)
print()

print(89 in marks) # to ckeck if a element exists in list or not
print()

# Len operation
print("len operation")
print(len(marks))
print()
 
# Extend Operation
print("Extend operation")
marks.extend([2,88])
print(marks)
print()

# Remove Operation
print("remove operation")
marks.remove(97)
print(marks)
print()

# Pop Operation
print("Pop operation")
marks.pop()
print(marks)
print()

# Reverse Operation
print("Reverse operation")
marks.reverse()
print(marks)
print()

# min operation
print("min operation")
print(min(marks))
print()

# max operation
print("max operation")
print(max(marks))
print()

# index Operation
print("index operation")
print("Give the indexing of number 88 -> ",marks.index(88))
print()

# sort Operation
print("sort operation")
marks.sort()
print(marks)
print()

# sort Operation
print("clear operation")
marks.clear()
print(marks)
print()
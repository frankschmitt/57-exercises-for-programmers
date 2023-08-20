val = ""
while len(val) == 0: 
  val = input("What's the input string? ")
  if len(val) == 0:
      print("Empty input not allowed, sorry. Do better next time.")
print(f"{val} has {len(val)} characters.")

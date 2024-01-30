def my_function(**kid):
  print("His last name is " + kid["lname"])
  for k,v in kid.items():
    print(k + "->" + v)
  print(len(kid))

my_function(fname = "Tobias", lname = "Refsnes")
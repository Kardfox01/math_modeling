Full_Name = "Kaigorodov Georgii Valer'evich"
FULL_NAME = list(Full_Name.upper())
full_name = list(Full_Name.lower())

FULL_NAME = map(ord, FULL_NAME)
full_name = map(ord, full_name)

print("FULL", sum(FULL_NAME), "full", sum(full_name))
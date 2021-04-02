names = []
degrees = []
max_degree = 0
for i in range(2):
    name = input("Δώσε μου το όνοματα του μαθητή: ")
    names.append(name)
    degree = input("Τώρα πες μου τon βαθμό του: ")
    degrees.append(int(degree))    

#for u in range(2):
#    print(f"{names[u]} {degrees[u]}")

max_degree = max(degrees)
print(f"Ο μεγαλήτερος βαθμός που πήρε μαθητής είναι {max_degree}")


for y in range(2):
    if degrees[y] == max_degree:
        print(f"ο/η {names[y]} πήρε: {degrees[y]}")





#max_index = degrees.index(max_degree)
#print(max_index)



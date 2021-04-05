names = []
degrees = []
max_degree = 0
number_of_studens = input("Πες μου πόσοι είναι οι μαθητές: ")
number_of_studens = int(number_of_studens)

# το πρόγραμμα ζητάει από τον χρήστη να του δώσει το όνομα του μαθητή και τον βαθμό του
for i in range(number_of_studens):
    name = input(f"{i + 1}. Δώσε μου το όνομα του μαθητή: ")
    names.append(name)
    degree = input(f"{i + 1}. Τώρα πες μου τον βαθμό του: ")
    # αποθηκεύω τον βαθμό σαν αριθμό κινητής υποδιαστολής
    degrees.append(float(degree))    

#for u in range(2):
#    print(f"{names[u]} {degrees[u]}")

# η εντολή max επιστρέφει τον μεγαλήτερο αριθμό της λίστας
max_degree = max(degrees)
print(f"Ο μεγαλήτερος βαθμός που πήρε μαθητής είναι {max_degree}")

# σαρώνω τη λίστα και βρίσκω τους μαθητές με τον μεγαλήτερο αριθμό
for y in range(number_of_studens):
    if degrees[y] == max_degree:
        print(f"ο/η {names[y]} πήρε: {degrees[y]}")

average_degree = 0
# σαρώνω τη λίστα για να βρώ τον μέσο όρο
for u in range(number_of_studens):
    average_degree = average_degree + degrees[u]
average_degree = average_degree / len(degrees)

print(f"Ο μέσος όρος των βαθμών είναι {average_degree}")


#max_index = degrees.index(max_degree)
#print(max_index)
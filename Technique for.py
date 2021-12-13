# Technique 1 : List Comprehension --> iterateur for iterateur in list
data = [int(d) for d in data]

# Technique 2 : i est un compteur
for i in range(0, len(data)):
    data[i] = int(data[i])

# Technique 3 : d est un itérateur
    for d in data:
        data_int.append(int(d))
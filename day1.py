data_int = []
cpt_d = 0

if __name__ == '__main__':
    f = open("input.txt","r")
    data = f.read().split("\n")

    # Technique 3 : d est un itérateur
    for d in data:
        data_int.append(int(d))

    for i in range(1, len(data_int)):
        n1 = data_int[i-1]
        n2 = data_int[i]
        if n1 < n2:
            cpt_d = cpt_d+1

    print(cpt_d)
def mp(file_path):
    with open(file_path, "r") as f:
    
        words = []
        for line in f.readlines():
            a = line.split()
            for i in a:
                words.append(i)



    uniques = []
    for word in words:
        if word not in uniques:
            uniques.append(word)


    counts = []
    for unique in uniques:
        count = 0              
        for word in words:     
            if word == unique:   
                count += 1         
        counts.append((count, unique))

    counts.sort()            
    counts.reverse()         

    print(counts[0:3])

mp("HW4/Ex3/smth2.txt")
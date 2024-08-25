

def find_pairs(nambers):
    pairs = []
    for i in range(1, nambers):
        for j in range(i + 1,nambers):
            if nambers % (i + j) == 0:
                pairs.append((i + j))
            return pairs


            while True:
                nambers = randint(3, 20)
                print(F"Число: {nambers}")
                pairs = find_pairs(nambers)
                if pairs:
                    for item in pairs:
                        for namber in item:

                            print(namber, end=' ')
                            









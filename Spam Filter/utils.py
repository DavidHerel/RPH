def read_classification_from_file(input):
    dictionary = {}
    with open (input, "r", encoding ="utf-8") as f:
        for line in f:
            index = line.strip().split()
            dictionary[index[0]] = index[1]
    return dictionary


import os
def getFileNames():
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, "DeckLists")
    os.chdir(path)
    filenames = os.listdir(path)
    textfilenames = []
    decknames = []
    for file in filenames:
        if file.endswith(".txt"):
            textfilenames.append(file)
            file = file.strip(".txt")
            decknames.append(file)
    return textfilenames , decknames 
def convertToList(textfilenames, decknames):
    library = {}
    for i in range (len(textfilenames)):
        file = open(textfilenames[i], 'r')
        library[decknames[i]] = []
        for line in file:
            if '1x' in line:
                line = line.strip("\n")
                library[decknames[i]].append(line[9:])
            if '2x' in line:
                line = line.strip("\n")
                for l in range(2):
                    library[decknames[i]].append(line[9:])
        file.close()
    return library

        



import LibraryBuilder
def ID():
#init
    textfilenames, decknames = LibraryBuilder.getFileNames()
    library = LibraryBuilder.convertToList(textfilenames, decknames)
    endQuery = True
    similarity = 0
#card submit
    keylist = list(library.keys())
    fakedeck = []
    similarcards = {}
    for i in range (len(keylist)):
        similarcards[keylist[i]] = 0
    while True:
        card = str(input("Give me a card... \n")).lower()
        if fakedeck.count(card) < 2:
            fakedeck.append(card)
        else:
            print("Error: cannot have more than two copies of a card in deck")
            continue
        for i in range(len(keylist)):
            for l in range(len(library[keylist[i]])):      
                if card == ((library[keylist[i]])[l].lower()):
                    similarcards[keylist[i]] += ((1/30) * 100)
                    break
        print (similarcards, fakedeck)


                
        
        
        
        
    

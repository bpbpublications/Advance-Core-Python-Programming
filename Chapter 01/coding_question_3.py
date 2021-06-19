def outerWishes():
    global wishes 
    wishes = "Happy New Year"
    def innerWishes():
        global wishes
        wishes = "Have a great year ahead"
        print('wishes =', wishes)  
wishes = "Happiness and Prosperity Always"
outerWishes()
print('wishes =', wishes)

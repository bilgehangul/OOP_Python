from media import *





list = []
b = True
while b == True:
    print("*** Media Library ***")
    print("a. Display all Media")
    print("b. Display only Songs")
    print("c. Display only Movies")
    print("d. Display only Pictures")
    print("e. Play a Song")
    print("f. Play a Movie")
    print("g. Show a Picture")
    print("h. Add a Song")
    print("i. Add a Movie")
    print("j. Add a Picture")
    print("k. Exit the program\n")
    choice = input("Enter your choice: ")
    
    if choice == "a":
        for i in list:
            if isinstance(i,Movie) == True:
                print("Movie:",i)
            elif isinstance(i,Song) == True:
                print("Song:",i)
            elif isinstance(i,Picture) == True:
                print("Picture:",i)
    elif choice == "b":
        for i in list:
            if isinstance(i,Song) == True:
                print("Song:",i)
    elif choice == "c":
        for i in list:
            if isinstance(i,Movie) == True:
                print("Movie:",i)

    elif choice == "d":
        for i in list:
            if isinstance(i,Picture) == True:
                print("Picture:",i)
    elif choice == "e":
        name= input("Enter name of the song to play:")
        not_found = True
        for i in list:
            if isinstance(i,Song) == True and i.name == name:
                i.play()
                not_found = False
        if not_found:    
            print("No such song in the media library")
    elif choice == "f":
        name= input("Enter name of the movie to play:")
        not_found = True
        for i in list:
            if isinstance(i,Movie) == True and i.name == name:
                i.play()
                not_found = False
        if not_found:    
            print("No such movie in the media library")
                
    elif choice == "g":
        name= input("Enter name of the picture to show:")
        not_found = True
        for i in list:
            if isinstance(i,Picture) == True and i.name == name:
                i.show()
                not_found = False
        if not_found:    
            print("No such picture in the media library")
    elif choice == "h":
        item = Song.add()
        list.append(item)
    elif choice == "i":
        item = Movie.add()
        list.append(item)
    elif choice == "j":
        item = Picture.add()
        list.append(item)
    elif choice == "k":
        print(" Good-Bye!")
        b = False
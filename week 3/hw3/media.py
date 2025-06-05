class Media:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
    
    def getName(self):
        return self.name
    def getRating(self):
        return self.rating
    def setRating(self, value):
        self.rating = value

        
class Movie(Media):
    def __init__(self,name,rating,director, running_time):
        Media.__init__(self,name,rating)
        self.director = director
        self.running_time = running_time
    def add():
        name = input("Enter movie name: ")
        director = input("Enter director: ")
        duration = int(input("Enter movie duration: "))
        rating = int(input("Enter rating: "))
        item = Movie(name, rating, director, duration)
        print("Movie added!")
        return item
        
    def getDirector(self):
        return self.director
    def setDirector(self,name):
        self.director = name
    def getRunningTime(self):
        return self.running_time
    def setRunningTime(self,time):
        self.running_time = time
    def play(self):
        print("%s, %d stars, Directed by: %s, Running time: %d minutes."%(self.name, self.rating, self.director, self.running_time))
    def __str__(self):
        return "%s, %d stars, Directed by: %s, Running time: %d minutes."%(self.name, self.rating, self.director, self.running_time)
    
class Song(Media):
    def __init__(self,name,rating,artist, album):
        Media.__init__(self,name,rating)
        self.artist = artist
        self.album = album
    def add():
        name = input("Enter song name: ")
        artist = input("Enter artist: ")
        album = input("Enter album: ")
        rating = int(input("Enter rating: "))
        item = Song(name, rating, artist, album)
        print("Song added!")
        return item
        
    def getArtist(self):
        return self.artist
    def setArtist(self,name):
        self.artist = name
    def getAlbum(self):
        return self.album
    def setAlbum(self,album):
        self.album = album
    def play(self):
        print("%s, %d stars, Artist: %s, Album: %s."%(self.name, self.rating, self.artist, self.album))
    def __str__(self):
        return "%s, %d stars, Artist: %s, Album: %s."%(self.name, self.rating, self.artist, self.album)
    
class Picture(Media):
    def __init__(self,name,rating, dpi):
        Media.__init__(self,name,rating)
        self.dpi = dpi

    def add():
        name = input("Enter picture name: ")
        dpi = int(input("Enter dpi:"))
        
        rating = int(input("Enter rating: "))
        item =Picture(name, rating, dpi)
        
        print("Picture added!")
        return item
        
    def getResolution(self):
        return self.dpi
    def setResolution(self,value):
        self.dpi = value
    def show(self):
        print("%s, %d stars, Resolution: %d dpi."%(self.name, self.rating, self.dpi))
    def __str__(self):
        return "%s, %d stars, Resolution: %d dpi."%(self.name, self.rating, self.dpi)
        
        
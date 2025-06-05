from spellchecker import spellchecker #Getting the spellchecker class

def getFileName(): #getFileName function
     b=0
     while b==0:
        try:
            fileName = input('Enter the name of the file to read:\n')
            the_file=open(fileName) #This raises an error if the file doesn't exist
            b=1
        except FileNotFoundError: #gets the error 
            print("Could not open file.")
        
     return fileName
    
if __name__ == "__main__":
    print("Welcome to Text File Spellchecker.")
    SP = spellchecker("english_words.txt") 
    file_name = getFileName()
    file = open(file_name)
    line_num = 0
    word_count=0
    false_word_count = 0
    for lines in file:
        line_num+=1
        for word in lines.split():
            word_count+=1
            if not SP.check(word):
                print("Possible Spelling Error on line %d:"%(line_num),word)
                false_word_count+=1
    true_word_count = word_count-false_word_count
    print(f"{true_word_count:,}","words passed spell checker.")
    print(f"{false_word_count:,}","words failed spell checker.")
    passing_percentage = (true_word_count/word_count)*100
    passing_percentage = "{:.2f}".format(passing_percentage)
    print(passing_percentage,"% of the words passed.",sep="")
        

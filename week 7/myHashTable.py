def ispalindrome(word):
    stack = []
    queue = []
    for i in word:
        stack.append(i)
        queue.append(i)

    for i in queue:
        if i!=stack.pop():
            return False
    return True

word = input("Enter a word:")

if ispalindrome(word):
    print("Yes,",word,"is palindrome")
else:
    print("No,",word,"is not palindrome")




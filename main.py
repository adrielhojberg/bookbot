def main():
    filePath = "./books/frankestein.txt"
    file_contents = readFile(filePath)
    wordCount = countWords(file_contents)
    letterCount = countLetters(file_contents)
    printReport(filePath, wordCount, letterCount)

def readFile(filePath):
    with open(filePath) as f:
        file_contents = f.read()
    return file_contents

def countWords(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

def countLetters(text):
    dictionary = {}
    for letter in text:
        if letter.isalpha():
            lowerLetter = letter.lower()
            if lowerLetter in dictionary:
                dictionary[lowerLetter] += 1
            else:
                dictionary[lowerLetter] = 1
    return dictionary

def sort_on(dict):
    return dict["value"]

def printReport(filePath, wordCount, lettersDict):
    print(f"--- Begin report of {filePath} ---")
    print(f"{wordCount} words found in the document")

    listOfDicts = [{"key": k, "value": v} for k,v in lettersDict.items()]
    
    listOfDicts.sort(reverse=True, key=sort_on)
    for dict in listOfDicts:
        items = dict.items()
        for k,v in items:
            print(f"The '{dict['key']}' character was found {dict['value']} times")
main()

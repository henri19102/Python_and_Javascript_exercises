import json

try:
    f = open('data.json',)
    dict = json.load(f)
except:
    dict = {"kissa": "cat", "koira": "dog"}
    with open('data.json', 'w') as fp:
            json.dump(dict, fp)

print("Dictionary")

while True:

    print("Use commands:")
    print("1 = Search translation")
    print("2 = Add word")
    print("3 = Exit program")
    command = str(input("Command:")).lower()

    if command == "1":
        search = input("Give a word: ").lower()
        for word, translation in dict.items():
            if translation == search:
                print("Translation: ", word)
                break
            if word == search:
                print("Translation: ", translation)
                break
        if search not in dict.keys() and search not in dict.values():
            print("Word not found. Please input a definition")
            translation = input("Definition: ").lower()
            if len(translation) == 0:
                continue
            dict[search] = translation
            with open('data.json', 'w') as fp:
                json.dump(dict, fp)
            print("Word added to dictionary!")

    if command == "2":
        add = input("Give a word: ").lower()
        translation = input("Give a translation: ").lower()
        dict[add] = translation
        with open('data.json', 'w') as fp:
            json.dump(dict, fp)
        
    if command == "3":
        print("The program was interrupted")
        break

    

import pandas
not_guessed = True
#TODO 1. Create a dictionary in this format:
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row["letter"]: row["code"] for (index,row) in nato_data_frame.iterrows()}
print(dictionary)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        result = [dictionary[letter] for letter in word]
        print(result)
        generate_phonetic()
    except KeyError:
        print("Word not found")
        generate_phonetic()
    else:
        print(result)
generate_phonetic()


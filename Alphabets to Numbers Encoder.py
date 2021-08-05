alphabet_dictionary = {chr(i + 96): i for i in range(1, 27)}
alphabet_dictionary.update({' ': '_'})

str_in = (input("Enter the Alphabets: ")).lower()

encoded = []

for i in str_in:
    encoded.append(str(alphabet_dictionary.get(i, "*")))

output = 'Encoded: '

for code in encoded:
    output += code + " "

print(output)

if "*" in encoded:
    print("* - characters other than Alphabets")

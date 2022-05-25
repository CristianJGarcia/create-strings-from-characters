def create_strings_from_characters(frequencies, string1, string2):
    # Write your code here.
    if len(frequencies) == 0:
        if string1 == "" and string2 == "":
            return 2
        else:
            return 0

    freq_copy = frequencies.copy()

    string1_creation = True
    string2_creation = True

    # checks to see if i can get both words without reusing any characters
    for character, chr_count in freq_copy.items():
        if string1_creation:
            for letter in string1:
                if letter == character:
                    if chr_count > 0:
                        chr_count -= 1
                    else:
                        string1_creation = False
                        break
        if string2_creation:
            for letter in string2:
                if letter == character:
                    if chr_count > 0:
                        chr_count -= 1
                    else:
                        string2_creation = False
                        break

    if string1_creation and string2_creation:
        return 2
    else:
        string1_creation = True
        string2_creation = True
    ###############################################################
    freq_copy = frequencies.copy()

    for character, chr_count in freq_copy.items():
        if string1_creation:
            for letter in string1:
                if letter == character:
                    if chr_count > 0:
                        chr_count -= 1
                    else:
                        string1_creation = False
                        break

    for character, chr_count in freq_copy.items():
        if string2_creation:
            for letter in string2:
                if letter == character:
                    if chr_count > 0:
                        chr_count -= 1
                    else:
                        string2_creation = False
                        break

    if string1_creation or string2_creation:
        return 1

    return 0

frequencies = {"h": 2, "e": 1, "l": 1, "r": 4, "a": 3, "o": 2, "d": 1, "w": 1}
string1 = "hello"
string2 = "world"

print(create_strings_from_characters(frequencies, string1, string2))
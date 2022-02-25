def anagram(string1, string2):

    if sorted(string1) == sorted(string2):
        return 1
    else:
        return 0


if __name__ == "__main__":

    str1 = input("Enter 1st String: ")
    str2 = input("Enter 2nd String: ")

    if anagram(str1, str2):
        print("Strings Are Anagram")
    else:
        print("Strings are not Anagram")
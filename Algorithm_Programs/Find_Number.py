def find_number(low, high):
    mid = low + (high - low)//2
    compare = input(f"Compare with {mid} E.Equal\tG.Greater\tS.Smaller: ")
    if compare.lower() == "e":
        print(f"{mid} is your Number")
    if compare.lower() == "g":
        find_number(mid, high)
    if compare.lower() == "s":
        find_number(low, mid)


if __name__ == "__main__":
    n = int(input("Enter n for N = 2^n: "))
    print(f"Think of a number between 0 - {2**n}")
    find_number(1, (2**n)-1)

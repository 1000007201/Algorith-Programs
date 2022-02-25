def prime_num():
    prime_list = []

    for i in range(1, 1000):
        count = 0
        for j in range(1, i):
            if i % j == 0:
                count += 1
        if count >= 2:
            continue
        if count < 2:
            prime_list.append(i)
    return prime_list


def palindrome(number):
    temp = number
    _number = 0
    while temp != 0:
        _temp = temp % 10
        _number = _number*10 + _temp
        temp = temp//10
    if _number == number:
        return 1
    else:
        return


if __name__ == "__main__":
    palindrome_list = []
    prime_list = prime_num()
    for i in prime_list:
        if palindrome(i):
            palindrome_list.append(i)
    print(prime_list)
    print(palindrome_list)

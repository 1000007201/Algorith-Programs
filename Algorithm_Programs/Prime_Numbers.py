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
    print(prime_list)


if __name__ == "__main__":
    prime_num()
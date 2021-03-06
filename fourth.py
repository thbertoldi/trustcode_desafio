def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(n**0.5) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

sentence = input("Waiting for words: ")
words = sentence.split()
for word in words:
    word_sum = 0
    valid = True
    for letter in word:
        value = ord(letter)
        if (value > 96) and (value < 122):
            word_sum += value - 96
        elif (value > 64) and (value < 90):
            word_sum += value - 38
        else:
            print("Invalid word, skipping")
            valid = False
            break
    if valid:
        if is_prime(word_sum):
            print("Word {} is prime, value {}".format(word,word_sum))
        else:
            print("Word {} is not prime, value {}".format(word,word_sum))

def StringCount(string, letter):
    count = 0
    for i in string:
        if (i == letter):
            count += 1

    return count

print(StringCount('banana', 'n'))
print(StringCount('paralelepipedo', 'p'))


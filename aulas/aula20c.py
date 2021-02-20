def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [0, 2, 0, 6, 5, 0, 8, 6, 5, 4, 8]
dobra(valores)
print(valores)


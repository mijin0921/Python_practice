

def divisor_mod():
    var = []
    for i in range(1, 11):
        if 10 % i != 0:
            continue
        var.append(i)
    return var

print(divisor_mod())



def f(num1=60, num2=1000):
    bin_1 = [0] * 16
    bin_2 = [0] * 16
    bin_result = [0] * 16

    m = 0
    j = num1
    while j > 0:
        bin_1[m] = j % 2
        m += 1
        j = j // 2

    while m < 16:
        bin_1[m] = 0
        m += 1

    # bin_1 is the binary representation of num1

    l = 0
    k = num2
    while k > 0:
        bin_2[l] = k % 2
        l += 1
        k = k // 2

    while l < 16:
        bin_2[l] = 0
        l += 1

    m = 15
    while m >= 0:
        bin_result[m] = bin_1[m] ^ bin_2[m]
        m -= 1

    result = 0
    l = 15
    while l >= 0:
        uVar1 = bin_result[l]
        dVar2 = pow(2.0, l)
        result = (dVar2 * uVar1 + result)
        l -= 1
    return result


print(f())

def expand(x: int) -> int:
    x = bin(x)[2:].zfill(6)
    table = (1, 2, 4, 3, 4, 3, 5, 6)
    newX = [x[num - 1] for num in table]
    return int(''.join(newX), 2)


def s1(x: int) -> int:
    assert 0 <= x <= 0b1111, "Invalid input to sbox 1"
    sbox1 = (
        (0b101, 0b010, 0b001, 0b110, 0b011, 0b100, 0b111, 0b000),
        (0b001, 0b100, 0b110, 0b010, 0b000, 0b111, 0b101, 0b011)
    )
    x1, x2 = divmod(x, 0b1000)
    return sbox1[x1][x2]


def s2(x: int) -> int:
    assert 0 <= x <= 0b1111, "Invalid input to sbox 2"
    sbox2 = (
        (0b100, 0b000, 0b110, 0b101, 0b111, 0b001, 0b011, 0b010),
        (0b101, 0b011, 0b000, 0b111, 0b110, 0b010, 0b001, 0b100)
    )
    x1, x2 = divmod(x, 0b1000)
    return sbox2[x1][x2]


def f(x: int, key: int) -> int:
    x = expand(x)
    x ^= key
    s1Value = s1(x >> 4)
    s2Value = s2(x & 0b1111)
    return s1Value | s2Value


def subkey(key: int, rnd: int) -> int:
    keyStr = bin(key)[2:].zfill(9)
    if rnd >= 2:
        keyStr = keyStr[rnd:] + keyStr[:rnd - 1]
    return int(keyStr[:8], 2)


def round(x: int, key: int, rnd: int) -> int:
    l0, r0 = divmod(x, 0b1000000)
    r1 = f(r0, subkey(key, rnd)) ^ l0
    l1 = r0
    return (l1 << 6) | r1


def encrypt(x: int, key: int) -> int:
    assert 0 <= x <= 0b111111111111, "Invalid plaintext"
    assert 0 <= key <= 0b111111111, "Invalid key"
    y = x
    for r in range(5):
        y = round(y, key, r + 1)
    return y


if __name__ == "__main__":
    assert expand(0b110011) == 0b11000011, "Expander failed"
    assert subkey(0b101100101, 4) == 0b10010110, "Subkey function failed"
    assert s1(0b1001) == 0b100, "S1 failed"
    assert s2(0b1001) == 0

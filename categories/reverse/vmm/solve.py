flag_enc = [0x88, 0x9A, 0x8B, 0x8A, 0x89, 0x84, 0x0D5, 0x93, 0x6B, 0x0AF, 0x0B1, 0x0B0, 0x86, 0x0A3, 0x0B9, 0x0A2, 0x98,
            0x0A8, 0x9F, 0x6B, 0x9B, 0x0AA, 0x0B9, 0x0A2, 0x68, 0x0BB, 0x0AE, 0x0B1, 0x8A, 0x0AF, 0x0D7]


def dec(x, oper):
    if oper == 1:
        return ((((x + 164 ^ 153) - 101) % 256) - 65 - 13) % 26 + 65
    if oper == 2:
        return ((((x + 164 ^ 153) - 101) % 256) - 97 - 13) % 26 + 97
    return ((x + 164 ^ 153) - 101) % 256


flag = ''
for i in flag_enc:
    not_alpha = dec(i, 3)
    if not chr(not_alpha).isalpha():
        flag += chr(not_alpha)
        continue
    if 124 <= i <= 155:
        flag += chr(dec(i, 1))
    elif 156 <= i <= 187:
        flag += chr(dec(i, 2))

print(flag)

def generate_all_binary_strings(n):
    result = []
    def generate_binary_strings(n, s):
        if n == 0:
            result.append(s)
        else:
            generate_binary_strings(n-1, s + '0')
            generate_binary_strings(n-1, s + '1')
    generate_binary_strings(n, '')
    return result

if __name__ == '__main__':
    print(generate_all_binary_strings(3))
    # 000
    # 001
    # 010
    # 011
    # 100
    # 101
    # 110
    # 111
    print(generate_all_binary_strings(4))
    # 0000
    # 0001
    # 0010
    # 0011
    # 0100
    # 0101
    # 0110
    # 0111
    # 1000
    # 1001
    # 1010
    # 1011
    # 1100
    # 1101
    # 1110
    # 1111
    print(generate_all_binary_strings(5))
    # 00000
    # 00001
    # 00010
    # 00011
    # 00100
    # 00101
    # 00110
    # 00111
    # 01000
    # 01001
    # 01010
    # 01011
    # 01100
    # 01101
    # 01110
    # 01111
    # 10000
    # 10001
    # 10010
    # 10011
    # 10100
    # 10101
    # 10110
    # 10111
    # 11000
    # 11001
    # 11010
    # 11011
    # 11100
    # 11101
    # 11110
    # 11111


hex_map = {str(i):i for i in range(10)}
hex_map.update({'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15})
    

def hex_to_decimal(hex_repr):
    n = 0
    d = 1
    hex_repr = hex_repr[::-1]
    for c in hex_repr:
        if c.lower() in hex_map:
            n = n+d*hex_map[c.lower()]
            d *= 16
        else:
            # print("not in map {}".format(c))
            return None
    return n

def get_sum(n):
    return sum(map(int, list(str(n))))


def process(line):
    ticket, check_sum = line[:-2], line[-2:]
    ticket_decimal = hex_to_decimal(ticket)
    check_sum_decimal = hex_to_decimal(check_sum)
    if not ticket_decimal or not check_sum_decimal or get_sum(ticket_decimal) != check_sum_decimal:
        return "INVALID"
    return "VALID"

# print(hex_to_decimal('8BADF0'))
# print(process('8BADF00D'))
print(process("C0FFEE1C"))
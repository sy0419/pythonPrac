bit1 = 0x61
bit2 = 0x62
print(hex(bit1 & bit2))
# & is run as AND operator
print(hex(bit1 | bit2))
# | is run as OR operator
print(hex(bit1 ^ bit2))
# ^ is run as NOR operator
print(hex(bit1 >> 1))
# A >> n => All the A bit is going to move to right as n
print(hex(bit1 << 2))
# A << n => All the A bit is going to move to left as n
def make_juice(fruit):
    return f"{fruit} is shaked"

def add_ice(juice):
    return f"{juice} + added ice"

def add_sugar(iced_juice):
    return f"{iced_juice} + added sugar"

juice = make_juice("apple")
chill_juice = add_ice(juice)
perfect_juice = add_sugar(chill_juice)
print(perfect_juice)
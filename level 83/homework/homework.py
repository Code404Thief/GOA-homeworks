class moto:
    motos_made = 0

    def __init__(self, color, year, brand, speed):
        self.color = color
        self.year = year
        self.brand = brand
        self.speed = speed
        moto.motos_made += 1

moto1 = moto("yellow", 2023, "fastpacedmotos", 700)
moto1 = moto("gray", 2010, "slowpacedmotos", 200)
moto1 = moto("blue", 2015, "mediumpacedmotos", 500)
moto1 = moto("black", 2025, "fastestpacedmotos", 1000)
print(moto.motos_made)
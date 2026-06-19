class Cup:
    def __init__(self, color, brand):
        self.color = color;
        self.brand = brand;

starCafeCup = Cup("green", "starCafe");
print("컵의 색상은", starCafeCup.color);
print("컵의 브랜드는", starCafeCup.brand);
print();
angelCafeCup = Cup("gold", "angelCafe");
print("컵의 색상은", angelCafeCup.color);
print("컵의 브랜드는", angelCafeCup.brand);
print();
blueCafeCup = Cup("blue", "blueCafe");
print("컵의 색상은", blueCafeCup.color);
print("컵의 브랜드는", angelCafeCup.color);
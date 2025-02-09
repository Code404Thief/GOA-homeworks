mobile_phone = {
    "brand": "Apple",
    "model": "iphone 8",
    "color": "Black",
    "storage": "64GB",
    "price": 500
}
for key in mobile_phone:
    print(key)
for value in mobile_phone.values():
    print(value)
for key, value in mobile_phone.items():
    print(f"{key}: {value}")
a = {"name": "네이비", "price": 32000}


print(a.get("name"))
print(a.get("discount_price"))

a["dis1000won"] = True
a["dis10per"] = False

del a["dis10per"]

print(a)





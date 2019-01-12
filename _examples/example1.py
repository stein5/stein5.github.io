def dis1000won(param):
    if param > 1000:
        param = param - 1000
    return param


def dis10per(price):
    return int(price * 0.9)


a = {"name": "네이비", "price": 22400}
b = {"name": "그레이", "price": 12400}
c = {"name": "블랙  ", "price": 42000}
d = {"name": "그린  ", "price": 400}
e = {"name": "옐로우", "price": 54000}
f = {"name": "화이트", "price": 42000}


abc = [a, b, c, d, e, f]


def add_item(item_list, item):
    item_list.append(item)
    return item_list


result = []
for jg in abc:
    price = jg["price"]
    if jg["dis10per"]:
        price = dis10per(price)

    if jg["dis1000won"]:
        price = dis1000won(price)

    result.append(jg["name"] + " "*10 + str(price) + "원")

print(result)


# for jg in abc:
#     print(jg["name"] + " "*10 + str(dis10per(jg["price"])) + "원")

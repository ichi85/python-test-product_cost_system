from product import Product

product1 = Product("ロングコート", 20000)
product2 = Product("ジャケット", 22000)
product3 = Product("ニットセーター", 3000)
product4 = Product("セーター", 2500)

products = [product1, product2, product3, product4]

print("商品一覧")
index = 0
for product in products:
    print(str(index) + ". " + product.info())
    index += 1

product_order = int(input("商品の番号を選択してください: "))
selected_product = products[product_order]

count = int(input("何セット発注しますか？ ３セットで５００円の送料が掛かります。"))

result = selected_product.get_total_price(count)

print("合計は" + str(result) + "円です")
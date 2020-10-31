# номер успешной отправки 38998349 - 31 окт 2020, 22:04:41
# houses - количество домов
# money - общий бюджет

houses, money = map(int, input().split(" "))
prices = [int(p) for p in input().split(" ")]
sorted_prices = sorted(prices)

count = 0
for price in range(len(sorted_prices)):
    if money >= sorted_prices[price]:
        money -= sorted_prices[price]
        count += 1

print(count)

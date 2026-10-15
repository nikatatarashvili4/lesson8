text = "Python არის მარტივი, Python არის ძლიერი და Python პოპულარულია."

words = text.lower().replace(",", "").replace(".", "").split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

for word, count in counts.items():
    print(f"{word}: {count}")

top_word = ""
top_count = 0
for word, count in counts.items():
    if count > top_count:
        top_word = word
        top_count = count
print(f"ყველაზე ხშირი: '{top_word}' ({top_count}-ჯერ)")

unique_words = set(words)
print("სხვადასხვა სიტყვა:", len(unique_words))

# სავარჯიში 2


prices = {"ლეპტოპი": 2500, "მაუსი": 40, "კლავიატურა": 120, "მონიტორი": 650}
stock = {"ლეპტოპი": 2, "მაუსი": 10, "კლავიატურა": 1, "მონიტორი": 3}

orders = [
    ("ნინო", "ლეპტოპი", 1),
    ("გიორგი", "მაუსი", 3),
    ("ანა", "კლავიატურა", 1),
    ("ნინო", "მაუსი", 2),
    ("გიორგი", "კლავიატურა", 1),
    ("ანა", "ტელეფონი", 1),
    ("ლუკა", "ლეპტოპი", 1),
    ("ლუკა", "მონიტორი", 5),
]

totals = {}    
rejected = []    

for customer, product, qty in orders:
    if product not in prices:
        rejected.append((customer, product, qty, "პროდუქტი არ არსებობს"))
    elif stock[product] < qty:
        rejected.append((customer, product, qty, "არასაკმარისი მარაგი"))
    else:
        stock[product] -= qty
        totals[customer] = totals.get(customer, 0) + prices[product] * qty

print("ჯამები:", totals)
print("დარჩენილი მარაგი:", stock)
print("უარყოფილი:")
for r in rejected:
    print(" ", r)


# სავარჯიშო 3



prices = {"ლეპტოპი": 2500, "მაუსი": 40, "კლავიატურა": 120, "მონიტორი": 650}
stock = {"ლეპტოპი": 2, "მაუსი": 10, "კლავიატურა": 1, "მონიტორი": 3}

orders = [
    ("ნინო", "ლეპტოპი", 1),
    ("გიორგი", "მაუსი", 3),
    ("ანა", "კლავიატურა", 1),
    ("ნინო", "მაუსი", 2),
    ("გიორგი", "კლავიატურა", 1),
    ("ანა", "ტელეფონი", 1),
    ("ლუკა", "ლეპტოპი", 1),
    ("ლუკა", "მონიტორი", 5),
]

spent = {}       
failed = set()    

for customer, product, qty in orders:
    if product not in prices:
        print(f"❌ {customer}: '{product}' არ იყიდება")
        failed.add(customer)
    elif stock[product] < qty:
        print(f"⚠️ {customer}: {product} — მარაგში მხოლოდ {stock[product]} ცალია")
        failed.add(customer)
    else:
        stock[product] -= qty
        cost = prices[product] * qty
        spent[customer] = spent.get(customer, 0) + cost
        print(f"✅ {customer}: {product} x{qty} = {cost} ლარი")

print("--- ანგარიში ---")
for customer in sorted(spent):
    print(f"{customer}: {spent[customer]} ლარი")
print(f"შემოსავალი: {sum(spent.values())} ლარი")
print("ამოიწურა:", sorted(p for p, n in stock.items() if n == 0))
print("წარუმატებელი შეკვეთა ჰქონდათ:", sorted(failed))
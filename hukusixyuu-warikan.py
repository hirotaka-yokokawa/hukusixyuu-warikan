amount = (int(input("合計金額を教えてね(円):")))
customer = (int(input("人数を教えてね(人):")))

print(f"一人あたり:{amount // customer}円"),print(f"端数:{amount % customer}円")



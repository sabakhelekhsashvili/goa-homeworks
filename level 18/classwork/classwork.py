'''
1) შექმენით 3 list'ი და სამივეც მიეცით 5 სხვადასხვა მნიშვნელობა, ასევე კომენტარის სახით ყველას მიუწერეთ ინდექსები
2) Indexing'ის მეშვეობით ყველა ლისტიდან გამოიტანეთ მეხუთე ანუ ბოლო ელემენტი
3) გადააკოპირეთ ეს list'ი
words = ["rise", "sun", "glasses"]

და indexing'ის მეშვეობით გამოიტანეთ სიტყვა "sunglasses"
4) შექმენით კიდევ ერთი list'ი და Indexing'ის მეშვეობით შეუცვალეთ ბოლო ელემენტის მნიშვნელობა
5) ახსენით რას ნიშნავს mutable
'''

name = ["luka", "nika", "gio", "saba", "aleqsi"]
#        0        1       2      3        4        


print (name[-1])


words = ["rise", "sun", "glasses"]

result = words [1] + words [2]
print(result)

numbers = [1, 2, 3, 4, 10]
numbers[-1] = 50
print(numbers)


#mutable  ნიშნავს list ჩამატებას ამოღებას და შეცვლას 
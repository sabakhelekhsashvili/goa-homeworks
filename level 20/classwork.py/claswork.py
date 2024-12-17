# 1) შექმენით list'ი 5 ელემენტით და slicing'ის მეშვეობით გამოიტანეთ 2 ელემენტიდან ბოლო ელემენტის ჩათვლით
# 2) შექმენით list'ი 5 ელემენტით და slicing'ის მეშვეობით გამოიტანეთ თავიდან ბოლოს წინა ელემენტამდე
# 3) შექმენით string'ი და შემდეგ slicing'ის მეშვეობით შეატრიალეთ უკუღმა

list1 = [1,2,3,4,5]
sliced_list1 = list1[1:]
print (sliced_list1)

sliced_list2 = list1[:-1]
print (sliced_list2)

str1 = "hello world"
reverced_str1 = str1[::-1]
print (reverced_str1)

# 2) შექმენით 10 ელემენტიანი list'ი და კომენტარის სახით დანომრეთ (მიუწერეთ ინდექსები). შემდეგ კი უბრალოდ გამოიტანეთ ეკრანზე.
# 3) პირველ დავალებაში შექმნილი List'იდან გამოიტანეთ პირველი სამი, ბოლო სამი და შუა 4 დადებითი ინდექსებით. (slicing)
# 4) პირველ დავალებაში შექმნილი List'იდან გამოიტანეთ პირველი სამი, ბოლო სამი და შუა 4 უარყოფითი ინდექსებით. (slicing)
# 5) შექმენით სტრინგი და შეატრიალეთ მისი სიმბოლოები ანუ თუ თავიდან იქნებოდა "Hello" გახდეს "olleH"

list1 = [1, 2, 3, 4, 5 ,6, 7, 8, 9, 10]
#        0  1  2  3  4  5  6  7  8  9
print (list1)

first_three = list1[:3]
last_three = list1[-3:]
middle_four = list1[2:6]

print("First three elements:", first_three)
print("Last three elements:", last_three)
print("Middle four elements:", middle_four)

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

first_three = list2[-20:-17]

last_three = list2[-3:]

middle_four = list2[-17:-13]

print("First three elements:", first_three)
print("Last three elements:", last_three)
print("Middle four elements:", middle_four)

str1 = "hello"
reverced_str1 = str1[::-1]
print("reverced sring:", reverced_str1)

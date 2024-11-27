#2) გააკეთეთ and ოპერატორის 10 მაგალითი და სანამ გაუშვებთ კომენტარად მიაწერეთ თქვენი აზრით რა იქნება შედეგი (არ არის აუცილებელი მხოლოდ 2 Input'ი იყოს, შეიძლება იყოს 10'იც, ანუ მაგალითად: True and True and False and False and True (5 input))
#3) გააკეთეთ or ოპერატორის 10 მაგალითი და სანამ გაუშვებთ კომენტარად მიაწერეთ თქვენი აზრით რა იქნება შედეგი
#4) შეურიეთ or და and ოპერატორები და გააკეთეთ ისევ 10 მაგალითი წინა დავალებების მსგავსად
#5) შეურიეთ შედარების და ლოგიკური ოპერატორები და გააკეთეთ ისევ 10 მაგალითი წინა დავალებების მსგავსად


print(True and False)#false
print(False and True)#false
print(False and False)#false
print(True and True)#true
print(True and True and False)#true
print(True and False and False)#true
print(True and False and True)#true
print(False and True and True)#false
print(False and False and True)#false
print(True and True and False)#true
print(False and True and False)#false

print(False or False)#false
print(True or True)#true
print(False or True)#false
print(True and False)#True
print(True or True or False)#true
print(True or False or True)#false
print(False or False or True)#false
print(False or True or True)#true
print(True or False or False)#false
print(False or False or True or True)#false


print(False or True and True)#true
print(True or False and False)#false
print(True or False and True)#true
print(False and True or False)#false
print(False and True or True)#true
print(True and True or False)#true
print(True and False or False and True)#false
print(True and False or True and False)#false
print(False and False or False and True)#false
print(True or False or True and False)#false

print(12>12 and 12>14 or 15>19)
print(17>99 and 55>77 or 12>59)
print(13>15 and 14>9 or 99>77)
print(66>55 and 22>12 or 32>23)
print(41>31 and 99> 51 or 95>91)
print(91>21 or 71>41 and 72>46)
print(96>81 and 51>22 or 66>41)
print(111>100 or 120>11 and 555>123)
print(345>81 and 49>20 or 91>47)
print(111>99 or 77>11 and 777>666)
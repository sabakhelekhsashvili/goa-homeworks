#1) გაიხსენეთ და ახსენით წესები რომლებიც მუშაობს ყველა ლოგიკურ ოპერატორზე რაც დღეს ვისწავლეთ (and, or, not)
#2) შექმენით and ოპერატორის მეშვეობით 5 სხვადასხვა მაგალითი
#3) შექმენით or ოპერატორის მეშვეობით 5 სხვადასხვა მაგალითი
#4) შეურიეთ შედარების და ლოგიკური ოპერატორები და გააკეთეთ 5 მაგალითი

'''
AND
    True AND True = True
    True AND False = False
    False AND True = False
    False AND False = False

OR 
True OR True = True
True OR False = True
False OR True = True
False OR False = False

NOT
NOT True = False
NOT False = True
'''

print(False and False)
print(False and True)
print(True and False)
print(True and True)
print(True and False and False)

print(True or True)
print(False or True)
print(False or False)
print (True or False)
print(False or False or True)



print(5>5 and 5>5)#False
print(7>10 and 7>11)#False
print(5==5 and 5==10) #False
print(15!=18 and 7!=9)#True
print(17!=19 and 12!=13)#True
print(11>=11 and 19>=16)#True


print(12>12 or 15>12)#True
print(5>8 or 7>9)#false
print(21==12 or 19==16)#false
print(66!=61 or 65!=31)##true
print(91>=77 or 79>=55)#true


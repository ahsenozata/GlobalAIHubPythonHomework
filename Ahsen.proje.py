Name = input("Please Enter your name and surname:")
c=3
dersler=[]
if Name =='Ahsen Ozata':
    print("Welcome "+format(Name))
else:
    while Name != 'Ahsen Ozata':
        c=c-1
        if c != 0:
            print('Wrong password!. You have ' + format(c) + ' chances left')
            Name = input("Please Enter your name and surname:")
            if Name =='Ahsen Ozata':
                print("Welcome " + format(Name))
        else:
            print('\nFailed to login!')
print("You have to add min 3,max 5 courses")
dersler.append(input("Listeye Eklenecek dersleri Giriniz: "))
print(dersler)
finalNotu=int(input("Notlar:"))
midterm=int(input("Notlar:"))
proje=int(input("Notlar:"))
ortalamaNot=(finalNotu*0.5+midterm*0.3+proje*0.2)/3
print(ortalamaNot)
if ortalamaNot >= 50:
    if (ortalamaNot >= 85 and finalNotu >= 50):
        print("Harf Notunuz AA")
    elif ortalamaNot >= 75 and ortalamaNot < 85:
        print("Harf Notunuz BA")
    elif ortalamaNot >= 70 and ortalamaNot < 75:
        print("Harf Notunuz BB")
    elif ortalamaNot >= 65 and ortalamaNot < 70:
        print("Harf Notunuz CB")
    elif ortalamaNot >= 60 and ortalamaNot < 65:
        print("Harf Notunuz CC")
    elif ortalamaNot >= 55 and ortalamaNot < 60:
        print("Harf Notunuz DC")
    elif ortalamaNot >= 50 and ortalamaNot < 55:
        print("Harf Notunuz DD")

else:
    print("Harf notunuz FF kaldınız .")
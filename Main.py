import time

print("HESAP MAKINESI!!!")

time.sleep(1)

while True:

    first = int(input("ilk sayıyı girin (Herhangi bir sayı)"))
    second = int(input("ikinci sayıyı girin (Herhangi bir sayı)"))
    symbol = input("Birini seçin (+ - * /)")


    if symbol == "+":
        math = first + second
    elif symbol == "-":
        math = first - second
    elif symbol == "*":
        math = first * second
    elif symbol == "/":
        math = first / second
    
    print("İşleminiz Düşünülüyor...")

    time.sleep(2)

    print("Cevabınız", math, "!")

    time.sleep(1)

    Q = input("Bir daha yapmak istermisiniz? (E / H)")
    if Q == "H":
        print("Görüşürüz!")
        break
    else:
        print ("O zaman")

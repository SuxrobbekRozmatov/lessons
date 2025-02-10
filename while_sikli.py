# while True:
#     rang = input("Iltimos, svetofor qaysi rangda ekanligini kiriting (qizil, sariq, yashil): ").lower()
#
#     if rang in ['qizil', 'sariq', 'yashil']:
#         print("Rahmat, to'g'ri keladi!")
#         break
#     else:
#         print("Xato rang kiritdingiz. Iltimos, qaytadan urinib ko'ring.")

# import random
# tasodifiy_son = random.randint(1, 10)
#
# while True:
#     foydalanuvchi_soni = int(input("1 dan 10 gacha bo'lgan sonni kiriting: "))
#     if foydalanuvchi_soni == tasodifiy_son:
#         print("Tabriklaymiz, siz topdingiz!")
#         break
#     else:
#         print("Noto'g'ri, qayta urinib ko'ring.")



# do_stlar = []
#
# while True:
#     ism = input("Do'stingizning ismini kiriting (to'xtatish uchun 'stop' deb yozing): ")
#     if ism.lower() == 'stop':
#         break
#     do_stlar.append(ism)
# print("Sizning do'stlaringiz ro'yxati:")
# for ism in do_stlar:
#     print(ism)


# USD_KURSI = 12600
# while True:
#     kiruvchi = input("So'm miqdorini kiriting (chiqish uchun 'exit' deb yozing): ")
#     if kiruvchi.lower() == 'exit':
#         print("Dastur to'xtatildi. Xayr!")
#         break
#
#     try:
#         # Kiritilgan qiymatni sonli formatga o'tkazamiz
#         som = float(kiruvchi)
#
#         # Hisob-kitobni amalga oshiramiz
#         dollar = som / USD_KURSI
#
#         # Natijani chiqaramiz
#         print(f"{som} so'm = {dollar:.2f} USD")
#     except ValueError:
#         # Agar foydalanuvchi noto'g'ri qiymat kiritgan bo'lsa, xabar chiqaramiz
#         print("Iltimos, faqat raqam kiriting yoki 'exit' deb yozing!")
sonlar = [7, 4, 15, 4, 50]
print(f"Asl ro'yxat: {sonlar}")
natija = []
for i, element in enumerate(sonlar):
    natija.append(element * i)

print(f"Natija:      {natija}")
natija_2 = [element * i for i, element in enumerate(sonlar)]
print(f"Tekshirish:  {natija_2}")

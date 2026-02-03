#6
try:
    a = int(input('Birinchi sonni kiriting: '))
    b = int(input('Ikkinchi sonni kiriting: '))
    print(f'Natija: {a / b}')
except ZeroDivisionError:
    print('Siz sonni 0 ga bolishga harakat qilyapsiz')
except ValueError:
    print('Siz matn kiritdingiz')

#7
roy = [1, 2, 3, 4, 5, 6, 7, 8]
son = int(input('Qaysi sonni ochirmoqchisiz: '))
try:
    roy.remove(son)
    print(f'{son} soni royxatdan ochirildi')
except ValueError:
    print('Son topilmadi')

print(f'Royxat: {roy}')

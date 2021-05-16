# tipe data skalar => tipe data sederhana
anak1 = 'eko'
anak2 = 'dwi'

# tipe data list/daftar/array
anak = ['eko', 'dwi', 'tri', 'catur']
anak.append('lino')
# print(anak)

# print(f'hai {anak[1]}!')

for a in anak:
    print(f'\nhai {a}!')

for a in range(0, len(anak)):
    print(f'{a+1}. hai {anak[a]}')
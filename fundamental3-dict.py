kamus = {'anak': 'son', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}

# print(kamus)
# print(kamus['ayah'])

print('data ini dikirimkan oleh server gojek untuk memberikan info driver sekitar kepada customer')
data_dari_server_gojek = {
    'tanggal': '2021-05-16',
    'driver_list': [{'nama': 'eko', 'jarak': 10},
                    {'nama': 'dwi', 'jarak': 30},
                    {'nama': 'tri', 'jarak': 100},
                    {'nama': 'catur', 'jarak': 1000}],
}

print(data_dari_server_gojek)
print(f"driver disekitar sini {data_dari_server_gojek['driver_list']}")
print(f"driver pertama {data_dari_server_gojek['driver_list'][0]}")
print(f"driver keempat {data_dari_server_gojek['driver_list'][3]}")
print(f"driver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")
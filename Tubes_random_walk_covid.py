import random

import matplotlib.pyplot as plt
import numpy


# variabel
jumlah_individu = 200
allocate_infected_individu = int((5/100)*jumlah_individu)
waktu_pemulihan = 10
total_waktu_pemulihan = 0
jumlah_individu_terinfeksi = [0] 

kondisi_individu_saat_ini = []
kondisi_color = []
posisi_terinfeksi = []
posisi_individu = []
imun_individu = []
waktu_pemulihan_individu = []

for p in range(jumlah_individu):
    kor_x = random.randint(-10, 10)
    kor_y = random.randint(-10, 10)
    posisi_individu.append([0,0])


def infected_individu(allocate_infected_individu, jumlah_individu_terinfeksi):
    for i in range(allocate_infected_individu):
        kondisi_individu_saat_ini.append('terinfeksi')
        waktu_pemulihan_individu.append(1)
        imun_individu.append('tidak punya imun')
        jumlah_individu_terinfeksi[0] += 1
    return(jumlah_individu_terinfeksi)


def uninfected_individu(jumlah_individu, allocate_infected_individu):
    hasil = jumlah_individu - allocate_infected_individu
    for i in range(hasil):
        kondisi_individu_saat_ini.append('tidak terinfeksi')
        waktu_pemulihan_individu.append(0)
        imun_individu.append('tidak punya imun')


def generate_pergerakan(n):
    for i in range(n):
        x = posisi_individu[i][0]
        y = posisi_individu[i][1]
        step = random.uniform(0, 1)
        if step <= 0.20:
            x = x + 1  # Bergerak ke kanan
        elif step <= 0.40:
            y = y - 1  # Bergerak ke bawah
        elif step <= 0.60:
            x = x - 1  # Bergerak ke kiri
        elif step <= 0.80:
            y = y + 1  # Bergerak ke atas
        else:
            continue   # Diam
            
        x_max =  20
        x_min = -20

        y_max =  20
        y_min = -20
        
        # PBC Method
        if x > x_max:
            x = x - x_max
        if x < x_min:
            x = x + abs(x_min)
        if y > y_max:
            y = y - y_max
        if y < y_min:
            y = y + abs(y_min)
        
        try:
            posisi_individu[i] = [x,y]
        except:
            posisi_individu.append([x,y])
        

jumlah_individu_terinfeksi = infected_individu(allocate_infected_individu,jumlah_individu_terinfeksi)
uninfected_individu(jumlah_individu,allocate_infected_individu)


def current_position_that_infected(n):
    for i in range(n):
        if kondisi_individu_saat_ini[i] == 'terinfeksi':
            posisi_terinfeksi.append(posisi_individu[i])
            return(False)
        if kondisi_individu_saat_ini[i] == 'tidak terinfeksi' and (posisi_individu[i] in posisi_terinfeksi) and (imun_individu[i] == 'tidak punya imun') :
            kondisi_individu_saat_ini[i] = 'terinfeksi'
            waktu_pemulihan_individu[i] = 1
            jumlah_individu_terinfeksi[0] += 1


"""
#print("individu {} dengan posisi: {} ".format(j,posisi_individu[j]))
for k in range(len(kondisi_individu_saat_ini)):
    print("individu nomor {}".format(k+1))
    print("kondisi individu saat ini: {}".format(kondisi_individu_saat_ini[k]))
    print("kondisi imun individu: {}".format(imun_individu[k]))
    print("waktu pemulihan individu: {}".format(kondisi_individu_saat_ini[k]))
    print("posisi individu: {}".format(posisi_individu[k]))
    print("")
print("jumlah individu terinfeksi: {}".format(jumlah_individu_terinfeksi))
print("")
"""
while jumlah_individu_terinfeksi[0] > 0:
    posisi_terinfeksi.clear()
    print("hari ke:", total_waktu_pemulihan)
    total_waktu_pemulihan += 1
    for i in range(jumlah_individu):
        generate_pergerakan(jumlah_individu)
        current_position_that_infected(jumlah_individu)
        print("individu: ", i)
        print("kondisi individu: ", kondisi_individu_saat_ini[i])
        print("kondisi imun individu: ", imun_individu[i])
        print("posisi individu: {}".format(posisi_individu[i]))
        print("sisa waktu pemulihan individu: ", waktu_pemulihan_individu[i])
        print("")
        if kondisi_individu_saat_ini[i] == 'terinfeksi':
            waktu_sembuh = waktu_pemulihan_individu[i] + 1
            waktu_pemulihan_individu[i] = waktu_sembuh 
            if waktu_pemulihan_individu[i] >= waktu_pemulihan:
                imun_individu[i] = 'punya imun'
                kondisi_individu_saat_ini[i] = 'tidak terinfeksi'
                jumlah_individu_terinfeksi[0] = jumlah_individu_terinfeksi[0] - 1
    print('total pasien ter infeksi: ', jumlah_individu_terinfeksi[0])

print('hasil akhir')
print(" ")
for j in range(jumlah_individu):
    print("individu: ", j)
    print("kondisi individu: ", kondisi_individu_saat_ini[j])
    print("kondisi imun individu: ", imun_individu[j])
    print("posisi individu: {}".format(posisi_individu[j]))
    print("sisa waktu pemulihan individu: ", waktu_pemulihan_individu[j])

print("total hari pemulihan: ", total_waktu_pemulihan)

posisi_individu_x = numpy.array(posisi_individu)[:, 0]
posisi_individu_y = numpy.array(posisi_individu)[:, 1]

scat = plt.scatter(posisi_individu_x, posisi_individu_y)
plt.show()
import random

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy

from matplotlib.animation import FuncAnimation

# variabel
jumlah_individu = 200
allocate_infected_individu = int((5 / 100) * jumlah_individu)
waktu_pemulihan = 10
total_waktu_pemulihan = 0
jumlah_individu_terinfeksi = [0]

kondisi_individu_saat_ini = []
posisi_terinfeksi = []
posisi_individu = []
imun_individu = []
waktu_pemulihan_individu = []

data_invidu_terinfeksi = []
kondisi_color_setiap_waktu = []
posisi_individu_setiap_waktu = []

for p in range(jumlah_individu):
    kor_x = random.randint(-10, 10)
    kor_y = random.randint(-10, 10)
    posisi_individu.append([0, 0])


def infected_individu(allocate_infected_individu, jumlah_individu_terinfeksi):
    for i in range(allocate_infected_individu):
        kondisi_individu_saat_ini.append('terinfeksi')
        waktu_pemulihan_individu.append(1)
        imun_individu.append('tidak punya imun')
        jumlah_individu_terinfeksi[0] += 1
    return (jumlah_individu_terinfeksi)


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
            continue  # Diam

        x_max = 20
        x_min = -20

        y_max = 20
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
            posisi_individu[i] = [x, y]
        except:
            posisi_individu.append([x, y])


jumlah_individu_terinfeksi = infected_individu(allocate_infected_individu, jumlah_individu_terinfeksi)
uninfected_individu(jumlah_individu, allocate_infected_individu)


def current_position_that_infected(n):
    for i in range(n):
        if kondisi_individu_saat_ini[i] == 'terinfeksi':
            posisi_terinfeksi.append(posisi_individu[i])
            return (False)
        if kondisi_individu_saat_ini[i] == 'tidak terinfeksi' and (posisi_individu[i] in posisi_terinfeksi) and (
                imun_individu[i] == 'tidak punya imun'):
            kondisi_individu_saat_ini[i] = 'terinfeksi'
            waktu_pemulihan_individu[i] = 1
            jumlah_individu_terinfeksi[0] += 1

while jumlah_individu_terinfeksi[0] > 0:
    posisi_terinfeksi.clear()
    total_waktu_pemulihan += 1
    for i in range(jumlah_individu):
        warna = 'blue'
        generate_pergerakan(jumlah_individu)
        current_position_that_infected(jumlah_individu)
        if kondisi_individu_saat_ini[i] == 'terinfeksi':
            waktu_sembuh = waktu_pemulihan_individu[i] + 1
            waktu_pemulihan_individu[i] = waktu_sembuh
            warna = 'red'
            if waktu_pemulihan_individu[i] >= waktu_pemulihan:
                imun_individu[i] = 'punya imun'
                kondisi_individu_saat_ini[i] = 'tidak terinfeksi'
                jumlah_individu_terinfeksi[0] = jumlah_individu_terinfeksi[0] - 1
                warna = 'blue'
        posisi_individu_setiap_waktu.append(posisi_individu[i])
        kondisi_color_setiap_waktu.append(warna)
    data_invidu_terinfeksi.append(jumlah_individu_terinfeksi[0])
    # print('total pasien ter infeksi: ', jumlah_individu_terinfeksi[0])

print("total hari pemulihan: ", total_waktu_pemulihan)

kondisi_individu_x = numpy.array(posisi_individu_setiap_waktu)[:, 0]
kondisi_individu_y = numpy.array(posisi_individu_setiap_waktu)[:, 1]


fig = plt.figure()
ax = fig.add_subplot(111)

scat = plt.scatter(kondisi_individu_x, kondisi_individu_y)


def update(frame_number, color_data, scat):
    scat.set_offsets((kondisi_individu_x[frame_number], kondisi_individu_y[frame_number]))
    scat.set_color(color_data[frame_number])
    return scat


animation = FuncAnimation(fig, update, fargs=(kondisi_color_setiap_waktu, scat),
                          frames=500, interval=100, repeat=False)
infeksi_patch = mpatches.Patch(color='red', label='Individu Terinfeksi')
non_infeksi_patch = mpatches.Patch(color='blue', label='Individu Pulih Atau Tidak Terinfeksi')
plt.legend(handles=[infeksi_patch, non_infeksi_patch])

plt.show()

animation.save('ucok.mp4')

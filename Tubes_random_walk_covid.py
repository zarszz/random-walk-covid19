import random

#variabel 
jumlah_pasien = 200
waktu_pemulihan = 10

kondisi_individu_saat_ini = []
posisi_individu = []
imun_individu = []
waktu_pemulihan_individu = []

x_max =  20
x_min = -20

y_max = 20
y_min = -20

def infected_patient():
    for i in range(10):
        kondisi_individu_saat_ini.append('terinfeksi')
        waktu_pemulihan_individu.append(10)
        imun_individu.append('tidak punya imun')

infected_patient()
    
for i in range(len(kondisi_individu_saat_ini)):
    print("individu nomor {}".format(i+1))
    print("kondisi individu saat ini: {}".format(kondisi_individu_saat_ini[i]))
    print("kondisi imun individu: {}".format(imun_individu[i]))
    print("waktu pemulihan individu: {}".format(kondisi_individu_saat_ini[i]))
    print("")
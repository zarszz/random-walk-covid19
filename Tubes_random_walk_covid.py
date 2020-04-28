import random

#variabel 
jumlah_individu = 30
waktu_pemulihan = 10
total_waktu_pemulihan = 0
jumlah_individu_terinfeksi = 0 

kondisi_individu_saat_ini = []
posisi_terinfeksi = []
posisi_individu = []
imun_individu = []
waktu_pemulihan_individu = []

for p in range(30):
    posisi_individu.append([0,0])

def infected_individu(jumlah_individu_terinfeksi):
    for i in range(10):
        kondisi_individu_saat_ini.append('terinfeksi')
        waktu_pemulihan_individu.append(10)
        imun_individu.append('tidak punya imun')
        jumlah_individu_terinfeksi += 1
    return(jumlah_individu_terinfeksi)
        
def uninfected_individu():
    for i in range(20):
        kondisi_individu_saat_ini.append('tidak terinfeksi')
        waktu_pemulihan_individu.append(0)
        imun_individu.append('tidak punya imun')
        
def generate_pergerakan(n):
    for i in range(n):
        x = posisi_individu[i][0]
        y = posisi_individu[i][1]
        step = random.choice(['N','S','E','W'])
        if step == 'N':
            y = y+1
        elif step == 'S':
            y = y - 1
        elif step == 'E':
            x = x+1
        else:
            x = x - 1
            
        x_max =  20
        x_min = -20

        y_max =  20
        y_min = -20
        
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
        

jumlah_individu_terinfeksi = infected_individu(jumlah_individu_terinfeksi)
uninfected_individu()

def current_position_that_infected(jumlah_individu_terinfeksi,n):
    posisi_terinfeksi.clear()
    for i in range(n):
        if kondisi_individu_saat_ini[i] == 'terinfeksi':
            posisi_terinfeksi.append(posisi_individu[i])
        if kondisi_individu_saat_ini[i] == 'tidak terinfeksi' and (posisi_individu[i] in posisi_terinfeksi) and (imun_individu[i] == 'tidak punya imun') :
            kondisi_individu_saat_ini[i] = 'terinfeksi'
            waktu_pemulihan_individu[i] = 10
            jumlah_individu_terinfeksi += 1


#print("individu {} dengan posisi: {} ".format(j,posisi_individu[j]))
for k in range(len(kondisi_individu_saat_ini)):
    print("individu nomor {}".format(k+1))
    print("kondisi individu saat ini: {}".format(kondisi_individu_saat_ini[k]))
    print("kondisi imun individu: {}".format(imun_individu[k]))
    print("waktu pemulihan individu: {}".format(kondisi_individu_saat_ini[k]))
    print("")
print("jumlah individu terinfeksi: {}".format(infected_individu(jumlah_individu_terinfeksi)))

while jumlah_individu_terinfeksi > 0:
    total_waktu_pemulihan += 1
    print("hari ke:", total_waktu_pemulihan)
    print(" ")
    for i in range(30):
        generate_pergerakan(30)
        #current_position_that_infected(jumlah_individu_terinfeksi,30)
        print("individu: ",i)
        print("kondisi individu: ",kondisi_individu_saat_ini[i])
        print("kondisi imun individu: ",imun_individu[i])
        print("posisi individu: {}".format(posisi_individu[i]))
        print("sisa waktu pemulihan individu: ",waktu_pemulihan_individu[i])
        print(" ")
        if kondisi_individu_saat_ini[i] == 'terinfeksi':
            waktu_sembuh = waktu_pemulihan_individu[i] - 1
            waktu_pemulihan_individu[i] = waktu_sembuh
            if waktu_pemulihan_individu[i] == 0:
                imun_individu[i] = 'punya imun'
                kondisi_individu_saat_ini[i] = 'tidak terinfeksi'
                jumlah_individu_terinfeksi = jumlah_individu_terinfeksi - 1
        print('total pasien ter infeksi: ',jumlah_individu_terinfeksi)

print('total waktu yang di perlukan untuk pemulihan: ',total_waktu_pemulihan)
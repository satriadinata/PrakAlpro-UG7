# 0010320001-satriadinata.pdf
fileName=input('Masukkan nama file: ')
jur=['001-Infomatika','002-Kedoteran','003-Hukum','004-Arsitektur']
bulan=['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']
dataPecah=fileName.split('-')
noDaftar=dataPecah[0]
nama=dataPecah[1]
for i in jur:
    j=i.split('-')
    if j[0]==noDaftar[0:3]:
        jurusan=j[1]
Bulan=bulan[int(noDaftar[3:5])-1]
Tahun='20'+noDaftar[5:7]
noUrut=noDaftar[7:10]
print('Data pendaftaran : ')
print('Jurusan :',jurusan)
print('Waktu Daftar :',Bulan,Tahun)
print('No Urut :',noUrut)
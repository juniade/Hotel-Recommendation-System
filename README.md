# Laporan Proyek Machine Learning -Juniandika


## Domain Proyek
#### Perkembangan teknologi yang semakin pesat menghadirkan inovasi baru dalam menentukan pilihan secara cepat dan tepat sesuai keinginan manusia. Salah satu contohnya seperti menentukan pilihan hotel. Untuk bisa menentukan pilihan hotel yang tepat dan sesuai dengan keinginan pengguna, maka diperlukan kemampuan untuk mendapatkan infomasi hotel secara cepat dan akurat. Oleh karena itu, hadirlah sistem rekomendasi hotel untuk memberikan kemudahan bagi para pengguna dalam menentukan sesuatu yang sesuai dengan keinginan pengguna tanpa harus mencari informasi detail dari setiap hotel. Sistem rekomendasi ini didasari atas preferensi kesukaan pengguna di masa lalu yang nantinya dijadikan sebagai acuan dalam memberikan prediksi terkait rekomendasi item tertentu berdasarkan tingkat kemiripan. 

## Business Understanding
### Problem Statement
#### Berdasarkan latar belakang di atas, bagaimana membangun sistem rekomendasi hotel yang dapat mempermudah pengguna dalam memberikan rekomendasi dengan menggunakan metode *conte based filtering*.
### Goals
#### Tujuan dari proyek ini adalah supaya dapat memberikan kemudahan dalam menemukan hotel sesuai dengan preferensi pengguna.
### Solution Statement
#### Solusi yang dapat dilakukan agar tujuan terpenuhi yaitu dengan membuat model rekomendasi sistem untuk memberikan rekomendasi hotel dengan pendekatan *content based filtering*

## Data Undersatnding
#### Dataset yang digunakan dalam proyek ini diambil dari website kaggle [hotel recomendation|Kaggle](https://www.kaggle.com/datasets/keshavramaiah/hotel-recommendation). Pada proyek ini digunakan 2 buah dataset yaitu *Hotel_details.csv* dan *Hotel_Room_attributes.csv*
#### Dataset pertama yaitu *Hotel_details.csv* yang memiliki 108048 baris dan 14 kolom dengan informasi sebagai berikut:
- id : id user
- hotelid : id hotel
- address : alamat hotel berasal
- city : kota hotel berasal
- country : negara hotel berasal
- zipcode : zipcode dari hotel
- propertytype : tipe properti dari hotel
- starrating : rating dari hotel
- latitude : garis lintang hotel
- longitude : garis bujur hotel
- Source : jumlah sumber hotel
- url : alamat website hotel
- curr: pusat unit rekam jejak sumber dari hotel

#### Dataset kedua yaitu *Hotel_Room_attributes.csv* dengan total 165873 baris dan 5 kolom dengan informasi sebagai berikut:
- id :n adalah id dari user
- hotelcode : id hotel
- roomamenities : fasilitas kamar
- roomtype : tipe kamar
- ratedescription : deskripsi kamar

## Exploratory Data Analysis
#### Pada tahapan ini dilakukan pemrosesan data seperti menghapus *missing value*, menghapus diplikat, menghapus fitur yang tidak relevan, serta melakukan *merging* data.
- ### Menangani *missing value*
  #### Pada dataset *Hotel_details.csv* terdapat *missing value* pada kolom addres dan url sedangkan pada dataset *Hotel_Room_attributes.csv* terdapat missing value pada kolom roomamenities dan ratedescription
- ### Menghapus fitur yang tidak relevan 
  #### Pada tahapn ini dilakukan penghapusan beberapa kolom yang dirasa tidak diperlukan dalam menentukan model sistem rekomendasi diantaranya seperti kolom id,zipcode pada dataset *Hotel_details.csv* dan id pada dataset *Hotel_Room_attributes.csv*
- ### Menghapus duplikat 
  #### Pada tahapan ini dilakukan penghapusan duplikat record contohnya seperti pada hotelid yang banyak mengnadung duplikasi data sehingga dapat membuat waktu komputasi semakin cepat
- ### *Merging dataset* 
  #### Pada tahapan ini dilakukan penyauan kedua dataset yang disatukan berdasarkan hotelcode dan hotel id yang ditampung ke dalam variabel hotel. Kemudian melakukan seleksi fitur-fitur yang diarasa memiliki korelasi penting dalam membuat sistem rekomendasi seperti hotelcode, hotelname, roomtype, dan starrating pada dataset hotel yang telah dibuat
  
## Data Preparation
#### Pada tahapan ini kita akan menghapus beberapa karakter yang tidak diperlukan dalam kolom roomtype. Krakter yang tidak diperlukan itu berupa punctuation (!"#$%&\'() +,-./:;<=>?@[\\]^_ {|}~' yang terdapat dalam library string. Untuk melakukan penghapusan maka dibuatkan sebuah fungsi bernama text_proses
#### selain itu dilakuakn reset index untuk me-reset index suapaya menjadi teratur dan normal kembali.
| roomtype                      | roomtype                    |
| ------------------------------| --------------------------- |
| Deluxe, Guest room, 1 Double  | Deluxe Guest room 1 Double  |
| Twin En-suite                 | Twin En suite               |

#### Steleh itu kita ubah huruh kapital yang berada pada roomtype menjadi huruf kecil semua dengan menggunakan gungsi str.lower()
| roomtype                      | roomtype                    |
| ------------------------------| --------------------------- |
| Deluxe, Guest room, 1 Double  | deluxe guest room 1 double  |
| Twin En-suite                 | twin en suite               |

#### selanjutnya kita replace spasi (" ") dengan ( _ )
| roomtype                      | roomtype                    |
| ------------------------------| --------------------------- |
| Deluxe, Guest room, 1 Double  | deluxe_guest_room_1_double  |
| Twin En-suite                 | twin_en_suite               |




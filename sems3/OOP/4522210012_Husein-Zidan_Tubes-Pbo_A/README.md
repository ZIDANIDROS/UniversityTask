<h1><b>MUSIC PLAYER.mp3</b></h1>


# 1. Topik
  pengembangan aplikasi pemutar musik sederhana menggunakan Java dan JavaFX. Kode ini memperlihatkan penggunaan dasar dari JavaFX untuk membuat antarmuka pengguna (UI) sederhana dan bagaimana mengimplementasikan   logika dasar untuk memainkan, menjeda, menghentikan, serta mengontrol playlist lagu yang dimuat dari direktori pada sistem file.

# 2. Masalah
  - menghindari mp.3 app yang adsen atau iklan nya karena itu sangat mengganggu
  - menghindari virus dari app yang disediakan yang gratis, dikarenakan kalo kita download app gratis kemungkinan akan ada virus sehingga saya membuat app sendiri

# 3. Siapa yang Terlibat
  - user
  - data music

# 4. Data apa saja yang disimpan dan diolah
  - Data yang disimpan : folder music
  - Data yang diolah   : file-file mp3

# 5. Model class
  * class ```AbstractMusicPlayer```:
      - Buat class abstract ```AbstractMusicPlayer``` yang mengimplementasikan interface ```MusicControl```.
      - Definisikan atribut-atribut yang diperlukan seperti Media, MediaPlayer, playlist, dsb.
      - Implementasikan fungsi-fungsi dasar seperti playMusic, pauseMusic, stopMusic, nextMusic, previousMusic, setVolume.
      - Buat sebuah method abstract setStatusLabel yang akan diimplementasikan oleh class turunannya.
  
  * Interface ```MusicControl```:
      - Tentukan kontrak fungsi-fungsi dasar seperti playMusic, pauseMusic, stopMusic, nextMusic, previousMusic.
  
  * class ```MusicPlayerController``` extends ```AbstractMusicPlayer```:
      - Implementasikan method initialize untuk memuat musik dari direktori menggunakan DirectoryStream.
      - Implementasikan method loadMusicFromDirectory yang akan membaca file-file musik dari direktori yang ditentukan.
      - Buat method playMusic untuk memainkan musik yang terpilih dari playlist.
      - Buat method pauseMusic, stopMusic, nextMusic, previousMusic untuk mengontrol pemutaran musik.
      - Implementasikan method setVolume untuk mengatur volume pemutaran musik.
      - Override method setStatusLabel yang akan menampilkan status pemutaran pada UI.
  
  * class ```MusicPlayerApplication``` extends Application:
      - Override method start untuk menginisialisasi aplikasi JavaFX.
      - Muat antarmuka pengguna menggunakan FXML.
      - Tetapkan class MusicPlayerController sebagai controller untuk antarmuka pengguna.
      - Tampilkan aplikasi dengan stage yang sesuai.

# 6. UML
<img src="https://github.com/ZIDANIDROS/uas-PBO/blob/main/screenshoot/UML.JPG" alt="gambarUML" align="bottom">

# 7. Skenario
1. Memulai Aplikasi
2. Pengguna membuka aplikasi pemutar musik.
3. Layar awal aplikasi ditampilkan untuk mengontrol pemutaran musik.
4. Pengguna menekan tombol "Play" untuk memulai pemutaran musik.
5. Jika tidak ada musik dalam daftar putar, pesan "No music found!" ditampilkan.
6. Jika ada musik dalam daftar putar, lagu pertama dimulai secara otomatis.
7. Memainkan Musik
8. Pengguna dapat melihat judul lagu yang diputar pada label status.
9. Pengguna dapat mengklik tombol "Pause" untuk menghentikan sementara pemutaran.
10. Pengguna dapat mengklik tombol "Stop" untuk menghentikan pemutaran lagu.
11. Pengguna dapat melihat judul yang akan diputar setelah music yang sedang diputar pada label status.
12. Navigasi Lagu.
13. Pengguna dapat memilih lagu berikutnya dengan mengklik tombol "Next".
14. Pengguna dapat memilih lagu sebelumnya dengan mengklik tombol "Previous".
15. Mengakhiri Aplikasi.
16. Pengguna menutup aplikasi setelah selesai mendengarkan musik.

# 9. Referensi
akun youtube 'Bro code' <link src="https://www.youtube.com/watch?v=-D2OIekCKes&t=830s">
implemtasi saya :
                  - IDE : IntellJIDE
                  - dengan MAVEN
                  - version, jadi harus merubah version pada file POM.xml
Fitur :
       - Play
       - Pause
       - Stop
       - Next
       - ada notif untuk nama music selanjutnya
       - Previous
       - Menampilkan Judul music

# 10. Printscreen hasil running code
<img src="https://github.com/ZIDANIDROS/uas-PBO/blob/main/screenshoot/gambaran%20app.JPG" alt="gambarApps" align="bottom">

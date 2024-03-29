package PenjumlahanDanPengurangan.Matriks;

public class Matrik{
    private Pecahan[][] data;
    private int baris;
    private int kolom;

    public Matrik(int baris, int kolom) {
        this.baris = baris;
        this.kolom = kolom;
        this.data = new Pecahan[baris][kolom];
    }


    public PenjumlahanDanPengurangan.Matriks.Matrik tambah(PenjumlahanDanPengurangan.Matriks.Matrik other) {
        if (this.baris != other.baris || this.kolom != other.kolom) {
            System.out.println("Ukuran matriks tidak sesuai");
            return null;
        }
        PenjumlahanDanPengurangan.Matriks.Matrik hasil = new PenjumlahanDanPengurangan.Matriks.Matrik(this.baris, this.kolom);
        for (int i = 0; i < baris; i++) {
            for (int j = 0; j < kolom; j++) {
                hasil.data[i][j] = this.data[i][j].tambah(other.data[i][j]);
            }
        }
        return hasil;
    }

    public PenjumlahanDanPengurangan.Matriks.Matrik kurang(PenjumlahanDanPengurangan.Matriks.Matrik other) {
        if (this.baris != other.baris || this.kolom != other.kolom) {
            System.out.println("Ukuran matriks tidak sesuai");
            return null;
        }
        PenjumlahanDanPengurangan.Matriks.Matrik hasil = new PenjumlahanDanPengurangan.Matriks.Matrik(this.baris, this.kolom);
        for (int i = 0; i < baris; i++) {
            for (int j = 0; j < kolom; j++) {
                hasil.data[i][j] = this.data[i][j].kurang(other.data[i][j]);
            }
        }
        return hasil;
    }

    public Pecahan dotProduct(PenjumlahanDanPengurangan.Matriks.Matrik other, int barisKedua) {
        if (this.kolom != other.baris) {
            System.out.println("Ukuran matriks tidak sesuai");
            return null;
        }
        Pecahan hasil = new Pecahan(0, 1);
        for (int i = 0; i < kolom; i++) {
            hasil = hasil.tambah(this.data[barisKedua][i].kali(other.data[i][0]));
        }
        return hasil;
    }

    public PenjumlahanDanPengurangan.Matriks.Matrik transpose() {
        PenjumlahanDanPengurangan.Matriks.Matrik hasil = new PenjumlahanDanPengurangan.Matriks.Matrik(kolom, baris);
        for (int i = 0; i < baris; i++) {
            for (int j = 0; j < kolom; j++) {
                hasil.data[j][i] = this.data[i][j];
            }
        }
        return hasil;
    }

    public PenjumlahanDanPengurangan.Matriks.Matrik invers() {
        // Implementasikan perhitungan invers matriks di sini.
        // Ini adalah tugas yang cukup kompleks dan melibatkan aljabar linear.
        return null;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < baris; i++) {
            for (int j = 0; j < kolom; j++) {
                sb.append(data[i][j].toString()).append(" ");
            }
            sb.append("\n");
        }
        return sb.toString();
    }

    public void setData(Pecahan[][] data) {
        if (data.length != baris || data[0].length != kolom) {
            System.out.println("Ukuran data tidak sesuai");
            return;
        }
        this.data = data;
    }
}
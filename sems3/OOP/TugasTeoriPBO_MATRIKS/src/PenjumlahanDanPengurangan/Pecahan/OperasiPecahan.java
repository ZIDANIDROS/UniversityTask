package PenjumlahanDanPengurangan.Pecahan;

public class OperasiPecahan {
    private int pembilang;
    private int penyebut;

    public OperasiPecahan(int pembilang, int penyebut) {
        this.pembilang = pembilang;
        this.penyebut = penyebut;
    }

    public OperasiPecahan tambah(OperasiPecahan other) {
        int newPembilang = (this.pembilang * other.penyebut) + (other.pembilang * this.penyebut);
        int newPenyebut = this.penyebut * other.penyebut;
        return sederhanakan(new OperasiPecahan(newPembilang, newPenyebut));
    }

    public OperasiPecahan kurang(OperasiPecahan other) {
        int newPembilang = (this.pembilang * other.penyebut) - (other.pembilang * this.penyebut);
        int newPenyebut = this.penyebut * other.penyebut;
        return sederhanakan(new OperasiPecahan(newPembilang, newPenyebut));
    }

    public OperasiPecahan kali(OperasiPecahan other) {
        int newPembilang = this.pembilang * other.pembilang;
        int newPenyebut = this.penyebut * other.penyebut;
        return sederhanakan(new OperasiPecahan(newPembilang, newPenyebut));
    }

    public OperasiPecahan bagi(OperasiPecahan other) {
        int newPembilang = this.pembilang * other.penyebut;
        int newPenyebut = this.penyebut * other.pembilang;
        return sederhanakan(new OperasiPecahan(newPembilang, newPenyebut));
    }

    private int fpb(int a, int b) {
        if (b == 0) {
            return a;
        }
        return fpb(b, a % b);
    }

    private OperasiPecahan sederhanakan(OperasiPecahan pecahan) {
        int common = fpb(pecahan.pembilang, pecahan.penyebut);
        pecahan.pembilang /= common;
        pecahan.penyebut /= common;
        return pecahan;
    }

    @Override
    public String toString() {
        return pembilang + "/" + penyebut;
    }
}

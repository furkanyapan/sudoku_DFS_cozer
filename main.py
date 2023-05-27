import numpy as np
import time

def mevcut_satir(tamamlanmis_tablo, indeks, deger):
    if deger in tamamlanmis_tablo[indeks[0], :]:
        return True
    return False

def mevcut_sutun(tamamlanmis_tablo, indeks, deger):
    if deger in tamamlanmis_tablo[:, indeks[1]]:
        return True
    return False

def mevcut_alt_dizi(tamamlanmis_tablo, indeks, deger):
    for i in range((indeks[0] - indeks[0] % 3), (indeks[0] - indeks[0] % 3) + 3):
        for j in range((indeks[1] - indeks[1] % 3), (indeks[1] - indeks[1] % 3) + 3):
            if deger == tamamlanmis_tablo[i][j]:
                return True
    return False

def kontrol(tamamlanmis_tablo, deger, indeks):
    if not mevcut_satir(tamamlanmis_tablo, indeks, deger) and not mevcut_alt_dizi(tamamlanmis_tablo, indeks, deger) \
            and not mevcut_sutun(tamamlanmis_tablo, indeks, deger):
        return True
    else:
        return False

def sifirlari_bul(tablo):
    for i in range(9):
        for j in range(9):
            if tablo[i][j] == 0:
                return [i, j]
    return None

def sudoku_dfs(tamamlanmis_tablo):
    sifir_indeksleri = sifirlari_bul(tamamlanmis_tablo)
    if sifir_indeksleri is None:
        return True
    i, j = sifir_indeksleri
    for deger in range(1, 10):
        if kontrol(tamamlanmis_tablo, deger, (i, j)):
            tamamlanmis_tablo[i, j] = deger
            print(f"{deger} değeri, {i+1}. satır ve {j+1}. sütuna yerleştirildi.")
            time.sleep(0.25)
            print(tamamlanmis_tablo)
            if sudoku_dfs(tamamlanmis_tablo):
                return True
            print(f"{deger} değeri, {i+1}. satır ve {j+1}. sütundan kaldırıldı. Geri dönülüyor.")
            tamamlanmis_tablo[i, j] = 0
    return False

def main():
    baslangic_zamani = time.time()
    tablo = np.array([[9, 0, 0, 1, 7, 0, 4, 0, 2],
                      [1, 6, 0, 0, 4, 0, 0, 9, 5],
                      [0, 0, 8, 0, 0, 3, 0, 0, 0],
                      [0, 1, 0, 9, 0, 0, 5, 7, 3],
                      [0, 4, 0, 0, 0, 0, 0, 2, 0],
                      [5, 8, 9, 0, 0, 7, 0, 1, 0],
                      [0, 0, 0, 4, 0, 0, 7, 0, 0],
                      [6, 7, 0, 0, 2, 0, 0, 5, 8],
                      [3, 0, 1, 0, 5, 8, 0, 0, 6]])

    if sudoku_dfs(tablo):
        bitis_zamani = time.time()
        print("Arama tamamlandı!")
        print("Toplam geçen süre", round(((bitis_zamani - baslangic_zamani) * 1000), 2), "milisaniyeydi!")
        print("Tamamlanmış Sudoku Bulmacası:")
        print(tablo)
    else:
        print("Bu Sudoku bulmacasının çözümü yok.")

if __name__ == "__main__":
    main()

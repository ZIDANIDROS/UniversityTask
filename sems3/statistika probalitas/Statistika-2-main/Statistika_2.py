import pandas as pd
import math
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np

# 1. Memasukkan data
def input_data():
    data = []
    n = int(input("Masukkan jumlah data: "))
    for i in range(n):
        angka = float(input(f"Masukkan data ke-{i + 1}: "))
        data.append(angka)
    return data

# 2. Mencari nilai Minimum
def find_min(numbers):
    return min(numbers)

# 3. Mencari nilai Maksimum
def find_max(numbers):
    return max(numbers)

# 4. Mencari range (R)
def find_range(numbers):
    return find_max(numbers) - find_min(numbers)

# 5. Mencari total frekuensi (N)
def find_total_frequency(numbers):
    return len(numbers)

# 6. Mencari banyak baris kelas (K)
def find_number_of_classes(numbers):
    return round(1 + 3.3 * math.log10(len(numbers)))

# 7. Mencari C = R/K
def find_class_length(class_range, number_of_classes):
    return round(class_range / number_of_classes)

# 8. Tabel batas kelas Batas Kelas, Tepi Kelas, & Interval Kelas
def find_class_limits(numbers, number_of_classes, class_length):
    bot_limit = [0] * number_of_classes
    top_limit = [0] * number_of_classes
    min_value = find_min(numbers)

    for i in range(number_of_classes):
        if i == 0:
            bot_limit[i] = min_value
            top_limit[i] = min_value + (class_length - 1)
        else:
            bot_limit[i] = top_limit[i - 1] + 1
            top_limit[i] = bot_limit[i] + (class_length - 1)

    return bot_limit, top_limit

def find_class_edges(class_limits, number_of_classes):
    bot_limit = class_limits[0]
    top_limit = class_limits[1]
    bot_edge = [0] * number_of_classes
    top_edge = [0] * number_of_classes
    for i in range(number_of_classes):
        bot_edge[i] = bot_limit[i] - 0.5
        top_edge[i] = top_limit[i] + 0.5
    return bot_edge, top_edge

def find_class_intervals(class_limits):
    bot_limit = class_limits[0]
    top_limit = class_limits[1]
    intervals = [0] * len(class_limits[0])
    for i in range(len(class_limits[0])):
        intervals[i] = "%3d - %3d" % (bot_limit[i], top_limit[i])
    return intervals

# Main program
data = input_data()
class_range = find_range(data)
number_of_classes = find_number_of_classes(data)
class_length = find_class_length(class_range, number_of_classes)
class_limits = find_class_limits(data, number_of_classes, class_length)
class_edges = find_class_edges(class_limits, number_of_classes)
class_intervals = find_class_intervals(class_limits)

###########################  MENAMPILKAN HASIL KE-1 #########################
print("")
print("Hasil Dari Masukan Data")
print(f"Data                  : {data}")
print(f"Minimum               : {find_min(data)}")
print(f"Maximum               : {find_max(data)}")
print(f"Range (R)             : {class_range}")
print(f"Total Frekuensi (N)   : {find_total_frequency(data)}")
print(f"Banyak Baris Kelas (K): {number_of_classes}")
print(f"C (R/K)               : {class_length}")

# Menampilkan tabel batas kelas dengan garis pembatas
print("")
print("Tabel Batas Kelas dan Tepi Kelas")
df_class = pd.DataFrame({
    'Batas Kelas': class_intervals,
    'Tepi Kelas Bawah': class_edges[0],
    'Tepi Kelas Atas': class_edges[1]
})
table_class = tabulate(df_class, headers='keys', tablefmt='fancy_grid', showindex=False)
print(table_class)
print("\n")

# 9. Menghitung frekuensi
def frequency(numbers, number_of_classes, class_limit):
    bot_limit = class_limit[0]
    top_limit = class_limit[1]
    frequency = [0] * number_of_classes
    for i in range(number_of_classes):
        for j in range(len(numbers)):
            if bot_limit[i] <= numbers[j] <= top_limit[i]:
                frequency[i] += 1
    return frequency

# Hasil
freq = frequency(data, number_of_classes, class_limits)

# 10. Menghitung frekuensi kumulatif
def cumulative_frequency(freq):
    cumulative_freq1 = [0] * len(freq)
    cumulative_freq2 = [0] * len(freq)
    for i in range(len(freq)):
        if i == 0:
            cumulative_freq1[i] = freq[i]
            cumulative_freq2[i] = sum(freq)
        else:
            cumulative_freq1[i] = cumulative_freq1[i - 1] + freq[i]
            cumulative_freq2[i] = cumulative_freq2[i - 1] - freq[i - 1]
    return cumulative_freq1, cumulative_freq2

# Hasil
cumulative_freq = cumulative_frequency(freq)

# 11. Menghitung frekuensi relatif
def relative_frequency(freq):
    relative_freq = [0] * len(freq)
    total_freq = sum(freq)
    for i in range(len(freq)):
        relative_freq[i] = (freq[i] / total_freq) * 100
    return relative_freq

# Hasil
relative_freq = relative_frequency(freq)

# 12. Menghitung frekuensi kumulatif relatif
def cumulative_relative_frequency(freq, cumulative_freq):
    cumulative_freq1 = cumulative_freq[0]
    cumulative_freq2 = cumulative_freq[1]
    total_freq = sum(freq)
    relative_cumulative_freq1 = [0] * len(freq)
    relative_cumulative_freq2 = [0] * len(freq)
    for i in range(len(freq)):
        relative_cumulative_freq1[i] = (cumulative_freq1[i] / total_freq) * 100
        relative_cumulative_freq2[i] = (cumulative_freq2[i] / total_freq) * 100
    return relative_cumulative_freq1, relative_cumulative_freq2

# Hasil
cumulative_relative_freq = cumulative_relative_frequency(freq, cumulative_freq)

# Membuat DataFrame untuk tabel frekuensi
df_freq = pd.DataFrame({
    'Batas Kelas': class_intervals,
    'Frekuensi': freq,
    'Frekuensi Kumulatif': cumulative_freq[0],
    'Frekuensi Kumulatif Terbalik': cumulative_freq[1],
    'Frekuensi Relatif (%)': relative_freq,
    'Frekuensi Kumulatif Relatif (%)': cumulative_relative_freq[0],
    'Frekuensi Kumulatif Relatif Terbalik (%)': cumulative_relative_freq[1]
})

# 13. Menampilkan tabel frekuensi dengan garis pembatas
print("Tabel Frekuensi, Frekuensi Kumulatif, Frekuensi Relatif, & Frekuensi Kumulatif Relatif")
table_freq = tabulate(df_freq, headers='keys', tablefmt='fancy_grid', showindex=False)
print(table_freq)

# 14. membuat Fungsi MEAN
def mean(numbers):
    return sum(numbers) / len(numbers)

# 15. membuat Fungsi MEDIAN
def median(numbers):
    n = len(numbers)
    if n % 2:
        return sorted(numbers)[n // 2]
    else:
        x = sorted(numbers)[(n // 2) - 1]
        y = sorted(numbers)[n // 2]
        return (x + y) / 2

# 16. membuat Fungsi MODUS
def mode(numbers):
    mode = [0, 0]
    for num in numbers:
        frequency = numbers.count(num)
        if frequency >= mode[1]:
            mode = [num, frequency]
    return mode[0]

# 17. Fungsi untuk menghitung quartile
def calculate_quartile(data, i_K):
    # Mengurutkan data
    sorted_data = sorted(data)

    n = len(sorted_data)

    # Menghitung posisi kuartil
    position = i_K / 4 * (n + 1)

    # Mencari indeks data yang mendekati posisi kuartil
    k = int(position)

    # Menghitung fraksional bagian dari posisi kuartil
    fract = position - k

    # Mengambil data yang mendekati kuartil
    quartile_value = sorted_data[k - 1] + fract * (sorted_data[k] - sorted_data[k - 1])

    return quartile_value

i_K = int(input("Masukkan nilai i (1, 2, atau 3) untuk menghitung quartil: "))
quartile_value = calculate_quartile(data, i_K)

# 18. Fungsi untuk menghitung Desail
def calculate_Desil(data, i_D):
    # Mengurutkan data
    sorted_data = sorted(data)

    n = len(sorted_data)

    # Menghitung posisi Desil
    position = i_D / 10 * (n + 1)

    # Mencari indeks data yang mendekati posisi Desil
    d = int(position)

    # Menghitung fraksional bagian dari posisi Desil
    fract = position - d

    # Mengambil data yang mendekati Desil
    desil_value = sorted_data[d - 1] + fract * (sorted_data[d] - sorted_data[d - 1])

    return desil_value

i_D = int(input("Masukkan nilai i (1, 2, atau 3) untuk menghitung desil: "))
desil_value = calculate_Desil(data, i_D)

# 19. Fungsi untuk menghitung Persil
def calculate_Persil(data, i_P):
    # Mengurutkan data
    sorted_data = sorted(data)

    n = len(sorted_data)

    # Menghitung posisi Desil
    position = i_P / 100 * (n + 1)

    # Mencari indeks data yang mendekati posisi Desil
    p = int(position)

    # Menghitung fraksional bagian dari posisi Desil
    fract = position - p

    # Mengambil data yang mendekati Desil
    desil_value = sorted_data[p - 1] + fract * (sorted_data[p] - sorted_data[p - 1])

    return desil_value

i_P = int(input("Masukkan nilai i (1, 2, atau 3) untuk menghitung Persil: "))
persil_value = calculate_Persil(data, i_P)

# Menampilkan hasil kuartil
print(f"Kuartil ke-{i_K}      : {quartile_value}")

# Menampilkan hasil Desil
print(f"Desil ke-{i_D}        : {desil_value}")

# Menampilkan hasil Persil
print(f"Persil ke-{i_P}       : {persil_value}")

# 20.Membuat Fungsi Quartil Bawah
def bawah_quartile(data):
    n = len(data)
    return data[n//4-1] + 0.25 * (data[n//4] - data[n//4-1])

# 21.Membuat Fungsi Quartil Atas
def atas_quartile(data):
    n = len(data)
    return data[(n*3)//4-1] + 0.75 * (data[(n*3)//4] - data[(n*3)//4-1])

Q1 = bawah_quartile(data)
Median = median(data)
Q3= atas_quartile(data)

# Membuat box plot
plt.boxplot(data, vert=False)  # vert=False untuk membuat box plot horizontal
plt.title('Box Plot')
plt.xlabel('Nilai')
plt.xticks([min(data), Q1 , Median, Q3, max(data)], ['Min', 'Q1', 'Median', 'Q3', 'Max'])
plt.show()

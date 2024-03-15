import pandas as pd
import matplotlib.pyplot as plt

# Interval data (contoh)
intervals = [16.5, 22.5, 28.5, 34.5, 40.5, 46.5, 52.5]  # Ganti dengan interval data Anda
frequencies = [6, 7, 6, 2, 4, 5]   # Ganti dengan frekuensi data Anda

# Membuat histogram
hist, edges, _ = plt.hist(intervals[:-1], bins=intervals, weights=frequencies, edgecolor='black')
plt.xlabel('Interval')
plt.ylabel('Frekuensi')
plt.title('Histogram')

plt.grid(axis='y', linestyle='--', alpha=0.8, color='black')

# Mengganti label sumbu x dengan nilai tepi kelas saja
plt.xticks(edges, ha='right')
plt.show()
print("   ")

# Generate sample data for positive ogive with modified cumulative frequencies
data = {'Tepi atas': ['22.5', '28.5', '34.5', '40.5', '46.5', '52,5'],
        'Frekuensi': [30, 24, 17, 11, 9, 5]}

# frekuensi kumulatif
desired_cumulative_frequencies = [5, 9, 11, 17, 24, 30]
data['Frekuensi'] = [cum_freq - cum_freq_prev for cum_freq, cum_freq_prev in zip(desired_cumulative_frequencies, [0] + desired_cumulative_frequencies[:-1])]

# membuat frame
df = pd.DataFrame(data)

# menghitung kumulatif relatif
df['Fk >= Ta'] = df['Frekuensi'].iloc[::+1].cumsum()[::+1]

# membuat grafik ogive positiv
plt.figure(figsize=(10,6))
plt.plot(df['Tepi atas'], df['Fk >= Ta'], marker='o')
plt.title('Grafik Ogive Positif')
plt.xlabel('Tepi Atas')
plt.ylabel('Fk >= Ta')
plt.grid(True)

# Display plot
plt.show()
print("   ")

#ogive negatif

data = {'Tepi Bawah': ['16.5', '22.5', '28.5', '34.5', '40.5', '46.5'],
        'Frekuensi': [30, 24, 17, 11, 9, 5]}

desired_cumulative_frequencies = [5, 9, 11, 17, 24, 30]
data['Frekuensi'] = [cum_freq - cum_freq_prev for cum_freq, cum_freq_prev in zip(desired_cumulative_frequencies, [0] + desired_cumulative_frequencies[:-1])]

# menggambar frame
df = pd.DataFrame(data)

# menghitung kumulatif relatif
df['Fk >= Tb'] = df['Frekuensi'].iloc[::-1].cumsum()[::-1]

# membuat grafik ogive negativ
plt.figure(figsize=(10,6))
plt.plot(df['Tepi Bawah'], df['Fk >= Tb'], marker='o')
plt.title('Grafik Ogive Negatif')
plt.xlabel('Tepi Bawah')
plt.ylabel('Fk >= Tb')
plt.grid(True)


#POLIGON

# data poligon
data_x = ['13.5', '19.5', '25.5', '31.5', '37.5', '43.5', '49.5', '55.5']
data_y = [6, 6, 7, 6, 2, 4, 5, 1]

# Menggambar poligon
plt.figure(figsize=(10, 6))
plt.plot(data_x, data_y, marker='o', linestyle='-', color='blue', markersize=8)
plt.fill_between(data_x, data_y, color='blue', alpha=0.3)
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')
plt.title('Poligon Data')
plt.grid(True)


plt.show()

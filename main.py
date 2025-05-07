import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt

# Data dummy untuk kemacetan lalu lintas
data = {
    "Volume_Lalu_Lintas": [1200, 2500, 1800, 3000, 1500, 4000, 3500, 2800, 2000, 2200],  # Kendaraan/jam
    "Kecepatan_Rata_Rata": [40, 25, 30, 20, 35, 15, 18, 22, 28, 30],  # km/jam
    "Kapasitas_Jalan": [2000, 3000, 2500, 3500, 2000, 4500, 4000, 3000, 2800, 3000],  # Kendaraan/jam
    "Jam_Hari": [8, 9, 17, 18, 7, 19, 16, 10, 14, 13],  # Waktu (format 24 jam)
    "Tingkat_Kemacetan": [1, 3, 2, 4, 1, 5, 4, 3, 2, 2],  # Target: 1 (rendah) sampai 5 (parah)
}

# Membuat DataFrame
data_kemacetan = pd.DataFrame(data)

# Memisahkan fitur (X) dan target (y)
X = data_kemacetan[["Volume_Lalu_Lintas", "Kecepatan_Rata_Rata", "Kapasitas_Jalan", "Jam_Hari"]]
y = data_kemacetan["Tingkat_Kemacetan"]

# Membagi data menjadi data latih dan data uji
X_latih, X_uji, y_latih, y_uji = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Random Forest Regressor
model = RandomForestRegressor(random_state=42)
model.fit(X_latih, y_latih)

# Prediksi pada data uji
y_prediksi = model.predict(X_uji)

# Evaluasi model
mae = mean_absolute_error(y_uji, y_prediksi)
rmse = np.sqrt(mean_squared_error(y_uji, y_prediksi))
print(f"Kesalahan Absolut Rata-Rata (MAE): {mae:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")

# Visualisasi hasil prediksi vs nilai aktual
plt.figure(figsize=(10, 6))
plt.plot(range(len(y_uji)), y_uji, label="Aktual", marker='o', color="blue")
plt.plot(range(len(y_prediksi)), y_prediksi, label="Prediksi", marker='x', color="red")
plt.title("Tingkat Kemacetan: Aktual vs Prediksi", fontsize=16)
plt.xlabel("Indeks Data Uji", fontsize=12)
plt.ylabel("Tingkat Kemacetan", fontsize=12)
plt.legend()
plt.grid()
plt.show()

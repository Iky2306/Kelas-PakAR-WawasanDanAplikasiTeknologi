# Sistem Prediksi Tingkat Kemacetan Lalu Lintas

## **Deskripsi Proyek**

Proyek ini bertujuan untuk memprediksi tingkat kemacetan lalu lintas menggunakan **Machine Learning** dengan algoritma Random Forest Regressor. Model dilatih pada data lalu lintas (dummy) dan menghasilkan prediksi berdasarkan volume lalu lintas, kecepatan rata-rata, kapasitas jalan, dan waktu.

---

## **Fitur Utama**

* **Input Data:** Volume lalu lintas, kecepatan rata-rata, kapasitas jalan, dan waktu dalam hari.
* **Model Machine Learning:** Algoritma Random Forest Regressor untuk prediksi tingkat kemacetan (1: rendah hingga 5: parah).
* **Visualisasi:** Grafik membandingkan hasil prediksi dengan data aktual.

---

## **Instalasi**

### **1. Prasyarat**

Pastikan Python (versi 3.8 atau lebih baru) telah terinstal di komputer Anda. Jika belum, unduh dan instal dari [python.org](https://www.python.org/downloads/).

### **2. Buat Virtual Environment** *(Opsional, tetapi direkomendasikan)*

1. Buka terminal/command prompt.
2. Buat virtual environment:

   ```bash
   python -m venv env
   ```
3. Aktifkan virtual environment:

   * **Windows:**

     ```bash
     .\env\Scripts\activate
     ```
   * **Linux/MacOS:**

     ```bash
     source env/bin/activate
     ```

### **3. Instal Pustaka yang Dibutuhkan**

Jalankan perintah berikut untuk menginstal semua pustaka yang diperlukan:

```bash
pip install pandas numpy scikit-learn matplotlib
```

#### **Penjelasan Modul yang Digunakan**

* **pandas:** Untuk memproses dan menganalisis data dalam bentuk tabel.
* **numpy:** Untuk operasi matematika dan manipulasi array.
* **scikit-learn:** Untuk implementasi algoritma Machine Learning, seperti Random Forest Regressor.
* **matplotlib:** Untuk visualisasi data dalam bentuk grafik.

---

## **Cara Menjalankan Program**

1. **Clone Repository atau Salin Kode**
   Pastikan Anda memiliki file Python utama, misalnya `traffic_prediction.py`.

2. **Jalankan Program**
   Pada terminal, pindah ke direktori proyek dan jalankan file:

   ```bash
   python traffic_prediction.py
   ```

3. **Hasil yang Diharapkan**

   * Prediksi tingkat kemacetan ditampilkan di terminal.
   * Grafik membandingkan hasil prediksi dengan data aktual akan muncul.

---

## **Penjelasan Analisis**

### **1. Data yang Digunakan**

Dataset berisi:

* **Volume\_Lalu\_Lintas:** Jumlah kendaraan per jam.
* **Kecepatan\_Rata\_Rata:** Kecepatan kendaraan rata-rata di area tertentu.
* **Kapasitas\_Jalan:** Kapasitas maksimal kendaraan per jam untuk jalan tersebut.
* **Jam\_Hari:** Waktu dalam format 24 jam.
* **Tingkat\_Kemacetan:** Skor kemacetan (1: rendah hingga 5: parah).

### **2. Proses Analisis**

1. **Preprocessing Data:**

   * Membagi data menjadi fitur (X) dan target (y).
   * Membagi dataset menjadi data latih (80%) dan data uji (20%).

2. **Pelatihan Model:**

   * Menggunakan algoritma **Random Forest Regressor**.
   * Model dilatih untuk memprediksi tingkat kemacetan berdasarkan fitur input.

3. **Evaluasi Model:**

   * Menghitung **MAE (Mean Absolute Error)** dan **RMSE (Root Mean Squared Error)** untuk mengevaluasi akurasi model.

4. **Visualisasi:**

   * Membandingkan nilai prediksi dengan nilai aktual dalam grafik untuk memvalidasi performa model.

### **3. Contoh Output**

* **Kesalahan Prediksi:**

  ```
  Kesalahan Absolut Rata-Rata (MAE): 0.75
  Root Mean Squared Error (RMSE): 0.87
  ```
* **Grafik:** Menunjukkan bagaimana prediksi mendekati nilai aktual tingkat kemacetan.

---

## **Pengembangan Lebih Lanjut**

1. **Integrasi Data Real-Time:**

   * Menggunakan data dari API lalu lintas seperti Google Maps API.
   * Menghubungkan model ke sensor IoT untuk input data real-time.

2. **Penambahan Fitur:**

   * Data cuaca untuk memperkaya analisis.
   * Faktor lain seperti hari libur atau konstruksi jalan.

3. **Optimisasi Model:**

   * Eksperimen dengan algoritma lain seperti Gradient Boosting atau Neural Networks.
   * Melakukan hyperparameter tuning untuk Random Forest.

##### Projek ini untuk memenuhi tugas dari mata kuliah WAWASAN DAN APLIKASI TEKNOLOGI
##### Dosen pengampu: Ahmad Roihan, S.Kom.,M.Ti.

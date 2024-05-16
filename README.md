# Fruit and Vegetable Image Classification

## Kelompok 7

### Ketua Kelompok:
- **Marlina** (2108107010009)

### Anggota Kelompok:
- **Nitiya Rihadatul 'Aisy** (2108107010003)
- **Nuzulurrahmah** (2108107010012)
- **Najla Raihana Kamila** (2108107010067)
- **Laila Asrin** (2108107010068)

## Deskripsi Proyek:
Proyek ini merupakan proyek akhir dari praktikum Pembelajaran Mesin. Tujuan utamanya adalah melakukan klasifikasi gambar buah dan sayuran menggunakan teknik pembelajaran mendalam (deep learning) dengan menggunakan TensorFlow untuk membangun arsitektur Convolutional Neural Network (CNN) yang dapat mengekstraksi fitur-fitur yang signifikan dari gambar.

Dataset yang digunakan diambil dari situs Kaggle dan berisi gambar-gambar dari berbagai jenis makanan, antara lain:

- **Fruits:** banana, apple, pear, grapes, orange, kiwi, watermelon, pomegranate, pineapple, mango.
- **Vegetables:** cucumber, carrot, capsicum, onion, potato, lemon, tomato, raddish, beetroot, cabbage, lettuce, spinach, soy bean, cauliflower, bell pepper, chilli pepper, turnip, corn, sweetcorn, sweet potato, paprika, jalepeño, ginger, garlic, peas, eggplant.

Jumlah data yang tersedia adalah sebagai berikut:
- **Data training:** 3115 file yang terdiri dari 36 kelas.
- **Data testing:** 359 file yang terdiri dari 36 kelas.
- **Data validation:** 351 file yang terdiri dari 36 kelas.

## Instalasi

### **1. Clone repositori:**

```bash
git clone https://github.com/your-repo/image-classification-flask.git
cd image-classification-flask
```

### **2. Buat virtual environment dan aktifkan:**

```bash
python -m venv venv
source venv/bin/activate  # Pada Windows, gunakan 'venv\Scripts\activate'
```

### **3. Install paket yang diperlukan:**

```bash
pip install -r requirements.txt
```

### **4. Pastikan file model Anda (`fruitmodel.h5`) ditempatkan di direktori `models`. Jika Anda tidak memiliki file model, Anda perlu melatihnya secara terpisah atau mengunduhnya dari sumber tertentu.**

## **Struktur Direktori**

Pastikan struktur direktori Anda terlihat seperti ini:

```
ImageClassification_ProyekAkhir_Kelompok7/
│
├── app-flask.py
├── models
│   └── fruitmodel.h5
├── templates
│   └── index.html
└── requirements.txt
```

## **Menjalankan Aplikasi**

1. Mulai aplikasi Flask:

```bash
python app.py
```

2. Buka browser web Anda dan navigasikan ke:

```
http://127.0.0.1:5000
```

3. Unggah gambar buah atau sayur dan lihat hasil klasifikasinya.

## **Akses Proyek:**
- **Repositori:** [Link Repositori](https://github.com/marlinaa31/ImageClassification_ProyekAkhir_Kelompok7)
- **Dataset:** [Link Dataset](https://www.kaggle.com/datasets/kritikseth/fruit-and-vegetable-image-recognition)
- **Video:** [Link Video](#)

## **Proyek ini dapat diakses melalui link sebagai berikut:**
- **Deployed App:** [Live App](https://marlinaa31-imageclassification-proyekakhir-kelompok7-app-zswcbb.streamlit.app/)
```


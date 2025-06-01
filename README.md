# TUGAS BESAR 1 STRATEGI ALGORITMA IF2211
## Pemanfaatan Algoritma Greedy dalam pembuatan bot permainan Diamonds
## Kelompok Mangu
## Kelas RC
---

### Anggota Kelompok

| Nama                          | NIM         |
|-------------------------------|-------------|
| Afifa Aulia                   | 123140073   |
| Bening Apni Prameswari        | 123140089   |
| Raisya Syifa Saleh            | 123140169   |

---

## Deskripsi Singkat

**Diamonds** adalah sebuah tantangan pemrograman di mana kamu akan membuat bot untuk mengumpulkan diamond sebanyak mungkin dalam grid permainan sambil bersaing melawan bot milik peserta lain. Bot yang kamu buat harus mampu mengatur arah gerak, menghindari musuh, serta kembali ke base untuk menyetorkan poin — semua itu dalam waktu terbatas.

Repositori ini berisi implementasi strategi **Greedy by Point per Distance** (alias Highest Density), yaitu strategi yang memilih diamond berdasarkan **rasio poin / jarak tempuh terbaik** agar lebih efisien.

---

## Struktur Folder

```
tubes1-IF2211-bot-starter-pack-1.0.1/
├── __pycache__/
│   └── decode.cpython-313.pyc
├── game/
│   ├── __pycache__/
│   ├── logic/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── greedybot.py
│   │   ├── mybot.py
│   │   ├── random.py
│   ├── __init__.py
│   ├── api.py
│   ├── board_handler.py
│   ├── bot_handler.py
│   ├── models.py
│   ├── util.py
├── .gitignore
├── decode.py
├── main.py
├── README.md
├── requirements.txt
├── run-bots.bat
└── run-bots.sh
```

## Kebutuhan Sistem

### Game Engine:
- Node.js
- Docker Desktop
- Yarn (install dengan: `npm install --global yarn`)

### Bot Starter Pack:
- Python 3.13

---

## Cara Menjalankan Game Engine

1. Download file `.zip` game engine dari:
   [Game Engine v1.1.0](https://github.com/haziqam/tubes1-IF2211-game-engine/releases/tag/v1.1.0)

2. Ekstrak dan masuk ke folder hasil ekstrak:

```bash
cd tubes1-IF2110-game-engine-1.1.0
```

3. Jalankan perintah-perintah berikut:

```bash
yarn
./scripts/copy-env.bat
docker compose up -d database
./scripts/setup-db-prisma.bat
npm run build
npm run start
```

> Note:  Pastikan Docker Desktop sudah berjalan sebelum menjalankan perintah database.

---

## Cara Menjalankan Bot Starter Pack

1. Download starter pack bot dari:
   [Bot Starter Pack v1.0.1](https://github.com/haziqam/tubes1-IF2211-bot-starter-pack/releases/tag/v1.0.1)

2. Ekstrak dan masuk ke folder:

```bash
cd tubes1-IF2211-bot-starter-pack-1.0.1
```

3. Install dependency:

```bash
pip install -r requirements.txt
```

4. Jalankan satu bot:

```bash
python main.py --logic MyBot --email=greedy@bot.com --name="GreedyBot" --password=123 --team=etimo
```

5. Menjalankan banyak bot:

```bash
./run-bots.bat    # Windows
./run-bots.sh     # Linux/macOS
```

> Gunakan `chmod +x run-bots.sh` jika .sh script belum bisa dijalankan.

---

## Strategi yang Digunakan

Berdasarkan hasil analisis dan pengujian, strategi Greedy yang kami gunakan adalah gabungan dari dua pendekatan:

### Greedy by Point per Distance

Bot menghitung rasio antara poin diamond dengan jarak (menggunakan Manhattan Distance) dari posisi bot ke diamond. Semua diamond kemudian diurutkan berdasarkan rasio ini, sehingga diamond yang **paling menguntungkan secara efisiensi** akan diprioritaskan.

Dengan strategi ini, bot dapat:
- Mengumpulkan lebih banyak poin dalam langkah seminimal mungkin
- Fokus pada target bernilai tinggi dan mudah dijangkau
- Menghindari pemborosan langkah untuk diamond yang terlalu jauh

### Greedy by Base Distance

Jika bot sudah membawa 3 diamond (inventory penuh), maka bot akan segera kembali ke base untuk menyetorkan diamond sebelum mengambil yang lain. Strategi ini penting untuk:
- Menghindari kehilangan diamond karena tackle oleh bot musuh
- Menjamin konversi diamond menjadi poin
- Meminimalkan risiko saat inventory penuh

Gabungan dari dua strategi ini membuat bot efisien, responsif, dan aman dalam menghadapi dinamika permainan.

---

## Pengujian

Bot telah diuji dan menunjukkan hasil:

- Tidak stuck dalam kondisi board kosong atau penuh
- Konsisten mengumpulkan poin tinggi
- Dapat kembali ke base tepat waktu
- Efisien dalam penggunaan inventory
- Tidak mudah ditackle karena menghindari musuh

---

## Informasi Tambahan

Tugas ini dibuat untuk memenuhi **Tugas Besar 1 mata kuliah IF2211 Strategi Algoritma** - Program Studi Teknik Informatika, Institut Teknologi Sumatera.

Game engine dikembangkan oleh [Etimo](https://github.com/Etimo/diamonds2) dan dimodifikasi untuk keperluan akademik.

---

© 2025 – Kelompok Mangu – Strategi Algoritma

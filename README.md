# Erajaya Backend Developer Assessment Test

## Deskripsi
Repository ini berisi source code yang ditulis untuk menjawab sebanyak dua pertanyaan yaitu:
1. Buat Sebuah REST API dengan bahasa pemrograman Python, framework flask, dan database MySQL atau PostgreSQL.
2. Buat sebanyak dua buah endpoint:
   - API add product
   - API list product dengan sorting
     - Mendapatkan semua daftar product
     - Urut berdasarkan product terbaru
     - Urut berdasarkan harga termurah
     - Urut berdasarkan harga termahal
     - Urut Berdasarkan nama product (A-Z) & (Z-A)

Berdasarkan Spesifikasi product sebagai berikut:
- Product ID
- Product name
- Product price
- Product description
- Product quantity

## Arsitektur 
Repository &rarr; Service &rarr; Controller
<br>Alasan:
1. Arsitektur ini diterapkan adalah agar dapat memisahkan proses bisnis dan tanggung jawab menjadi beberapa Layer. 
2. Repository layer bertanggung jawab untuk menyimpan data ke dalam database.
3. Service layer bertanggung jawab terhadap semua proses bisnis yang melibatkan logika. 
4. Controller layer bertanggung jawab untuk menerima HTTP request dari client dan meneruskan HTTP response dari service layer.

## Tools yang digunakan
1. Database: PostgreSQL
2. Database Adapter: Psycopg2
3. Backend Framework: Flask
4. SQL Toolkit & ORM: Flask SQLAlchemy & Marshmallow
5. Environment Variables: Python-dotenv

## Checklist
- [x] API add product
- [x] API list product dengan sorting
- [x] Sort berdasarkan produk terbaru
- [x] Sort berdasarkan harga termahal
- [x] Sort berdasarkan nama product (A-Z)
- [x] Sort berdasarkan nama product (Z-A)
- [x] Implement Docker
- [ ] Implement Redis cache

## Cara Menggunakan
> Syarat: Pastikan sudah menginstall Python, PostgreSQL dan Docker sebelum menjalankan source code ini.

Ada dua cara untuk menjalankan source code ini:

### 1. Local Environment
1. Clone repository ini.
2. Rename file `env.example` menjadi `.env`
3. Buka file `.env` dan tambahkan PostgreSQL URI pada variabel `PGSQL_URI` mengikuti pola berikut:
   <pre><code>postgresql://username:password@hostname:port/db_name?sslmode=disable</code></pre>
    sesuaikan `username`, `password`, `hostname`, `port`, dan `db_name` dengan konfigurasi yang anda miliki.

1. Buka terminal lalu ketik `make init` untuk menginstall dependencies.
2. Ketik `make local_run` untuk menjalankan server.
3. Server dapat di akses dengan alamat `http://localhost:8080`
   
### 2. Docker Container
1. Clone repository ini.
2. Buka terminal lalu ketik `make container_run` agar server berjalan di dalam docker container.
3. Server dapat di akses dengan alamat `http://localhost:8081`

## API Endpoints
> Catatan: Semua endpoint diawali dari prefiks: `/api/v1`

1. `/products`
<br>method: POST
<br>Deskripsi: Menambah produk baru
<br> Request Body (JSON):

    | Field        | Tipe Data | Kriteria                 |
    |--------------|-----------|--------------------------|
    | product_name | str       | Required, min=2, max=128 |
    | price        | int       | Required                 |
    | description  | str       | Required, min=10         |
    | quantity     | int       | Required                 |

    Contoh request (dengan menggunakan cURL):
    <pre><code>curl -X POST localhost:8080/api/v1/products \
    -L -H 'Content-Type: application/json' \
    -d '{"product_name":"Redmi Note 10","price":2500000, "description":"mid-range phone", "quantity": 15}'</code></pre>

2. `/products`
<br>Method: GET
<br>Deskripsi: Mendapatkan semua daftar product

    Contoh request (dengan menggunakan cURL):
    <pre><code>curl -L -X GET localhost:8080/api/v1/products</code></pre>

    Untuk mendapatkan data berdasarkan hasil sorting, cukup dengan menambahkan query string `orderBy`:
   1. Urut berdasarkan produk terbaru
      - `/products?orderBy=latest`
       <pre><code>curl -G -d 'orderBy=latest' -L -X GET localhost:8080/api/v1/products</code></pre>
   2. Urut berdasarkan harga termurah
      - `/products?orderBy=min`
       <pre><code>curl -G -d 'orderBy=min' -L -X GET localhost:8080/api/v1/products</code></pre>
   3. Urut berdasarkan harga termahal
      - `/products?orderBy=max`
       <pre><code>curl -G -d 'orderBy=max' -L -X GET localhost:8080/api/v1/products</code></pre>
   4. Urut berdasarkan nama product (A-Z)
      - `/products?orderBy=asc`
       <pre><code>curl -G -d 'orderBy=asc' -L -X GET localhost:8080/api/v1/products</code></pre>
   5. Urut berdasarkan nama product (Z-A)
      - `/products?orderBy=desc`
       <pre><code>curl -G -d 'orderBy=desc' -L -X GET localhost:8080/api/v1/products</code></pre>

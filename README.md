# KULI-AH
Program ini dibuat untuk memenuhi salah satu tugas kecil mata kuliah IF2211 Strategi Algoritma. Program ini adalah program untuk menyusunn sebuah rencana kuliah dengan menggunakan Topological Sort. Program ini berasumsi bahwa input selalu dapat dijadikan sebuah Directed Acyclic Graph (DAG)

## Algoritma Decrease and Conquer yang Digunakan
ALgoritma Decerase and Conquer digunakan saat mengurutkan mata kuliah yang ada. Langkah-langkah yang dilakukan adalah sebagai berikut:
1. Mengambil semua mata kuliah yang saat ini tidak memiliki prerequisite dan mengeluarkannya dari list seluruh mata kuliah
2. Mengurangi jumlah prerequisite dari mata kuliah yang belum diambil berdasarkan mata kuliah yang sekarang diambil
3. Ulangi langkah 1 dan 2 pada list mata kuliah yang tersisa sisanya hingga semua mata kuliah sudah terpilih

Ini merupakan algoritma Decrease and Conquer varian 'Decrease by a variable size' karena pada setiap iterasi, jumlah mata kuliah yang tidak memiliki prerequisite yang belum diambil dapat berubah-ubah.

## Requirements
Python 3

## Cara Menggunakan Program
Jalankan file main.py dalam folder src, kemudian masukkan nama file problem yang ingin dicari solusinya. File problem harus berada pada folder test dan mengikuti template yang sudah ada.

## Author
Reyhan Emyr Arrosyid - 13519167

meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "Tanggapan terhadap lelucon",
            "CREEPY": "Menakutkan, tidak menyenangkan",
            "AGGRO": "Untuk menjadi agresif/marah",
            "SHEESH": "Sedikit ketidaksetujuan",
            "OTW": "Pergi ke sesuatu tempat",
            }

for i in range (5):
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

    if word in meme_dict.keys():
        # Apa yang harus kita lakukan jika kata itu ditemukan?
        print("ARTINYA:")
        print(meme_dict[word])

    else:
        # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
        print("MAAF KATA BELUM TERSEDIA/BELUM DI UPDATE")

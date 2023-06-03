import tkinter as tk
import random

# Oyun ayarları
WIDTH, HEIGHT = 800, 600
WORD_SPEED = 2

# Seviyeler ve kelimelerin uzunlukları
levels = {
    1: 4,
    2: 5,
    3: 6,
    4: 7,
    5: 8,
    6: 9,
    7: 10
}

# Kelimelerin listesi
words = {
    1: ['elma', 'armut', 'kiraz', 'üzüm', 'muz', 'nar', 'kivi', 'erik'],
    2: ['masa', 'sandalye', 'koltuk', 'yatak', 'raflar', 'televizyon'],
    3: ['kitap', 'defter', 'kalem', 'silgi', 'çanta', 'kalemlik', 'defterlik'],
    4: ['okul', 'öğrenci', 'öğretmen', 'sınıf', 'tahta', 'kantin'],
    5: ['bilgisayar', 'klavye', 'fare', 'monitör', 'hoparlör', 'kulaklık'],
    6: ['gözlük', 'saat', 'kolye', 'yüzük', 'bilezik', 'kemer', 'cüzdan'],
    7: ['araba', 'bisiklet', 'motor', 'uçak', 'gemi', 'tren', 'otobüs']
}

# Pencere oluşturma
window = tk.Tk()
window.title("Type Game")
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

# Seviye ve kelime uzunluğunu belirleme
level = 1
word_length = levels[level]

# Aktif kelimeyi rastgele seçme
active_word = random.choice(words[word_length])
active_word_x = WIDTH // 2
active_word_y = 0

# Puan ve geçen süre
score = 0

# Oyun döngüsü
def game_loop():
    global active_word_x, active_word_y, score, active_word, level
    
    # Kelimeyi aşağı hareket ettirme
    active_word_y += WORD_SPEED
    
    # Ekrandaki kelimeyi güncelleme
    canvas.delete("active_word")
    canvas.create_text(active_word_x, active_word_y, text=active_word, fill="black", font=("Arial", 32), tags="active_word")
    
    # Kelimenin ekranın alt tarafına ulaşması durumu
    if active_word_y > HEIGHT:
        # Yeni kelime seçme
        if score < 10 and level < 7:
            level += 1
            word_length = levels[level]
        active_word = random.choice(words[word_length])
        active_word_x = random.randint(0, WIDTH)
        active_word_y = 0
    
    # Puanı ve geçen süreyi güncelleme
    score_label.config(text=f"Score: {score}")
    
    # Oyun döngüsünü tekrar çağırma
   

    window.after(10, game_loop)

# Olay işleme
def handle_key(event):
    global score, active_word
    
    if event.char == active_word[0]:
        active_word = active_word[1:]
        if len(active_word) == 0:
            score += 1
            active_word = random.choice(words)
            active_word_x = WIDTH
            active_word_y = random.randint(HEIGHT // 4, 3 * HEIGHT // 4)

# Olay dinleyicisi ekleme
window.bind("<Key>", handle_key)

# Skor etiketi
score_label = tk.Label(window, text="Score: 0", font=("Arial", 16))
score_label.pack()

# Oyun döngüsünü başlatma
game_loop()

# Pencereyi gösterme
window.mainloop()

from PIL import Image, ImageDraw
import math

# Ukuran gambar
WIDTH, HEIGHT = 800, 800

# Buat kanvas baru dengan latar belakang gelap
img = Image.new("RGB", (WIDTH, HEIGHT), "#0a0a23")
draw = ImageDraw.Draw(img)

# Fungsi untuk membuat warna gradasi
def get_color(t, max_t):
    r = int(255 * abs(math.sin(t / max_t * math.pi)))
    g = int(200 * abs(math.sin((t / max_t + 0.33) * math.pi)))
    b = int(255 * abs(math.cos((t / max_t + 0.66) * math.pi)))
    return (r, g, b)

# Gambar pola bunga spiral yang memukau
cx, cy = WIDTH // 2, HEIGHT // 2
total_points = 1200

for i in range(total_points):
    t = i * 0.06
    r = i * 0.35
    x = cx + r * math.cos(t)
    y = cy + r * math.sin(t)
    warna = get_color(i, total_points)
    ukuran_titik = max(1, 6 - i // 200)
    draw.ellipse(
        [x - ukuran_titik, y - ukuran_titik, x + ukuran_titik, y + ukuran_titik],
        fill=warna
    )

# Simpan gambar
import os
os.makedirs("output", exist_ok=True)
img.save("output/entry.png")
print("🎉 Selesai! Gambar disimpan di output/entry.png")
print("✨ Semoga menang ya! Semangat!")

import turtle

def persegi_panjang(warna, x, y, lebar, tinggi):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(warna)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(lebar)
        turtle.left(90)
    turtle.end_fill()

def buat_papan_catur(baris, kolom, lebar_kotak):
    warna_putih = "white"
    warna_hitam = "black"
    warna_latar_belakang = "tan"  # Coklat muda

    for i in range(baris):
        for j in range(kolom):
            x = j * lebar_kotak
            y = -i * lebar_kotak
            if (i + j) % 2 == 0:
                persegi_panjang(warna_hitam, x, y, lebar_kotak, lebar_kotak)
            else:
                persegi_panjang(warna_putih, x, y, lebar_kotak, lebar_kotak)

def main():
    turtle.speed(-3)
    turtle.hideturtle()
    
    baris = 6
    kolom = 9
    lebar_kotak = 60

    turtle.bgcolor("tan")  # Coklat muda
    buat_papan_catur(baris, kolom, lebar_kotak)

    turtle.exitonclick()

if __name__ == "__main__":
    main()

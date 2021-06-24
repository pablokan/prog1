import qrcode
image = qrcode.make("http://www.itecriocuarto.org.ar")
image.save("peql.png")


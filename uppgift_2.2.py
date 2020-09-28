
# Kod som beräknar volym och area på en sfär

volym = False
area = False

radie = input("Vad är sfärens radie?")

radie = float(radie)

radie = radie * radie * radie

area = float(4) * 3.14 * radie

volym = 4 * 3.14 * radie

volym = volym / 3

print("Sfärens area är ", area)

print("Sfärens volym är ", volym)


#miniräknare

timer = 500000
running = True

print("Välj Räknesätt:")
fråga1 = False

atimer = 8000000
stimer = 8000000

while running == True:
    while timer > -1:
        if timer == 0:
            print("skriv 'plus' för addition")
            print("skriv 'minus' för subtraktion")
            fråga1 = input()
        timer -= 1
    if fråga1 == "plus":
        print("Skriv in tal nummer ett:")
        fråga2 = input()
        print("Skriv in tal nummer två:")
        fråga3 = input()
        print("Calculating....")
        fråga1 = "gg"
    if fråga1 == "gg":
        if atimer > 0:
            atimer -= 1
        if atimer == 0:
            fråga2 = float(fråga2)
            fråga3 = float(fråga3)
            print(fråga2 + fråga3)
            atimer = -5
    
    if fråga1 == "minus":
        print("Skriv in tal nummer ett:")
        fråga2 = input()
        print("Skriv in tal nummer två:")
        fråga3 = input()
        print("Calculating....")
        fråga1 = "ggg"
    if fråga1 == "ggg":
        if stimer > 0:
            stimer -= 1
        if stimer == 0:
            fråga2 = float(fråga2)
            fråga3 = float(fråga3)
            print(fråga2 - fråga3)
            stimer = -5








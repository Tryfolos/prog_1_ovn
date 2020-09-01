#miniräknare

import time
import os

timer = 500000
running = True
start_countdown = False
reset_timer = 1
error = False

fråga1 = False

atimer = 8000000
stimer = 8000000

while running == True:
    while timer > -1:
        if timer == 0:
            print("Välj Räknesätt:")
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
            start_countdown = True
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
            start_countdown = True
            stimer = -5

    if fråga1 != "plus":
        if fråga1 != "minus":
            if fråga1 != False: 
                if fråga1 != "gg":
                    if fråga1 != "ggg":
                        error = True
                        if error == True:
                            os.system("color c")
                            print("error: Det räknesättet finns inte")
                            error = False
                            atimer = 8000000
                            stimer = 8000000
                            timer = 500000
                            fråga1 = False
                            time.sleep(2.5)
                            os.system("color 7")
                            

    if start_countdown == True:
        time.sleep(1)
        reset_timer = 0
    if reset_timer == 0:
        atimer = 8000000
        stimer = 8000000
        timer = 500000
        fråga1 = False
        start_countdown = False
        reset_timer = 1





import random

from player import Player
from rooms.room import Room

if __name__ == "__main__":

    Atrio = Room("Atrio", None, None, None, None)
    Segreteria = Room("Segreteria", None, None, None, None)
    AreaRelax = Room("Area relax", None, None, None, None)
    Parcheggio = Room("Parcheggio", None, None, None, None)
    AulaGialla = Room("Aula gialla", None, None, None, None)
    Presidenza = Room("Presidenza", None, None, None, None)
    AulaAzzurra = Room("Aula azzurra", None, None, None, None)  # serve a inizializzare parcheggio

    Atrio.set_links(Parcheggio, Segreteria, AreaRelax, None)
    Segreteria.set_links(Atrio, AreaRelax, AulaGialla, Presidenza)
    AulaAzzurra.set_links(AreaRelax, Parcheggio, None, None)
    AreaRelax.set_links(Segreteria, Atrio, AulaAzzurra, None)
    AulaGialla.set_links(Segreteria, None, None, None)
    Presidenza.set_links(Segreteria, None, None, None)
    Parcheggio.set_links(Atrio, AulaAzzurra, None, None)
    
    places = [Parcheggio, Atrio, Segreteria, AulaAzzurra, AreaRelax, AulaGialla, Presidenza]

    man = random.choice(places[1:])
    print(man.get_room_name())
    man.set_manual()

    p = Player("ciro")
    p.is_in = Parcheggio
    p.move()
    p.show()
    while p.get_pv() >= 1:
        q2 = input("m = move\ns = show\nq = quit\n")
        if q2 == "m":
            p.move()
        elif q2 == "s":
            p.show()
        elif q2 == "q":
            quit()
    print("Oh no ho perso tutti i miei punti vita, VEDO LA LUCE!!!\n rip.")
    quit()

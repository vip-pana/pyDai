import random

from player import Player
from rooms.room import Room

'''    Atrio = Room("Atrio", None, None, None, None, "qui si va per la formazione dolente,\nda questa zona posso andare un po' dappertutto")
Segreteria = Room("Segreteria", None, None, None, None, "in questo luogo ci sono un sacco di scartoffie,\nnon mi ci voglio neanche avvicinare...")
AreaRelax = Room("Area relax", None, None, None, None, "ahh in questa zona posso ")'''

if __name__ == "__main__":
    print("""                                                                                                    
                        ...     ..                                  _                                                      s                
        .=*8888x <"?88h.                              u                                                      :8                
        X>  '8888H> '8888                 u.    u.    88Nu.   u.                u.    u.      x.    .        .88           u.   
        '88h. `8888   8888        .u     x@88k u@88c. '88888.o888c      .u     x@88k u@88c.  .@88k  z88u     :888ooo  ...ue888b  
        '8888 '8888    "88>    ud8888.  ^"8888""8888"  ^8888  8888   ud8888.  ^"8888""8888" ~"8888 ^8888   -*8888888  888R Y888r 
        `888 '8888.xH888x.  :888'8888.   8888  888R    8888  8888 :888'8888.   8888  888R    8888  888R     8888     888R I888> 
        X" :88*~  `*8888> d888 '88%"   8888  888R    8888  8888 d888 '88%"   8888  888R    8888  888R     8888     888R I888> 
        ~"   !"`      "888> 8888.+"      8888  888R    8888  8888 8888.+"      8888  888R    8888  888R     8888     888R I888> 
        .H8888h.      ?88  8888L        8888  888R   .8888b.888P 8888L        8888  888R    8888 ,888B .  .8888Lu= u8888cJ888  
        :"^"88888h.    '!   '8888c. .+  "*88*" 8888"   ^Y8888*""  '8888c. .+  "*88*" 8888"  "8888Y 8888"   ^%888*    "*888*P"   
        ^    "88888hx.+"     "88888%      ""   'Y"       `Y"       "88888%      ""   'Y"     `Y"   'YP       'Y"       'Y"      
                ^"**""          "YP'                                  "YP'                                                       
                                .                                 ..                                      s                      
                            @88>                             dF                                       :8                      
            ...     ..        %8P                  u.    u.   '88bu.                     u.    u.      .88                      
        :~""888h.:^"888:      .          u      x@88k u@88c. '*88888bu         u      x@88k u@88c.   :888ooo      .u           
        8X   `8888X  8888>   .@88u     us888u.  ^"8888""8888"   ^"*8888N     us888u.  ^"8888""8888" -*8888888   ud8888.         
        X888n. 8888X  ?888>  ''888E` .@88 "8888"   8888  888R   beWE "888L .@88 "8888"   8888  888R    8888    :888'8888.        
        '88888 8888X   ?**h.   888E  9888  9888    8888  888R   888E  888E 9888  9888    8888  888R    8888    d888 '88%"        
        `*88 8888~ x88x.     888E  9888  9888    8888  888R   888E  888E 9888  9888    8888  888R    8888    8888.+"           
        ..<"  88*`  88888X    888E  9888  9888    8888  888R   888E  888F 9888  9888    8888  888R   .8888Lu= 8888L             
            ..XC.    `*8888k   888&  9888  9888   "*88*" 8888" .888N..888  9888  9888   "*88*" 8888"  ^%888*   '8888c. .+        
        :888888H.    `%88>   R888" "888*""888"    ""   'Y"    `"888*""   "888*""888"    ""   'Y"      'Y"     "88888%          
        <  `"888888:    X"     ""    ^Y"   ^Y'                    ""       ^Y"   ^Y'                             "YP'           
             888888x.-`                                                                                                       
                ""**""                                                                                                          
                                                                                                                                
                                                                                                                                                                                            
                                                                                                    """)



    Atrio = Room("Atrio", None, None, None, None, "qui si va per la formazione dolente,\nda questa zona posso andare un po' dappertutto")
    Segreteria = Room("Segreteria", None, None, None, None, "in questo luogo ci sono un sacco di scartoffie,\nnon mi ci voglio neanche avvicinare...")
    AreaRelax = Room("Area relax", None, None, None, None, "ahh in questa zona posso prendermi un caffe pensando a tutti gli sbagli che ho fatto nella mia vita...\nBENE vediamo dove è questo manuale!")
    Parcheggio = Room("Parcheggio", None, None, None, None, "Qui è dove mastro Pana parcheggia il supremo monopattino ogni mattina,\nSia lode a lui!!")
    AulaGialla = Room("Aula gialla", None, None, None, None, "in questo posto sogni e frustrazioni si legano in passione.\nfino a che Bruno non ti fa uscire scemo con teoria nuova!\nvediamo se trovo il manuale...")
    Presidenza = Room("Presidenza", None, None, None, None, "Non conosco il padron del luogo, se non trovo il manuale namose da qui")
    AulaAzzurra = Room("Aula azzurra", None, None, None, None, "questi sono i gollum del luogo, i serpe verde della zona, quelli a cui chiedi l'accendino quando lo hai perso\ne puntualmente loro hanno uno molto simile al tuo... (-_-)")  # serve a inizializzare parcheggio

    Atrio.set_links(Parcheggio, Segreteria, AreaRelax, None)
    Segreteria.set_links(Atrio, AreaRelax, AulaGialla, Presidenza)
    AulaAzzurra.set_links(AreaRelax, Parcheggio, None, None)
    AreaRelax.set_links(Segreteria, Atrio, AulaAzzurra, None)
    AulaGialla.set_links(Segreteria, None, None, None)
    Presidenza.set_links(Segreteria, None, None, None)
    Parcheggio.set_links(Atrio, AulaAzzurra, None, None)
    
    places = [Parcheggio, Atrio, Segreteria, AulaAzzurra, AreaRelax, AulaGialla, Presidenza]

    man = random.choice(places[1:])
    man.set_manual()
    m = 0
    p = Player("ciro")
    p.is_in = Parcheggio
    p.move()
    p.show()
    while p.get_pv() >= 1:
        q2 = input("m = move\ns = show\nq = quit\n")
        if q2 == "m":
            p.move()
            m +=1
        elif q2 == "s":
            p.show()
        elif q2 == "q":
            quit()
    print("Oh no ho perso tutti i miei punti vita, VEDO LA LUCE!!!\n rip.")
    print(f"Statistiche:\nmovimenti totali = {m}")
    quit()

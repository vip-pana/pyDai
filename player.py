class Player:
    pv = 10
    is_in = object
    
    def __init__(self, nome):
        self.nome = nome
        print(f"Benvenuto {self.nome}!\n")

    def get_is_in(self):
        return self.is_in
        
    def move(self):
        b = self.is_in.get_links()
        q = (input("dove devo andare: "))
        try:
            for i in b.values():
                a = i
                b = a.get_room_name()
                if q == b:
                    self.is_in = a
                    self.pv -= 1
                    print(f"ora sei in {a.get_room_name()}\n******** Hai ben {self.pv} punti vita")
                    break
        except:
            return print("Ahime' non posso andare per la via indicata...")

    def get_pv(self):
        return self.pv

    def show(self):
        place = self.get_is_in()
        place.show()
    
    def quit(self):
        pass

class Room:
    __manual = False
    __links = {}
    
    def __init__(self, room_name, nord = None, sud=None, est=None, ovest=None):
        self.__room_name = room_name
        self.__links = {"nord": nord, "sud": sud, "est": est, "ovest": ovest}

    def get_links(self):
        return self.__links

    def get_room_name(self):
        return self.__room_name

    def get_key_name(self):
        for i in self.__links.values():
            if i == None:
                pass
            else:
                a = i
                print("- ", a.get_room_name(), "\n")

    def set_manual(self):
        self.__manual = True

    def set_links(self, nord, sud, est, ovest):
        self.__links = {
            "nord":nord,
            "sud":sud,
            "est":est,
            "ovest":ovest
        }

    def show(self):
        if self.__manual is False:
            print(f"Sono in {self.__room_name} e il manuale qui non c'e'!\nda qui posso andare in zona:")
            self.get_key_name()
        else:

            print("Complimenti hai trovato il manuale!\ncanteranno delle tue gesta negli anni a venire")
            quit()




class HotelRoom:
    ''' _____________________________________________________
        + room_number :   int
        + room_type   :   str
        + is_occupied :   bool
        - guest_name  :   str
        _____________________________________________________
        + __init__(room_number: int, room_type: str) -> None
        + set_guest_name(guest_name: str) -> None
        + get_guest_name() -> str
        + occupy(guest_name: str) -> None
        + vacate() -> None
        + get_room_info() -> str
        _____________________________________________________
    '''
    def __init__(self, room_number: int, room_type: str) -> None:
        self.room_number = room_number
        self.room_type = room_type
        self.is_occupied = False
    
    def set_guest_name(self, guest_name: str) -> None:
        self.__guest_name = guest_name
    
    def get_guest_name(self) -> str:
        return self.__guest_name
    
    def occupy(self, guest_name: str) -> None:
        if self.is_occupied == False:
            self.is_occupied = True
            self.set_guest_name(guest_name)
    
    def vacate(self) -> None:
        if self.is_occupied == True:
            self.is_occupied = False
            self.set_guest_name('')

    def get_room_info(self) -> str:
        if self.is_occupied == True:
            return f'Stanza {self.room_number}: {self.room_type}, occupata da {self.get_guest_name()}'
        else:
            return f'Stanza {self.room_number}: {self.room_type}, libera'


stanza = HotelRoom(104, 'doppia')
print(stanza.get_room_info())
stanza = HotelRoom(234, 'singola')
stanza.occupy('Luisa Ferro')
print(stanza.get_room_info())
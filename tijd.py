from time import sleep

#ADT Time
class Time:
    """
    Initialiseer Tijd 

    preconditie: /
    postconditie: Tijd object wordt aangemaakt

    :param date: tuple dat dag, maand, jaar bevat | Type -> Tuple
    :param time: tuple dat uur, minuut, second bevat | Type -> Tuple
    """
    def __init__(self, date, time) -> None:
        self.day, self.month, self.year = date
        self.h, self.m, self.s = time
    
    """
    Stringify Time
    """
    def __str__(self) -> str:
        return "Time: {}:{}:{}".format(self.h, self.m, self.s) + " Date: {}:{}:{}".format(self.day, self.month, self.year)
    
    """
    Stel de tijd in

    preconditie: /
    postconditie: tijd wordt aangepast

    :param new: nieuwe Tijd | Type -> Time

    :return: None
    """
    def setTime(self, new):
        self.day, self.month, self.year = new.day, new.month, new.year
        self.h, self.m, self.s = new.h, new.m, new.s

    """
    Is huidig jaar een schrikkeljaar

    preconditie: /
    postconditie: /

    :return: Geeft True terug als desbetreffend jaar een schrikkeljaar is
    """
    def isSchrikkeljaar(self):
        return (self.year%4==0 and not self.year%100==0) or self.year%400==0
    
    """
    Geeft True terug als er teveel dagen zijn voor desbetreffende maand
    """
    def dayError(self):
        return (self.month in [1,3,5,7,8,10,12] and self.day > 31) or (self.month in [4,6,9,11] and self.day > 30) or (self.month == 2 and ((self.isSchrikkeljaar() and self.day > 29) or (not self.isSchrikkeljaar() and self.day > 28)))

    """
    Behandelt violations van maanden na optelling
    """
    def handleMonths(self):
        while self.month > 12:
            self.year += 1
            self.month -= 12

    """
    Behandelt violations van dagen na optelling
    """
    def handleDays(self):
        while self.dayError():
            if self.month in [1,3,5,7,8,10,12]:
                self.day -= 31
            elif self.month in [4,6,9,11]:
                self.day -= 30
            elif self.month == 2:
                if self.isSchrikkeljaar():
                    self.day -= 29
                elif not self.isSchrikkeljaar():
                    self.day -= 28
            self.month += 1
        self.handleMonths()
        
    """
    Behandelt violations van uren na optelling
    """
    def handleHours(self):
        while self.h >= 24:
            self.h -= 24
            self.day += 1
            self.handleDays()
    
    """
    Behandelt violations van minuten na optelling
    """
    def handleMinutes(self):
        while self.m >= 60:
            self.m -= 60
            self.h += 1
            self.handleHours()

    """
    Behandelt violations van seconden na optelling
    """
    def handleSeconds(self):
        while self.s >= 60:
            self.s -= 60 
            self.m += 1
            self.handleMinutes()

    """
    Telt 's' aantal seconden bij de huidige tijd op
    """
    def addSeconds(self, s):
        self.s += s
        self.handleSeconds()

#ADT Clock
class Clock(Time):
    """
    Initialiseer Clock object

    preconditie: /
    postconditie: Clock object wordt aangemaakt

    :param date: tuple dat dag, maand, jaar bevat | Type -> Tuple
    :param time: tuple dat uur, minuut, second bevat | Type -> Tuple
    """
    def __init__(self, date, time) -> None:
        super().__init__(date, time)
    
    """
    Tick de clock

    preconditie: /
    postconditie: De clock slaagt

    :param tps: Aantal ticks per seconden | Type -> int
            Als TPS None is tickt de clock zonder een delay
    """
    def tick(self, tps):
        #tps is ticks per second
        self.addSeconds(1)
        if tps is not None:
            sleep(1/tps)

    """
    Stringify de clock
    """
    def __str__(self) -> str:
        return super().__str__()
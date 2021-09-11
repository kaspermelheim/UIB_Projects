#!/usr/bin/env python3

"""
Grafisk framstilling av labyrint
Author: nmidd
"""

from tkinter import Tk, Canvas

BREIDDE = 1200 # Pikslar
HØGDE = 600 # Pikslar
FARGAR = {
        'S' : 'black',    # Stengt
        'G' : 'yellow',   # Ope
        'R' : 'red'       # Utgang
        }

def vis(labyrint, utvegsliste):
    tk = Tk()
    brett = Brett(labyrint, utvegsliste)
    brett.initiering()
    brett.pack()
    tk.mainloop()

def main():
    """
    Test av grafisk framstilling av ein liten labyrint
    """
    tk = Tk()
    labyrint = [[True, True, False, True], [False, True, True, False]]
    utvegsliste = [(0,0), (0,1), (1,1)]
    brett = Brett(labyrint, utvegsliste)
    brett.initiering()
    brett.pack()
    tk.mainloop()

class Brett(Canvas):

    def __init__(self, labyrint, utvegsliste):
        super().__init__(width=BREIDDE, height=HØGDE,
            background="grey", highlightthickness=0)
        self._labyrint = labyrint
        self._utvegsliste = utvegsliste
        self._steg = 0
        self._steglengd = (BREIDDE//len(labyrint[0]), HØGDE//len(labyrint))

    def initiering(self):
        """Gjer klar for teikning av labyrinten"""
        self.teikn()
        self.bind_all("<Key>", self.tast)

    def teikn(self):
        """Teiknar labyrinten"""
        (m, n) = (len(self._labyrint), len(self._labyrint[0]))
        for i in range(m):
            for j in range(n):
                rute = 'S'
                if self._labyrint[i][j]:
                    rute = 'G'
                (y1, x1) = (i*self._steglengd[1], j*self._steglengd[0])
                (y2, x2) = (y1 + self._steglengd[1], x1 + self._steglengd[0])
                self.create_rectangle(x1, y1, x2, y2, fill=FARGAR[rute])

    def flytt(self):
        """Flytt framover i labyrinten"""
        (xlengd, ylengd) = (self._steglengd[0], self._steglengd[1])
        if self._steg < len(self._utvegsliste):
            (i,j) = self._utvegsliste[self._steg]
            (y1, x1) = (i*ylengd, j*xlengd)
            (y2, x2) = (y1 + ylengd, x1 + xlengd)
            self.create_rectangle(x1, y1, x2, y2, fill=FARGAR['R'])
            self._steg += 1
        
    def tast(self, trykk):
        """Tar mot signal om tastetrykk"""
        self.flytt()

if __name__ == '__main__':
    main()

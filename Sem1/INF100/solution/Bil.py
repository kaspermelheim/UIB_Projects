class Bil():
    def __init__(self, name, x, y, bensin):
        self._name = name
        self._x = x
        self._y = y
        self._bensin = bensin

    def __brukBensin(self, distanse):
        # Vi kan ikke bruke mer bensin enn vi har på tanken
        bensinFør = self._bensin
        self._bensin = max(self._bensin - distanse, 0)
        if self._bensin <= 0:
            print('%s er tom for bensin!' % (self._name))
        return bensinFør - self._bensin

    def __hentPosisjon(self):
        return (self._x, self._y)

    def kjørØst(self, distanse):
        self._x += self.__brukBensin(distanse)

    def kjørVest(self, distanse):
        self._x -= self.__brukBensin(distanse)

    def kjørNord(self, distanse):
        self._y -= self.__brukBensin(distanse)

    def kjørSør(self, distanse):
        self._y += self.__brukBensin(distanse)

    def fyllBensin(self, enheter):
        self._bensin += enheter

    def printStatus(self):
        print('%s befinner seg på posisjon %s med %d enheter bensin igjen.' %
              (self._name, self.__hentPosisjon(), self._bensin))

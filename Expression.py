import Piece
import operator

class Express:

    def __init__(self, elements):
        self.elements = elements
        self.ordered = self.sortElements()

    def __str__(self):

        running = "parts of expression:"

        for element in self.elements:
            running = running + "\n" + element.toString()

        return running


    def returnSorted(self):

        running = "parts of expression:"

        for order in self.ordered:
            running = running + "\n" + ordered.toString()

        return running


    def sortElements(self):

        return sorted(self.elements, key=operator.attrgetter("power"))

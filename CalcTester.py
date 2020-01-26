import Piece
import Expression

def main():



    til = Piece.Part(False, "11", "t", ".5")

    tilt = Piece.Part(True, "10", "t", "2")


    #print(til)

    #print(til.equals(25))

    #print(tilt)

    #print(tilt.equals(5))

    stuff = [til, tilt]

    tilting = Expression.Express(stuff)

    print(tilting)

    print(tilting.ordered)

    print(tilting.sortElements())

if __name__ == '__main__':
    main()

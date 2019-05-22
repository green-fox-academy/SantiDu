for id in range(1,5):
    with open(f"./database/{id}.txt", "w") as f:
        if id == 1:
            f.write("1991\nJonathan Demme\nJodie Foster, Anthony Hopkins, Lawrence A. Bonney")
        elif id == 2:
            f.write("2014\nDamien Chazelle\n Miles Teller, J.K. Simmons, Melissa Benoist")
        elif id == 3:
            f.write("1997\nGus Van Sant\nRobin Williams, Matt Damon, Ben Affleck")
        else:
            f.write("2009\nJuan José Campanella\n Ricardo Darín, Soledad Villamil, Pablo Rago")
            
def distanze(punto_destinazione):
    '''Restituisce la distanza euclidea e di manhattan
    calcolata dal punto (0, 0)'''
    x, y = punto_destinazione[0], punto_destinazione[1]
    dist_e = (x**2 + y**2)**0.5
    dist_m = x+y
    return(dist_e, dist_m)

p = (4, 11)
d = distanze(p)
print(d)


def distance_time(distance):
    v = 299792458               # m/s
    distance = distance*1000    # km -> m
    t = distance/v              # s
    return(t)

# Utilizzo la funzione
d = distance_time(424)
print(d)
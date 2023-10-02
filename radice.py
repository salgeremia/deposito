num = 81 

print('\nmetodo iterativo definito')
eccesso = num
for _ in range(10):    
    difetto = num/eccesso
    eccesso = (eccesso+difetto)/2
    print(eccesso)

print('\nmetodo iterativo indefinito')
eccesso = num
soglia = 0.001
diff = soglia+1
while diff > soglia:
    difetto = num/eccesso
    diff = eccesso - (eccesso+difetto)/2
    eccesso = (eccesso+difetto)/2
    print(eccesso)
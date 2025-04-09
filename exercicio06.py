dentro = 0
fora = 0
for x in range(10):
    n =int(input("digite um numero"))
    if n>= 10 and n <= 20:
        dentro = dentro+1
else:
    fora = fora+1
print (dentro, fora)

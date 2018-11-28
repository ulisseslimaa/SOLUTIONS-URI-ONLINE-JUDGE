n= int(input())
contador=2
penultimo=0
ultimo=1
fn=0
l = [0,1]
while contador != n:
    contador+=1
    fn=ultimo+penultimo
    l.append(fn)
    penultimo=ultimo
    ultimo=fn
print(" ".join(map(str, l)))
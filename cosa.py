costo_to=int(input())
costo_people= costo_to/13
casa1=5*costo_people
pagar1=round(casa1,2)
casa2=1*costo_people
pagar2 = round(casa2,2)
casa3= 3*costo_people
pagar3=round(casa3,2)
casa4=4*costo_people
pagar4=round(casa4,2)
cosa=[[101, 5, pagar1], [201, 1, pagar2], [301, 3, pagar3], [401, 4, pagar4]]
print(cosa[0])
print(cosa[1])
print(cosa[2])
print(cosa[3])

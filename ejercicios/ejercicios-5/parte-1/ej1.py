print("ingrese distancia");
dis = float(input());

print("Ingrese velocidad");
vel = float(input());

def calcs (dis,vel):
    res = dis/vel;
    return print("demora " + str(res));

calcs(dis,vel);

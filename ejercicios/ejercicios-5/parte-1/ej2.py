print("ingrese base");
base = float(input());

print("Ingrese altura");
altura = float(input());

def calcs (base,altura):
    res = base*altura;
    return print("area " + str(res/2));

calcs(base,altura);

money = 200
value = 150

if (money < value):
    print('El dinero que tiene no es suficiente para esta compra.')
else:
    change = money - value
    if (change == 0):
        print('No hay devuelta el dinero fue igual a la compra')
    else:
        print('Su devuelta es de: ' + str(change))

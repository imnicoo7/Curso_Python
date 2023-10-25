ingreso_mensual = 2500
gasto_mesual = 1800

if ingreso_mensual > 1000:
    if ingreso_mensual - gasto_mesual < 0:
        print('estas en perdida')
    elif ingreso_mensual - gasto_mesual > 300:
        print('estas bien pa')
    else: 
        print('empieza a gastar menos pa')
        
elif ingreso_mensual > 500:
    print('estas bien en latinoamerica')
    
elif ingreso_mensual > 100:
    print('empieza a buscar otro trabajo che')

else:
    print('sos probre')
class MiExcepcion(Exception):
    def __int__(self, err):
        print(f'Impresionante, cometiste el siguiente error: {err}')


try:
    raise MiExcepcion("Como cometes esa excepcion taradito JAJA")

except:
    print('Como vas a cometer ese error che?')


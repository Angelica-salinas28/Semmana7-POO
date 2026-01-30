class ImpresoraTickets:

    def __init__(self, ruta_archivo: str):
        self.ruta_archivo = ruta_archivo
        self.archivo = open(self.ruta_archivo, "a", encoding="utf-8")
        print("Archivo abierto en__init__")

    def imprimir(self, mensaje: str):
        self.archivo.write(mensaje + "/n")
        self.archivo.flush()

    def cerrar(self):
        if self.archivo and not self.archivo.closed:
            self.archivo.close()
            print("Archivo cerrado con cerrar()")

    def __del__(self):
        try:
            if self.archivo and not self.archivo.closed:
                self.archivo.close()
                print("Archivo cerrado en __del__ (respaldo)")
        except Exception:
            pass

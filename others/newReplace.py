class replaceNew():
    def __init__(self, texto):
        self.texto = texto
        self.salida = ""
        self.i = 0
    def reemplazarDerecha(self, oldstr, newstr):
        while self.i < len(self.texto):
            if self.texto[self.i:self.i+len(oldstr)] == oldstr:
                self.salida = self.salida.rstrip() + newstr
                self.i += len(oldstr)
            else:
                self.salida = self.salida + self.texto[self.i]
                self.i += 1
        return self.salida
    def reemplazarIzquierda(self, oldstr, newsrt):
        while self.i < len(self.texto):
            if self.texto[self.i:self.i+len(oldstr)] == oldstr:
                self.salida += newsrt
                self.i += len(oldstr)
                self.i += 1
            else:
                self.salida += self.texto[self.i]
                self.i += 1
        return self.salida
if __name__ == "__main__":
    class Carta:
        CORAZON = 'Corazón'
        DIAMANTE = 'Diamante'
        PICAS = 'Picas'
        TREBOLES = 'Treboles'

        def __init__(self, valor, pinta):
            self.valor = valor
            self.pinta = pinta

        def __str__(self):
            return f"{self.valor} de {self.pinta}"
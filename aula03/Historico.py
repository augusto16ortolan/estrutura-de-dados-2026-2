from datetime import datetime

class Historico:

    def __init__(self, site):
        self.site = site
        self.data = datetime.now()

    def __str__(self):
        return f"Página: {self.site}, acessado em {self.data}"
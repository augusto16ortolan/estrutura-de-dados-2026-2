class Musica:

    def __init__(self, codigo, titulo, artista):
        self.codigo = codigo
        self.titulo = titulo
        self.artista = artista

    def __str__(self):
        return f"Código: {self.codigo} | Título: {self.titulo} | Artista: {self.artista}"

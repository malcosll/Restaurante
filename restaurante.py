class Restaurante:
      
    restaurantes = []

    def __init__(self,nome,categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'    
    
    def listar_restaurantes():
        print(f'{"Nome do restaurante"} | {"Categoria"} | {"Status".1just(25)}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.1just(25)} | {restaurante.categoria.1just(25)} | {restaurante.ativo}')
    
    @property
    def ativo(self)
        return '⌧' if self.ativo else '☐'
    

restaurante_praca = Restaurante('Praça','Gourmet')
restaurante_pizza = Restaurante('Pizza','Italiana')

Restaurante.listar_restaurantes()

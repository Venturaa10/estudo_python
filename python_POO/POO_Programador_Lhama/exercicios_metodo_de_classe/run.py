class Loja:
    taxa = 1.15
    
    def __init__(self, valor: float) -> None:
        self.valor_produto_bruto = valor
        
    def consultar_valor_do_produto(self):
        valor_produto = self.valor_produto_bruto * self.taxa
        print(f'Valor do produto: {valor_produto:.2f}')

    @classmethod
    def editar_taxa_do_produto(cls, valor:float):
        ''' Altera o valor da taxa para todos os objetos da classe'''
        print(f'\nTaxa alterada de {cls.taxa:.2f} para {valor:.2f}')
        cls.taxa = valor
    

loja_prata = Loja(30.50)
loja_gold = Loja(40.21)
loja_diamante = Loja(50.42)

loja_prata.consultar_valor_do_produto()
loja_gold.consultar_valor_do_produto()
loja_diamante.consultar_valor_do_produto()

Loja.editar_taxa_do_produto(2.3) # Altera o valor da taxa

loja_prata.consultar_valor_do_produto()
loja_gold.consultar_valor_do_produto()
loja_diamante.consultar_valor_do_produto()
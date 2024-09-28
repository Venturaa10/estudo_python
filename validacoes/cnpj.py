
'''
class Cnpj:
    def __init__(self, documento):
        documento = str(documento)
        if self.cnpj_eh_Valido(documento):
            self.cnpj = documento
        else:
            raise ValueError("cnpj inválido!")

    def cnpj_eh_Valido(self, cnpj):
        if len(cnpj) == 14:
            validador = CNPJ()
            return validador.validate(cnpj)
        else:
            raise ValueError("Quantidade de dígitos inválida")

    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        return self.format_cnpj()
'''
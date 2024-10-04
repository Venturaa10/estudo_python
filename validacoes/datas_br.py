from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        ''' Verifica o mes que o usuario foi cadastrado '''
        meses_do_ano = [
            'janeiro', 'fevereiro', 'março',
            'abril', 'maio', 'junho', 'julho'
            'agosto', 'setembro', 'outubro', 
            'novembro', 'dezembro'
        ]

        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]
    
    def dia_semana(self):
        ''' Verifica o dia da semana que o usuario foi cadastrado '''

        dias_da_semana = [
            'Segunda-Feira', 'Terça-Feira', 'Quarta-Feira',
            'Quinta-Feira', 'Sexta-Feira', 'Sabado', 'Domingo'
        ]
        dia_semana = self.momento_cadastro.weekday() 
        return dias_da_semana[dia_semana]
    
    def format_data(self):
        ''' Data formatada no padrão BR'''
        data_formatada = self.momento_cadastro.strftime('%d/%m/%Y %H:%M') 
        return data_formatada
    
    def __str__(self):
        return self.format_data()

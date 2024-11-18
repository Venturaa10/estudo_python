import re

teste_email = ('''João estava organizando um evento para seus colegas de trabalho na empresa. O evento seria realizado no próximo mês e ele precisava confirmar a presença de todos os convidados o mais rápido possível. Para isso, ele enviou um e-mail informando todos os detalhes do evento, como a data, o horário e o local. Ele também solicitou que os convidados respondessem com qualquer dúvida ou sugestão para melhorar o evento. Caso alguém precisasse de mais informações, João disponibilizou o seu e-mail de contato para suporte: joao.eventos123@email.com. Além disso, pediu que confirmassem a presença até a próxima semana.

Durante a organização, João se deparou com algumas dificuldades para reservar o local e contratar o serviço de buffet. Contudo, ele se manteve otimista, pois já havia planejado tudo com antecedência e estava seguro de que conseguiria resolver qualquer contratempo que surgisse.''')


padrao = r'[a-zA-Z0-9._%+-]{2,50}@[a-zA-Z0-9.-]{2,15}\.[a-zA-Z]{2,6}(\.[a-zA-Z]{2,6})?'
busca = re.search(padrao, teste_email)
''' 
span -> Indica a posição onde a correspondência foi encontrada dentro da string original
match -> A parte que correspondeu ao padrão da expressão regular
'''
print(busca) # <re.Match object; span=(516, 541), match='joao.eventos123@email.com'>

''' 
.group() -> Retorna apenas a string que correspondeu ao padrão da expressão regular, sem informações adicionais
'''
print(busca.group()) # joao.eventos123@email.com
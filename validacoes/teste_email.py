import re

email_um = 'rodrigo@gmail.com'
email_dois = 'rodrigao1993@4shared.org.uk'
email_tres = 'rodrigo@rodrigo.br'
email_quatro = 'rodrigo123@python.py.br'

# Utilizar o "r" para trabalhar com expressões regulares é uma boa pratica
padrao = r'[a-zA-Z0-9._%+-]{2,50}@[a-zA-Z0-9.-]{2,15}\.[a-zA-Z]{2,6}(\.[a-zA-Z]{2,6})?'

# Testando
for email in [email_um, email_dois, email_tres, email_quatro]:
    match = re.search(padrao, email)
    if match:
        print(f"{email} | Resposta: {match.group(0)}")

import re 

padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}" # Padrão de telefone
texto = "aaabbbcc 2126451234 r fu92h78gfh278fh8 21264563414 2126451234"
resposta = re.search(padrao, texto) # Retorna so a primeira correspondencia do padrão

# 'resposta.group()' retorna a correspondência completa do padrão.
print(resposta.group())

# findall -> Retorna todas as correspondencia do padrão
resposta2 = re.findall(padrao, texto)
print(resposta2)

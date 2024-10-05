from datetime import datetime, timedelta

hoje = datetime.today()
amanha = datetime.today() + timedelta(days=1, hours=13)

print(amanha - hoje)
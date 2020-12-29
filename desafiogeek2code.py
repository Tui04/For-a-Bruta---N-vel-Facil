import random
from zipfile import ZipFile


def descobrir_senha():
        return random.randint(0, 10_000)


zip_file = 'facil.zip'
with ZipFile(zip_file) as zf:
    while True:
        password = descobrir_senha()
        try:
            zf.setpassword(str(password).encode('UTF-8'))
            zf.extract('parabens.txt')
            print(f'a senha era {password}')
            break
        except:
            pass
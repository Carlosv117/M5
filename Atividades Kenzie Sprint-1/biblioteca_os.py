import os

variavel = "Carlos"

minha_variavel = os.getenv(f'variavel')
print(minha_variavel)
# 'valor da variavel'


minha_variavel = os.getenv('NOME_DE_VARIAVEL_QUE_NAO_EXISTE')
print(minha_variavel)
# None

# Passando valor default
minha_variavel = os.getenv('NOME_DE_VARIAVEL_QUE_NAO_EXISTE', 'valor default')
print(minha_variavel)
# 'valor default'

# os.system("rm -rf example.txt")
# os.system("mkdir diretorio")


resultado = os.popen("ls -la")
print(resultado)
# <os._wrap_close object at 0x7f5007f34940>

print(*resultado)

# total xy
# drwxrwxr-x  6 usuario usuario 4096 mai 17 13:31 .
# drwxr-xr-x  4 usuario usuario 4096 abr 12 11:50 ..
# drwxrwxr-x 10 usuario usuario 4096 mai 17 09:58 dir_name
# drwxrwxr-x  2 usuario usuario 4096 mai 17 13:31 dir_name
# -rw-rw-r--  1 usuario usuario  477 mai 17 15:06 dir_name
# drwxrwxr-x  6 usuario usuario 4096 fev 19 21:45 dir_name
# drwxrwxr-x  7 usuario usuario 4096 mai 17 14:02 dir_name


print(os.listdir())
# ['dir_name', 'dir_name-06', 'filename.txt', 'dir_name', 'dir_name']

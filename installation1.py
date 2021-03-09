import os
import sys

print('Programma di installazione di prova')

#file che saranno installati
Installed_files = ['real program.py', 'Libprova']


#Controllo che non ci siano già
if set(Installed_files) <= set(os.listdir(path='.')):
    print('Programma già installato correttamente.')
    sys.exit(1)

#Vedo quali mancano
Missing_files=set(Installed_files) - (set(Installed_files) & set(os.listdir(path='.')))


#se mancano tutti ok, altrimenti va disinstallato e reinstallato
if set(Missing_files) != set(Installed_files):
    print('Missing file: %s' % Missing_files)
    sys.exit(1)
    


os.mkdir('./Libprova')


#apro il file e cambio directory
buff2 = open('hello_lib', 'r')
os.chdir('./Libprova')

buff=None


for line in  buff2:

    #riconosce la linea corrispondente alle vare funzioni
    if line.startswith('$$$Vfun1'):
        if buff is not None:
            buff.close()
        if line.replace('$','') not in os.listdir(path='.'):
            buff = open(line.rstrip('\n').replace('$','')+'.py', 'x')
        else:
            #non è davvero necessario, lo tengo per sicurezza
            print('errore: file già esistente')
        continue
    
    #Creo anche init prima di uscire 
    if line.startswith('$$$real'):
        if '__init__.py' not in os.listdir(path='.'):
            temp = open('__init__.py', 'w+')
            temp.write('')
            temp.close()
        os.chdir('..')
        if buff is not None:
            buff.close()
        if line.replace('$','') not in os.listdir(path='.'):
            buff = open(line.rstrip('\n').replace('$','')+'.py', 'x')
        else:
            print('errore: file già esistente')
        continue

    #creo il file per disinstallare
    if line.startswith('$$$uninstall'):
        if buff is not None:
            buff.close()
        if line.replace('$','') not in os.listdir(path='.'):
            buff = open(line.rstrip('\n').replace('$','')+'.py', 'x')
        else:
            print('errore: file già esistente')
        continue

    buff.write(line)

#chiudo tutto
buff.close()
buff2.close()

if set(Installed_files) <= set(os.listdir(path='.')):
    print('Installazione completata')
    sys.exit(0)
else:
    print('Qualcosa è andato storto')
    sys.exit(1)




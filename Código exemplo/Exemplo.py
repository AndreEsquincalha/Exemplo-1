#Questão 2 - Trabalho 2ºBI Sisteamas Operacionais
#Integrantes:
#Alain Patrick Fernandes Garcia
#André Luiz Esquincalha Vieira Garcia

#Foi feito a importação da biblioteca mMap como mostrado
import mmap

arquivo = open("C:/temp/arquivo.dat", "r+b")
dado_mmap = mmap.mmap(arquivo.fileno(), 0)

while True:
    info_tela = input("\nInforme o que deseja:\nLer ----------- (l)\nGravar -------- (g)\nSair ---------- (s)\n")
    
    if info_tela == 'l':
        
        print(dado_mmap.readline())
    
    elif info_tela == 'g':
        
        Dado_usuario = input("Ola, Informe o que deseja gravar: ")
        dado_mmap[0:len(Dado_usuario)] = Dado_usuario.encode()
        dado_mmap.seek(0)
    
    elif info_tela == 's':
        break;
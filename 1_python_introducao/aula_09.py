import shutil


def escrever_arquivo(texto):
    # arquivo = open('teste.txt', 'w')
    diretorio = 'C:/Temp/dio/workspace/data-engineer-bootcamp-dio/1_python_introducao/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)


def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        print(lista_notas)
        aluno = lista_notas[0]
        print(aluno)
        lista_notas.pop(0)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno: media(lista_notas)})
    return lista_media


def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Temp/dio/workspace/data-engineer-bootcamp-dio/notas_alunos.txt')


def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Temp/dio/workspace/data-engineer-bootcamp-dio/')


if __name__ == '__main__':
    # escrever_arquivo('Primeira linha.')
    # aluno = 'Cesar, 7, 5, 9, 6\n'
    # atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('teste.txt')
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
    # copia_arquivo('notas.txt')
    move_arquivo('notas.txt')

# arquivo= open('teste.txt', 'w')
# arquivo.write('Primeira linha')

# arquivo= open('teste.txt', 'a')
# arquivo.write('\nTerceira linha')
# arquivo.close()

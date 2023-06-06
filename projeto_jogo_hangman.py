"""
Docstring
Maybe, it may be neccessary to download yourself the module 'unidecode', seen that it can cause several problems.
"""
import random
from unidecode import unidecode
from IPython.display import clear_output

def hangman_game(respostas: list, forcas: list, chances: int, cont: int, letras:list, resp:dict) -> None:
    """
    hangman_game function
    This function will develop the game. Every loop starts with the input asking for a new letter,
    after it goes through a refinement process, the logic through the code starts.
    """
    print("-----Seja bem vindo ao jogo da forca!-----\n")
    while chances > 0:
        clear_output(wait=True)
        cont += 1
        resposta = unidecode((input(f"\nPor gentileza, digite o {cont}º chute: ").lower()))
        respostas.append(resposta)
        if resposta in letras:
            for i in resp.keys():
                if unidecode(i[0]) == resposta:
                    resp[i] = i[0]
        else:
            print("infelizmente, você errou :/")
            chances -= 1
        if chances != 0:
            print(forcas[chances])
            for i in resp.values():
                print(i + " ", end=" ")
            print("\n", respostas)
            if "_" not in resp.values():
                print("\n\nParabéns, você venceu o jogo :)")
                break
        else:
            print(forcas[chances])


def main()->None:
    """
    Main function
    """
    palavras = ['escada','criança','fralda','leão','pássaro','natação','banho','musculação']
    random.shuffle(palavras)
    respostas = []
    forcas = [
    f'''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =======
    Você perdeu o jogo, sinto muito
    A palavra era {palavras[0]}
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =======
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =======
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =======
    ''',
    '''
      +---+
      |   |
      O   |
     /    |
          |
          |
    =======
    ''',

    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =======
    ''',
        '''
      +---+
      |   |
          |
          |
          |
          |
    =======
    ''',
    ]
    chances = 6
    cont = 0
    letras = [unidecode(i) for i in palavras[0]]
    resp = {(f'{k}{n}'): "_" for n, k in enumerate(list(palavras[0]))}
    hangman_game(respostas, forcas, chances, cont, letras, resp)

if __name__=="__main__":
    main()

def main()->None:
  import random
  from IPython.display import clear_output
  from unidecode import unidecode
  palavras = ['escada','criança','fralda','leão','pássaro','natação','banho','musculação']
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
  random.shuffle(palavras)
  letras = [unidecode(i) for i in palavras[0]]
  resp = {(f'{k}{n}'): "_" for n, k in enumerate([i for i in palavras[0]])}
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

if __name__=="__main__":
    main()

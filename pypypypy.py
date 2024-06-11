jogo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def mostrar_jogo(jogo):		
    for l in range(0,3):
        for c in range(0,3):
            print(f'[{jogo[l][c]:^5}]', end='')
        print()

mostrar_jogo(jogo)
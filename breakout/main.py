from breakout.game import Game

# Simulação do jogo
if __name__ == "__main__":
    game = Game()

    print("Simulação do Breakout")
    print("Comandos: 'esq', 'dir', 'play', 'sair'")
    print("Mova a raquete com 'esq' ou 'dir'. Jogue com 'play'.")

    while game.running:
        command = input("Digite o comando: ").strip().lower()

        if command == "esq":
            game.move_paddle("esq")
        elif command == "dir":
            game.move_paddle("dir")
        elif command == "play":
            game.play_turn()
        elif command == "sair":
            print("Saindo do jogo.")
            break
        else:
            print("Comando inválido")

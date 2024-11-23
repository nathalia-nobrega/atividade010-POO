from pong.game import Game

def main():
    game = Game()

    print("Bem-vindo ao Pong!")
    print("Controles:")
    print("Jogador 1: escreva 'acima' para acima, 'abaixo' para abaixo")
    print("Jogador 2: 'acima' para acima, 'abaico' para abaixo")
    print("Pressione 'q' para sair.")

    while game.running:
        # show state
        game.print_game_state()

        # ball movement
        game.play_turn()

        #
        action_player1 = input("Jogador 1 (acima/abaixo): ")
        if action_player1 == "acima":
            game.move_paddle(1, "acima")
        elif action_player1 == "abaixo":
            game.move_paddle(1, "abaixo")

        action_player2 = input("Jogador 2 (acima/abaixo): ")
        if action_player2 == "acima":
            game.move_paddle(2, "acima")
        elif action_player2 == "abaixo":
            game.move_paddle(2, "abaixo")

        # finish game
        if input("Continuar jogando? (s/n): ").lower() != "s":
            game.running = False

if __name__ == "__main__":
    main()
from card import Card
from player import Player
from gamedealer import GameDealer
def play_game():
    # 두 명의 player 객체 생성 + dealer 객체 생성
    player1 = Player("흥부")
    player2 = Player("놀부")
    dealer = GameDealer()

    GameDealer.make_deck(dealer)
    GameDealer.shuffle_deck(dealer)
    GameDealer.givecard(dealer, 10, player1, player2)

    player1.display_two_card_lists()
    player2.display_two_card_lists()

    n = 2
    while True:
        if len(dealer.deck) == 0 or len(player1.holding_card_list) == 0 or len(player2.holding_card_list) == 0:
            break
        enter = input(f'[{n}]단계: 다음 단계 진행을 위해 Enter 키를 누르세요!')
        if enter != '': break
        if n == 2:
            player1.check_one_pair_card()
            player1.display_two_card_lists()
            player2.check_one_pair_card()
            player2.display_two_card_lists()
        else:
            GameDealer.givecard(dealer,4, player1, player2)
            player1.check_one_pair_card()
            player1.display_two_card_lists()
            player2.check_one_pair_card()
            player2.display_two_card_lists()
        n += 1


if __name__ == '__main__':
    play_game()
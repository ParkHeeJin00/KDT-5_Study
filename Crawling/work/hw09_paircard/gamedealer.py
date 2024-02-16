from card import Card
import random
class GameDealer:
    def __init__(self):
        self.deck = []
        self.suit_number = 13

    def print_deck(self,deck):
        for n, i in enumerate(deck):
            print(i, end ='\n' if (n + 1) % 13 == 0 else ' ')

    def make_deck(self):

        card_suits = ["♠", "♥", "♣", "◆"]
        card_numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        for i in card_suits:
            for j in card_numbers:
                self.deck.append(Card(i,j))


    def shuffle_deck(self):
        random.shuffle(self.deck)

    def givecard(self,n,player1,player2):
        for i in range(n):
            player1.holding_card_list.append(self.deck.pop())
            player2.holding_card_list.append(self.deck.pop())
        print('='*70,f'\n카드 나누어 주기: {n}장')
        print('-'*70)
        print(f'[GameDealer] 딜러가 가진 카드 수 : {len(self.deck)}')
        self.print_deck(self.deck)
        print()

if __name__ == '__main__':
    dealer = GameDealer()
    dealer.make_deck()
    print('[GameDealer] 초기 카드 생성')
    print('-' * 70)
    print(f'[GameDealer] 딜러가 가진 카드 수: {len(dealer.deck)}')
    dealer.print_deck(dealer.deck)
    dealer.shuffle_deck()
    print('\n[GameDealer] 카드 랜덤하게 섞기')
    print('-' * 70)
    print(f'[GameDealer] 딜러가 가진 카드 수: {len(dealer.deck)}')
    dealer.print_deck(dealer.deck)

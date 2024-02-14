from gamedealer import GameDealer
from card import Card
class Player:
    def __init__(self, name):
        self.name = name
        self.holding_card_list = list()
        self.open_card_list = list()

    def add_card_list(self):
        pass

    def display_two_card_lists(self):
        print('='*70)
        print(f'[{self.name}] Open card list: {len(self.open_card_list)}')
        if len(self.open_card_list) > 0:
            for card in self.open_card_list:
                print(card, end = ' ')
        print('\n')

        print(f'[{self.name}] Holding card list: {len(self.holding_card_list)}')
        if len(self.holding_card_list) > 0:
            for card in self.holding_card_list:
                print(card, end=' ')
        print('\n')

    def check_one_pair_card(self):
        print("="*70)
        print(f"[{self.name}: 숫자가 같은 한쌍의 카드 검사]")
        for card1 in self.holding_card_list:
            for card2 in self.holding_card_list:
                if card1 != card2 and card1.number == card2.number and card1 not in self.open_card_list and card2 not in self.open_card_list:
                    self.open_card_list.append(self.holding_card_list.pop(self.holding_card_list.index(card1)))
                    self.open_card_list.append(self.holding_card_list.pop(self.holding_card_list.index(card2)))







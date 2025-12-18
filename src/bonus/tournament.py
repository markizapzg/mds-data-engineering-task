import random
from collections import defaultdict


class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0

    def __repr__(self):
        return self.name


class Table:
    def __init__(self, players):
        self.players = players

    def play(self):
        winner = random.choice(self.players)
        winner.wins += 1
        return winner


class Tournament:
    def __init__(self, players, tables, group_size):
        self.players = players
        self.tables = tables
        self.group_size = group_size

        # ko je sa kim već igrao
        self.played_with = defaultdict(set)

    def run_round(self):
        random.shuffle(self.players)

        tables = []
        for i in range(0, self.tables * self.group_size, self.group_size):
            group = self.players[i:i + self.group_size]
            if len(group) == self.group_size:
                tables.append(Table(group))

        winners = []
        for table in tables:
            winner = table.play()
            winners.append(winner)

            for p in table.players:
                for other in table.players:
                    if p != other:
                        self.played_with[p.name].add(other.name)

        return winners

    def run_tournament(self, rounds=5):
        for r in range(rounds):
            self.run_round()

        return max(self.players, key=lambda p: p.wins)

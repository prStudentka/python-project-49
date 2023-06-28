#!/usr/bin/env python3
from brain_games.game import start_game
from brain_games.games import brain_calc


def main():
    start_game(brain_calc)


if __name__ == "__main__":
    main()

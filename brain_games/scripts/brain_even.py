#!/usr/bin/env python3
from brain_games.game import start_game
from brain_games.games import brain_even


def main():
    start_game(brain_even)


if __name__ == "__main__":
    main()

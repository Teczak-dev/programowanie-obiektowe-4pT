import random

def roll_dice(num_dice):
    """Rzuca określoną liczbę kości."""
    return [random.randint(1, 6) for _ in range(num_dice)]

def calculate_score(dice):
    """
    Oblicza punkty za rzut.
    1 = 100 pkt, 5 = 50 pkt
    Trójki: 1 = 1000 pkt, inne liczby = liczba * 100
    """
    score = 0
    counts = {i: dice.count(i) for i in range(1, 7)}

    # Punkty za jedynki i piątki
    score += counts[1] * 100
    score += counts[5] * 50

    # Punkty za trójki
    for num, count in counts.items():
        if count >= 3:
            if num == 1:
                score += 1000
            else:
                score += num * 100
            counts[num] -= 3  # Usuń trójkę z liczenia jedynek/piątek

    return score

def play_turn():
    """Rozgrywa turę jednego gracza."""
    total_score = 0
    remaining_dice = 6

    while True:
        print(f"\nRzucasz {remaining_dice} kośćmi...")
        dice = roll_dice(remaining_dice)
        print(f"Wynik rzutu: {dice}")

        turn_score = calculate_score(dice)
        if turn_score == 0:
            print("Brak punktowanych wyników! Tracisz punkty z tej rundy.")
            return 0

        print(f"Punkty za ten rzut: {turn_score}")
        total_score += turn_score

        # Decyzja gracza
        choice = input(f"Masz {total_score} punktów. Czy chcesz rzucać dalej? (tak/nie): ").lower()
        if choice != 'tak':
            break

        remaining_dice = int(input("Ile kości chcesz ponownie rzucić? (1-6): "))
        if remaining_dice < 1 or remaining_dice > 6:
            print("Błędna liczba kości, przerywamy turę.")
            break

    return total_score

def main():
    """Główna pętla gry."""
    num_players = int(input("Podaj liczbę graczy: "))
    target_score = 5000  # Cel do wygranej
    scores = [0] * num_players

    print("\nRozpoczynamy grę w kości!")
    while all(score < target_score for score in scores):
        for i in range(num_players):
            print(f"\nTura gracza {i + 1} (wynik: {scores[i]} pkt)")
            scores[i] += play_turn()
            print(f"Gracz {i + 1} ma teraz {scores[i]} punktów.")

            if scores[i] >= target_score:
                print(f"\nGracz {i + 1} osiągnął cel {target_score} punktów i wygrał!")
                return

    print("Gra zakończona.")

if __name__ == "__main__":
    main()

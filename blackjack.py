from art import logo
import random
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


start_game = input("Quieres jugar BlackJack? Selecciona 'y' o 'n': ")

while start_game == "y":
    my_cards = []
    computer_cards = []
    total_my_cards = 0
    total_computer_cards = 0

    print(logo)

    my_cards.extend(random.sample(cards, 2))
    computer_cards.extend(random.sample(cards, 1))

    print(f"Tus cartas son: {my_cards}")
    print(f"Las cartas de la computadora son: [{computer_cards[0]}, ?]")

    continue_game = input("¿Quieres agregar otra carta? Presiona 'y' para sí, 'n' para no: ")

    while continue_game == "y":
        random_choice = random.choice(cards)
        if random_choice == 11 and total_my_cards + 11 > 21:
            random_choice = 1

        my_cards.append(random_choice)

        total_my_cards = sum(my_cards)

        print(f"Tus cartas son: {my_cards}")

        if total_my_cards > 21:
            print(f"Superaste 21 con un total de {total_my_cards}. ¡Perdiste!")
            start_game = "end"
            break

        continue_game = input("¿Quieres agregar otra carta? Presiona 'y' para sí, 'n' para no: ")

    if start_game == "end":
        break


    while sum(computer_cards) < 13:
        computer_cards.append(random_choice)

    total_computer_cards = sum(computer_cards)

    print(f"Las cartas de la computadora son: {computer_cards}")
    print(f"Tu total de cartas es: {total_my_cards}")
    print(f"El total de cartas de la computadora es: {total_computer_cards}")

    if total_computer_cards > 21:
        print("La computadora se pasó de 21. ¡Ganaste!")
    elif total_computer_cards > total_my_cards:
        print("La computadora gana. ¡Perdiste!")
    elif total_computer_cards < total_my_cards:
        print("Ganaste!")
    else:
        print("Empate.")

    start_game = input("¿Quieres jugar otra vez? Selecciona 'y' o 'n': ")

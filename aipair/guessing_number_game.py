import random


def play_game():
	number = random.randint(1, 25)

	print("Guess the number between 1 and 25!")
	for attempt in range(1, 4):
		guess = int(input(f"Attempt {attempt}/3: "))

		if guess == number:
			print("You guessed it!")
			return

		if guess < number:
			print("Hint: try a higher number.")
		else:
			print("Hint: try a lower number.")

	print(f"Sorry, the number was {number}.")


if __name__ == "__main__":
	play_game()

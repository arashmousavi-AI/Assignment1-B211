import os
import random
import string
import time


class PasswordGenerator:

    def __init__(self, words_file="top_english_nouns_lower_100000.txt"):
        self.words_file = words_file
        self.words = self._load_words(words_file)

        # Ensuring the output directories actually exist
        self.mem_dir = "Memorable"
        self.rand_dir = "Random"
        os.makedirs(self.mem_dir, exist_ok=True)
        os.makedirs(self.rand_dir, exist_ok=True)

        self.mem_log = os.path.join(self.mem_dir, "Generated_Passwords.txt")
        self.rand_log = os.path.join(self.rand_dir, "Generated_Passwords.txt")

    def _load_words(self, words_file):
        #Load words from the specified file into a list.
        base_dir = os.path.dirname(os.path.abspath(__file__))
        words_path = os.path.join(base_dir, words_file)

        # necessary checking that whether the file ex
        if not os.path.exists(words_path):
            print(f"ERROR: '{words_file}' not fund in the program directory.")
            return []

        with open(words_path, "r", encoding="utf-8") as f:
            words = [line.strip() for line in f if line.strip()]

        if not words:
            print("words file is empty.")
            return []

        return words


    def _timestamp(self):
        # Return timestamp in the day/date/time format.
        # like Tue Jan 27 08:34:59 PM| 2026
        return time.strftime("%a %b %d %I:%M:%S %p %Y")

    def _append_log(self, password_type, password_value):
        #Append password + timestamp to the correct log file.
        line = f"{self._timestamp()} | {password_value}\n"
        if password_type == "memorable":
            with open(self.mem_log, "a", encoding="utf-8") as f:
                f.write(line)
        else:
            with open(self.rand_log, "a", encoding="utf-8") as f:
                f.write(line)

    def generate_memorable(self, num_words=4, case="lower"):
        #create a memorable password using several random wordds.
        if num_words < 1 or not self.words:
            return "ERROR: the invalid number of words or word list is unavailable."

        if case not in {"lower", "upper", "title"}:
            case = "lower"

        parts = []
        for w in random.choices(self.words, k=num_words):
            digit = str(random.randint(0, 9))
            w = w.upper() if case == "upper" else w.title() if case == "title" else w.lower()
            parts.append(w + digit)

        password = "-".join(parts)
        self._append_log("memorable", password)
        return password


    def generate_random(self, length=12, include_punct=True, banned_chars=""):
        #create a random password based on the user-specified options like lenghth.
        if length < 1:
            return "ERROR: Invalid password length."

        allowed = string.ascii_lowercase + string.ascii_uppercase + string.digits
        if include_punct:
            allowed += string.punctuation

        allowed = "".join(c for c in allowed if c not in banned_chars)

        if not allowed:
            return "ERROR: No valid characters available."

        password = "".join(random.choice(allowed) for _ in range(length))
        self._append_log("random", password)
        return password


    def prompt_and_generate(self):
        #Prompts the user to choose password type and the other required options.
        print("\npassword Generator")
        print("1) memorable password")
        print("2) Random password")

        choice = input("Choose (1/2): ").strip()

        if choice == "1":
            try:
                num_words = int(input("How many words? : ").strip())
                case = input("Case (lower/upper/title): ").strip().lower()
                password = self.generate_memorable(num_words=num_words, case=case)
                print("Generated memorable password:", password)
            except ValueError:
                print("Invalid input. Please enter valid values.")

        elif choice == "2":
            try:
                length = int(input("Password length?: ").strip())
                include_punct = input("Include punctuation? (y/n): ").strip().lower() == "y"
                banned = input("Any banned characters (leave blank if none): ")
                password = self.generate_random(
                    length=length,
                    include_punct=include_punct,
                    banned_chars=banned
                )
                print("Generated random password:", password)
            except ValueError:
                print("Invalid input. Please enter valid values.")

        else:
            print("Invalid choice. Please select 1 or 2.")



    def generate_1000_random_mix(self):
        #Confirm logging works by generating a thousands passwords,with password type chosen randomly each time.
        
        for _ in range(1000):
            if random.choice(["memorable", "random"]) == "memorable":
                # Reasonable defaults; you can tweak these
                self.generate_memorable(num_words=4, case="lower")
            else:
                self.generate_random(length=12, include_punct=True, banned_chars="")


def main():
    # the main entry of the program. here the user interact with the program.
    
    random.seed(80)  # I set the random seed to a fixed value for reproducibility.

    gen = PasswordGenerator()

    while True:
        print("\nMenu:")
        print("1) Generate a password")
        print("2) Generate 1000 passwords (random mix)")
        print("3) Quit")
        choice = input("Choose (1/2/3): ").strip()

        if choice == "1":
            gen.prompt_and_generate()
        elif choice == "2":
            gen.generate_1000_random_mix()
            print("Done! Check Memorable/Generated_Passwords.txt and Random/Generated_Passwords.txt")
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()

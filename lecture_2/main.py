def generate_profile(age):
    try:
        if age < 0:
            return "Unknown"
        elif 0 <= age <= 12:
            return "Child"
        elif 13 <= age <= 19:
            return "Teenager"
        else:
            return "Adult"
    except:
        return "Unknown"


def main():
    print("Mini-Profile Generator")
    print("==============================================")

    while True:
        user_name = input("Enter your full name: ").strip()
        if user_name:
            break
        else:
            print("Namefield is empty. Please try again.")

    while True:
        birth_year_str = input("Enter your birth year: ").strip()
        try:
            birth_year = int(birth_year_str)
            if birth_year <= 0 or birth_year > 2025:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid YEAR (e.g., 2005).")

    try:
        current_age = 2025 - birth_year
    except:
        current_age = 0

    hobbies = []

    while True:
        hobby = input("Enter a favorite hobby or type 'stop' to finish: ").strip()

        if hobby.lower() == "stop":
            break
        elif hobby == "":
            print("Hobby cannot be empty. Please try again.")
        else:
            hobbies.append(hobby)

    life_stage = generate_profile(current_age)

    user_profile = {
        "name": user_name,
        "age": current_age,
        "stage": life_stage,
        "hobbies": hobbies
    }

    print("\n---")
    print("Profile Summary:")
    print(f"Name: {user_profile['name']}")
    print(f"Age: {user_profile['age']}")
    print(f"Life Stage: {user_profile['stage']}")

    if len(hobbies) == 0:
        print("You didn't mention any hobbies.")
    else:
        print(f"Favorite Hobbies ({len(hobbies)}):")
        for h in hobbies:
            print(f"- {h}")

    print("---")

if __name__ == "__main__":
    main()

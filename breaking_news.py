import random
import datetime

subjects = [
    "Ali Zafar", "Naseem Shah", "Maira Khan", "A Pindi Cat",
    "Prime Minister", "Auto Rickshaw Driver from Karachi",
    "A Group of Monkeys", "Biryani Wala Uncle", "A Confused Politician",
    "Karachi Traffic Police", "A Lost Tourist in Lahore"
]
actions = [
    "launches", "cancels", "dances with", "eats",
    "declares war on", "orders 50 plates of", "celebrates",
    "argues about", "accidentally sits on", "runs away from",
    "takes a selfie with", "files a complaint against"
]
places = [
    "at Red Fort", "in Karachi Local Train", "a plate of samosa",
    "inside Parliament", "at Rohri", "during PSL match",
    "at Sea View", "in a rickshaw stuck in Lahore traffic",
    "at Naan shop at 2am", "during load shedding",
    "at Biryani festival", "inside a flooded street"
]

CATEGORIES = {
    "1": {
        "name": "Pakistani Drama",
        "subjects": ["Sad Heroine", "Rich Villain", "Poor Hero", "Naani Amma", "Suspicious Bhabhi"],
        "actions": ["cries dramatically at", "slaps someone at", "returns after 20 years to", "forgives everyone at", "plots against"],
        "places": ["a haveli", "rainy rooftop", "hospital corridor", "wedding stage", "drawing room"]
    },
    "2": {
        "name": "Cricket Special",
        "subjects": ["Naseem Shah", "Babar Azam", "A Pigeon on the pitch", "Pakistani Umpire", "Whole Team"],
        "actions": ["drops a catch at", "hits a six into", "argues with referee at", "celebrates too early at", "sledges opponent at"],
        "places": ["Lords Cricket Ground", "Gaddafi Stadium", "someone rooftop", "tape-ball pitch in Karachi", "National Stadium"]
    },
    "3": {
        "name": "Random Mix",
        "subjects": subjects,
        "actions": actions,
        "places": places
    }
}

session_headlines = []

def print_banner():
    print("\n" + "=" * 52)
    print("     PAKISTAN BREAKING NEWS GENERATOR")
    print("=" * 52)

def choose_category():
    print("\nSelect category:")
    print("  1. Pakistani Drama")
    print("  2. Cricket Special")
    print("  3. Random Mix")
    print("  4. Custom (you enter person & place)")
    choice = input("\nEnter 1 / 2 / 3 / 4: ").strip()
    return choice if choice in ("1","2","3","4") else "3"

def get_custom_inputs():
    print("\n--- Custom Mode ---")
    person = input("Enter person/character name: ").strip() or "Mystery Person"
    place  = input("Enter a place or thing: ").strip()  or "somewhere in Pakistan"
    return person, place

def generate_headline(cat_choice):
    if cat_choice in ("1","2","3"):
        cat     = CATEGORIES[cat_choice]
        subject = random.choice(cat["subjects"])
        action  = random.choice(cat["actions"])
        place   = random.choice(cat["places"])
    else:
        subject, place = get_custom_inputs()
        action = random.choice(actions)
    ts = datetime.datetime.now().strftime("%I:%M %p")
    return f"BREAKING NEWS [{ts}]: {subject} {action} {place}!"

def save_to_file():
    if not session_headlines:
        print("\nKoi headline nahi hai abhi.")
        return
    fname = f"headlines_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(fname, "w", encoding="utf-8") as f:
        f.write("PAKISTAN BREAKING NEWS - Session Report\n")
        f.write(f"Date: {datetime.datetime.now().strftime('%B %d, %Y %I:%M %p')}\n")
        f.write("=" * 52 + "\n\n")
        for i, h in enumerate(session_headlines, 1):
            f.write(f"{i}. {h}\n")
    print(f"\n✓ {len(session_headlines)} headlines saved to: {fname}")

def main():
    print_banner()
    cat_choice = choose_category()
    count = 0
    while True:
        headline = generate_headline(cat_choice)
        session_headlines.append(headline)
        count += 1
        print("\n" + "-" * 52)
        print(headline)
        print("-" * 52)
        print(f"Session count: {count}")
        if count == 4:
            print(f"\n[4 headlines completed!]")
            if input("Do you want to save them? (yes/no): ").strip().lower() == "yes":
                save_to_file()
        print("\n  yes  - next headline")
        print("  cat  - change category")
        print("  save - save now")
        print("  no   - exit")
        choice = input("\nChoice: ").strip().lower()
        if choice == "no":
            if session_headlines:
                if input(f"\nWould you like to save {len(session_headlines)} headlines before exiting? (yes/no): ").strip().lower() == "yes":
                    save_to_file()
            print("\nThanks! Good Bye :)\n")
            break
        elif choice == "cat":
            cat_choice = choose_category()
        elif choice == "save":
            save_to_file()

if __name__ == "__main__":
    main()   
import time
import json
import os

# Init makes
surron = "Sur-Ron"
talaria = "Talaria"
rt = "Riding Times"
tuttio = "Tuttio"
rs = "Ridstar"
tst = "TST GRP LLC"
sf = "Stark Future"

# Your make missing? Join the discord on the github page to request makes.

# Init models

# SUR-RON
ubx = "Ultra Bee X"
lbx26 = "Light Bee X 2026"
lbx25 = "Light Bee X 2025"
lbs = "Light Bee S"
hbx = "Hyper Bee X 2026"

# Talaria
mx5p = "Sting MX5 Pro"
rmx4 = "Sting R MX4"
mx3 = "Sting MX3"
x3mx = "X3 (XXX) MX"

# Riding Times
gt54p = "GT54 PRO"
gt54 = "GT54"
gt73p = "GT73 PRO"
gt73 = "GT73"
gt33 = "GT33"
z8p = "Z8 PRO"

# Tuttio
s01 = "Soliel01"
s01lo = "Soliel01 LO"
s01bf = "Soliel01 BF"
s01gb = "Soleil01 GB"
s01sf = "Soleil01 SF"
a26 = "Adria26"
arci = "ARC-I"
ict = "ICT"

# Ridstar
q20l = "Q20 Lite"
q20 = "Q20"
q20p = "Q20 Pro"
q30 = "Q30"
q30l = "Q30 Lite"
q30p = "Q30 Pro"
q30ll = "Q30 Lux Lite"

# TST GRP LLC
r002 = "R002"
r7 = "R7"
r9 = "R9"

# Stark Future
sv = "Stark Varg"

# Your model missing? Join the discord in the github bio to request a model!


# ---- JSON DATABASE ----

DB_FILE = "bikes.json"

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return {}

def save_db(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=4)

def add_bike(owner, make_name, model_name):
    db = load_db()
    db[owner] = {
        "make": make_name,
        "model": model_name,
        "mod_logs": [],
        "maintenance_logs": [],
        "notes": []
    }
    save_db(db)
    print(f"\nBike registered for {owner}: {make_name} {model_name}")

def edit_bike(owner):
    db = load_db()
    if owner not in db:
        print("Username not found in database.")
        return
    print(f"\nCurrent bike: {db[owner]['make']} {db[owner]['model']}")
    new_make = input("Enter new make (or press Enter to keep current):\n> ").strip()
    new_model = input("Enter new model (or press Enter to keep current):\n> ").strip()
    if new_make:
        db[owner]["make"] = new_make
    if new_model:
        db[owner]["model"] = new_model
    save_db(db)
    print(f"Bike updated for {owner}!")

def remove_bike(owner):
    db = load_db()
    if owner in db:
        del db[owner]
        save_db(db)
        print(f"Bike removed for {owner}.")
    else:
        print("Username not found in database.")

def view_bike(owner):
    db = load_db()
    if owner not in db:
        print("Username not found in database.")
        return
    b = db[owner]
    print(f"\n{'='*40}")
    print(f"  {owner}'s Bike: {b['make']} {b['model']}")
    print(f"{'='*40}")

    print("\n-- Modification Logs --")
    if b["mod_logs"]:
        for i, entry in enumerate(b["mod_logs"], 1):
            print(f"  {i}. [{entry['date']}] {entry['mod']}")
    else:
        print("  No modifications logged.")

    print("\n-- Maintenance Logs --")
    if b["maintenance_logs"]:
        for i, entry in enumerate(b["maintenance_logs"], 1):
            print(f"  {i}. [{entry['date']}] {entry['work']} (Next due: {entry['next_due']})")
    else:
        print("  No maintenance logged.")

    print("\n-- Notes --")
    if b["notes"]:
        for i, entry in enumerate(b["notes"], 1):
            print(f"  {i}. [{entry['date']}] {entry['note']}")
    else:
        print("  No notes added.")
    print(f"{'='*40}\n")


# ---- LOGS & NOTES ----

def add_mod_log(owner):
    db = load_db()
    if owner not in db:
        print("Username not found in database.")
        return
    print(f"\nLogging modification for {owner}'s {db[owner]['make']} {db[owner]['model']}")
    date = input("Date of modification (e.g. 2026-06-10):\n> ").strip()
    mod = input("What was modified?\n> ").strip()
    db[owner]["mod_logs"].append({"date": date, "mod": mod})
    save_db(db)
    print("Modification logged!")

def remove_mod_log(owner):
    db = load_db()
    if owner not in db:
        print("Username not found in database.")
        return
    logs = db[owner]["mod_logs"]
    if not logs:
        print("No modification logs to remove.")
        return
    print("\n-- Modification Logs --")
    for i, entry in enumerate(logs, 1):
        print(f"  {i}. [{entry['date']}] {entry['mod']}")
    choice = input("\nEnter the number to remove:\n> ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(logs):
        removed = logs.pop(int(choice) - 1)
        save_db(db)
        print(f"Removed: [{removed['date']}] {removed['mod']}")
    else:
        print("Invalid selection.")

def add_maintenance_log(owner):
    db = load_db()
    if owner not in db:
        print("Username not found in database.")
        return
    print(f"\nLogging maintenance for {owner}'s {db[owner]['make']} {db[owner]['model']}")
    date = input("Date of maintenance (e.g. 2026-06-10):\n> ").strip()
    work = input("What work was done?\n> ").strip()
    next_due = input("Next due date (or press Enter to skip):\n> ").strip() or "N/A"
    db[owner]["maintenance_logs"].append({"date": date, "work": work, "next_due": next_due})
    save_db(db)
    print("Maintenance logged!")

def remove_maintenance_log(owner):
    db = load_db()
    if owner not in db:
        print("Username not found in database.")
        return
    logs = db[owner]["maintenance_logs"]
    if not logs:
        print("No maintenance logs to remove.")
        return
    print("\n-- Maintenance Logs --")
    for i, entry in enumerate(logs, 1):
        print(f"  {i}. [{entry['date']}] {entry['work']} (Next due: {entry['next_due']})")
    choice = input("\nEnter the number to remove:\n> ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(logs):
        removed = logs.pop(int(choice) - 1)
        save_db(db)
        print(f"Removed: [{removed['date']}] {removed['work']}")
    else:
        print("Invalid selection.")

def add_note(owner):
    db = load_db()
    if owner not in db:
        print("Username not found in database.")
        return
    print(f"\nAdding note for {owner}'s {db[owner]['make']} {db[owner]['model']}")
    date = input("Date (e.g. 2026-06-10):\n> ").strip()
    note = input("Note:\n> ").strip()
    db[owner]["notes"].append({"date": date, "note": note})
    save_db(db)
    print("Note added!")

def remove_note(owner):
    db = load_db()
    if owner not in db:
        print("Username not found in database.")
        return
    notes = db[owner]["notes"]
    if not notes:
        print("No notes to remove.")
        return
    print("\n-- Notes --")
    for i, entry in enumerate(notes, 1):
        print(f"  {i}. [{entry['date']}] {entry['note']}")
    choice = input("\nEnter the number to remove:\n> ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(notes):
        removed = notes.pop(int(choice) - 1)
        save_db(db)
        print(f"Removed: [{removed['date']}] {removed['note']}")
    else:
        print("Invalid selection.")

def manage_bike(owner):
    db = load_db()
    if owner not in db:
        print("Username not found in database.")
        return
    while True:
        print(f"\n-- Managing {owner}'s {db[owner]['make']} {db[owner]['model']} --")
        print("1. Add modification log")
        print("2. Remove modification log")
        print("3. Add maintenance log")
        print("4. Remove maintenance log")
        print("5. Add note")
        print("6. Remove note")
        print("7. View full bike profile")
        print("8. Back")
        choice = input("\nChoice:\n> ").strip()

        if choice == "1":
            add_mod_log(owner)
        elif choice == "2":
            remove_mod_log(owner)
        elif choice == "3":
            add_maintenance_log(owner)
        elif choice == "4":
            remove_maintenance_log(owner)
        elif choice == "5":
            add_note(owner)
        elif choice == "6":
            remove_note(owner)
        elif choice == "7":
            view_bike(owner)
        elif choice == "8":
            break
        else:
            print("Invalid choice.")

        db = load_db()


# ---- MAIN APPLICATION ----

print("Copyright Wintercat Development Digital, 2026. All Rights Reserved.")
time.sleep(2)

while True:
    print("\nWhat would you like to do?")
    print("1. Register my bike")
    print("2. Manage my bike (logs & notes)")
    print("3. Edit my bike")
    print("4. Remove my bike")
    print("5. View my bike")
    print("6. Exit")
    choice = input("\nChoice:\n> ").strip()

    if choice == "1":
        print("\nPlease find your make in this list, then type in its variable.")
        print("Sur-Ron (surron)")
        print("Talaria (talaria)")
        print("Riding Times (rt)")
        print("Tuttio (tuttio)")
        print("Ridstar (rs)")
        print("TST GRP LLC (tst)")
        print("Stark Future (sf)")

        make = input("\n\nWho made your bike?\n> ").strip()

        if make == "surron":
            print("\nPlease look through the list, find your vehicle, and enter its variable.")
            print("Ultra Bee X (ubx)")
            print("Light Bee X 2026 (lbx26)")
            print("Light Bee X 2025 (lbx25)")
            print("Light Bee S (lbs)")
            print("Hyper Bee X 2026 (hbx)")
            model = input("\n\nWhat model is your Sur-Ron?\n> ").strip()
            model_map = {"ubx": ubx, "lbx26": lbx26, "lbx25": lbx25, "lbs": lbs, "hbx": hbx}
            make_name, model_name = surron, model_map.get(model)

        elif make == "talaria":
            print("\nSting MX5 Pro (mx5p)")
            print("Sting R MX4 (rmx4)")
            print("Sting MX3 (mx3)")
            print("X3 (XXX) MX (x3mx)")
            model = input("\n\nWhat model is your Talaria?\n> ").strip()
            model_map = {"mx5p": mx5p, "rmx4": rmx4, "mx3": mx3, "x3mx": x3mx}
            make_name, model_name = talaria, model_map.get(model)

        elif make == "rt":
            print("\nGT54 PRO (gt54p)")
            print("GT54 (gt54)")
            print("GT73 PRO (gt73p)")
            print("GT73 (gt73)")
            print("GT33 (gt33)")
            print("Z8 PRO (z8p)")
            model = input("\n\nWhat model is your Riding Times?\n> ").strip()
            model_map = {"gt54p": gt54p, "gt54": gt54, "gt73p": gt73p, "gt73": gt73, "gt33": gt33, "z8p": z8p}
            make_name, model_name = rt, model_map.get(model)

        elif make == "tuttio":
            print("\nSoliel01 (s01)")
            print("Soliel01 LO (s01lo)")
            print("Soliel01 BF (s01bf)")
            print("Soleil01 GB (s01gb)")
            print("Soleil01 SF (s01sf)")
            print("Adria26 (a26)")
            print("ARC-I (arci)")
            print("ICT (ict)")
            model = input("\n\nWhat model is your Tuttio?\n> ").strip()
            model_map = {"s01": s01, "s01lo": s01lo, "s01bf": s01bf, "s01gb": s01gb, "s01sf": s01sf, "a26": a26, "arci": arci, "ict": ict}
            make_name, model_name = tuttio, model_map.get(model)

        elif make == "rs":
            print("\nQ20 Lite (q20l)")
            print("Q20 (q20)")
            print("Q20 Pro (q20p)")
            print("Q30 (q30)")
            print("Q30 Lite (q30l)")
            print("Q30 Pro (q30p)")
            print("Q30 Lux Lite (q30ll)")
            model = input("\n\nWhat model is your Ridstar?\n> ").strip()
            model_map = {"q20l": q20l, "q20": q20, "q20p": q20p, "q30": q30, "q30l": q30l, "q30p": q30p, "q30ll": q30ll}
            make_name, model_name = rs, model_map.get(model)

        elif make == "tst":
            print("\nR002 (r002)")
            print("R7 (r7)")
            print("R9 (r9)")
            model = input("\n\nWhat model is your TST GRP LLC?\n> ").strip()
            model_map = {"r002": r002, "r7": r7, "r9": r9}
            make_name, model_name = tst, model_map.get(model)

        elif make == "sf":
            print("\nStark Varg (sv)")
            model = input("\n\nWhat model is your Stark Future?\n> ").strip()
            model_map = {"sv": sv}
            make_name, model_name = sf, model_map.get(model)

        else:
            print("Make not recognized. Please try again.")
            continue

        if model_name is None:
            print("Model not recognized. Please try again.")
            continue

        owner = input("\nEnter a username to save your bike under:\n> ").strip()
        add_bike(owner, make_name, model_name)

    elif choice == "2":
        owner = input("\nEnter your username:\n> ").strip()
        manage_bike(owner)

    elif choice == "3":
        owner = input("\nEnter your username:\n> ").strip()
        edit_bike(owner)

    elif choice == "4":
        owner = input("\nEnter your username:\n> ").strip()
        remove_bike(owner)

    elif choice == "5":
        owner = input("\nEnter your username:\n> ").strip()
        view_bike(owner)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1-6.")
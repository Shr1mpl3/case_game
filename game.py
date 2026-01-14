import random
from players import OhnePixel, Dxno
from case import cases

cases_defeated = 0
total_inventory_value = 0

#STORY INTRO
print("Du spawnst auf der Map Anubis")
print("\nGabeN hat Cases lebendig gemacht.")
print("\nAber deine sucht hungert.")
print("Um sie zu öffnen, musst du sie BESIEGEN.\n")

# CASE(S)
anubis_case = cases(
    4.31,
    ["AUG | Snake Pit", "MP7 | Sunbaked"],
    [0.16, 0.12],
    ["M4A1-S | Mud-Spec"],
    [0.81],
    ["AWP | Black Nile"],
    [5.06],
    ["Glock-18 | Ramese's Reach"],
    [30.36],
    ["FAMAS | Waters of Nephthys"],
    [184.8],
    ["M4A4 | Eye of Horus"],
    [1185],
    [],
    []
)

# PLAYER SELECT
print("Wähle deinen Spieler:")
print("A) OhnePixel: mehr Startkapital")
print("B) dxno: mehr Glück, bessere Drops (Cooler und besser)")

choice = input("Eingabe (A/B): ").lower()

if choice == "a":
    player = OhnePixel(
        "männlich",
        endurance=20,
        dmg=8,
        hp=40,
        luck=10,
        money=1200,
        key=1
    )
elif choice == "b":
    player = Dxno(
        "männlich",
        endurance=18,
        dmg=10,
        hp=38,
        luck=25,
        money=500,
        key=1
    )
else:
    print("Ungültige Eingabe. OhnePixel wurde gewählt.")
    player = OhnePixel("männlich", 20, 8, 40, 10, 1200, 1)

print(f"\nDu spielst als {player.name}.")
print(f"Stats → HP: {player.hp} | DMG: {player.dmg} | Glück: {player.luck} | Geld: {player.money}€\n")

# FIGHTING
print("\nDie Sucht beginnt...\n")

while player.is_alive():
    print("Eine neue Case erscheint!\n")

    anubis_case.create_enemy()

    while player.is_alive() and not anubis_case.is_defeated():
        dmg = player.attack()
        anubis_case.case_hp -= dmg
        print(f"Du greifst die Case an und machst {dmg} Schaden.")

        if anubis_case.is_defeated():
            break

        player.hp -= anubis_case.case_dmg
        print(f"Die Case trifft dich für {anubis_case.case_dmg} Schaden.")
        print(f"Deine HP: {player.hp}\n")

    if not player.is_alive():
        break

    # CASE DEFEATED
    cases_defeated += 1
    print("Die Case wurde besiegt!")

    # PRICE CHECK
    case_price = 4.31

    while player.money < case_price:
        print("Nicht genug Geld, um die Case zu öffnen.")
        sell_choice = input("Skins verkaufen? (j/n): ").lower()

        if sell_choice == "j":
            sell_menu(player)
        else:
            print("Dein Run endet hier.")
            player.hp = 0
            break

    if not player.is_alive():
        break

    player.money -= case_price
    print(f"Du zahlst {case_price:.2f}€ zum Öffnen der Case.")
    print(f"Verbleibendes Geld: {player.money:.2f}€\n")

    print("Die Case öffnet sich...\n")

    # RNG DROP
    rolls = 1 + player.luck // 20
    names, prices = anubis_case.open(rolls)

    best_index = prices.index(max(prices))
    weapon = names[best_index]
    value = prices[best_index]

    player.inventory.add_item(weapon, value)
    total_inventory_value += value

    print(f"DROP: {weapon} ({value}€)")
    print(f"Cases besiegt: {cases_defeated}")
    print(f"Aktueller Inventarwert: {total_inventory_value:.2f}€\n")

    # HP recovery
    player.hp += 5
    print("Du erholst dich leicht (+5 HP)\n")

# RESULT
if not player.is_alive():
    print("Du wurdest von der Case besiegt.")
    print("\n DU BIST GESTORBEN! 💀🥀\n")

print("===== GAME OVER =====")
print(f"Spieler: {player.name}")
print(f"Cases besiegt: {cases_defeated}")
print(f"Inventarwert: {total_inventory_value:.2f}€")
print("\nInventar:")
print(player.inventory.show())

score = int(cases_defeated * 10 + total_inventory_value)
print(f"\n🏆 ENDSCORE: {score}")
quit()

# OPEN CASE
rolls = 1 + player.luck // 20
names, prices = anubis_case.open(rolls)

best_index = prices.index(max(prices))
weapon = names[best_index]
value = prices[best_index]

player.inventory.add_item(weapon, value)

print(f"DROP ERHALTEN: {weapon} ({value}€)\n")

# INVENTORY
print("Dein Inventar:")
print(player.inventory.show())

# SELLING
def sell_menu(player):
    if not player.inventory.items:
        print("Du hast keine Skins zum Verkaufen.\n")
        return

    print("\n===== INVENTAR VERKAUF =====")
    for i, (name, value) in enumerate(player.inventory.items):
        print(f"{i + 1}) {name} ({value}€)")

    choice = input("Nummer zum Verkaufen (oder ENTER zum Abbrechen): ")

    if choice == "":
        print("Verkauf abgebrochen.\n")
        return

    if not choice.isdigit():
        print("Ungültige Eingabe.\n")
        return

    index = int(choice) - 1
    sold = player.inventory.sell_item(index)

    if sold:
        name, value = sold
        player.money += value
        print(f"Verkauft: {name} für {value}€")
        print(f"Neues Guthaben: {player.money:.2f}€\n")
    else:
        print("Ungültige Auswahl.\n")




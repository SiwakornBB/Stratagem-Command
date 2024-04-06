import tkinter as tk
import threading
import keyboard

# Define the stratagem commands
stratagem_commands ={
    "▼◄▼▲►": "Machine Gun",
    "▼◄►▲▼": "Anti-Material Rifle",
    "▼◄▼▲▲◄": "Stalwart",
    "▼▼◄▲►": "Expendable Anti-Tank",
    "▼◄►►◄": "Recoilless Rifle",
    "▼◄▲▼▲": "Flamethrower",
    "▼►◄▼▼▲▲►": "Autocannon",
    "▼►◄▼▼▲◄▼►": "Railgun",
    "▼▼▲▼▼": "Spear",
    "►▼◄▲▲": "Gatling Barrage",
    "►►►": "Airburst Strike",
    "►▼▼◄▼►▼▼": "120MM HE Barrage",
    "►▼▼▲▲◄▼▼▼": "380MM HE Barrage",
    "►▼►▼►▼": "Walking Barrage",
    "►▲◄▲►◄": "Laser Strike",
    "►▼▲▼◄": "Railcannon Strike",
    "▲►►": "Eagle Strafing Run",
    "▲►▼►": "Eagle Airstrike",
    "▲►▼▼►▼": "Eagle Cluster Bomb",
    "▲►▼▲": "Eagle Napalm Airstrike",
    "▼▲▲▼▲": "Jump Pack",
    "▲►▲▼": "Eagle Smoke Strike",
    "▲▼▲◄": "Eagle 110MM Rocket Pods",
    "▲◄▼▼▼": "Eagle 500KG Bomb",
    "►►▲": "Orbital Precision Strikes",
    "►►▼►": "Orbital Gas Strike",
    "►►◄▼": "Orbital EMS Strike",
    "►►▼▲": "Orbital Smoke Strike",
    "▲▼◄►►◄": "HMG Emplacement",
    "▼▲◄►◄▼": "Shield Generator Relay",
    "▼▲►▲◄►": "Tesla Tower",
    "▼◄▲►": "Anti-Personnel Minefield",
    "▼◄▼▲▲▼": "Supply Pack",
    "▼◄▼▲◄▼▼": "Grenade Launcher",
    "▼◄▼▲◄": "Laser Cannon",
    "▼◄◄▼": "Incendiary Mines",
    "▼◄▼▲◄▼▼": "Guard Dog Rover",
    "▼◄▲▲►": "Ballistic Shield Backpack",
    "▼►▲◄▼": "Arc Thrower",
    "▼▲◄▼►►": "Shield Generator Pack",
    "▼▲►►▲": "Machine Gun Sentry",
    "▼▲►◄▼": "Gatling Sentry",
    "▼▲►►▼": "Mortar Sentry",
    "▼▲◄▲►▼": "Guard Dog",
    "▼▲►▲◄▲": "Autocannon Sentry",
    "▼▲►►◄": "Rocket Sentry",
    "▼▼▲▲◄": "EMS Mortar Sentry",
    "▲▼►◄▲": "Reinforce",
    "▲▼►▲": "SOS Beacon",
    "▼▲▼▲": "Super Earth Flag",
    "◄►▲▲▲": "Upload Data",
    "▼▲◄▼▲►▼▲": "Hellbomb",
    "▼▼▲►": "Resupply"
}

def translate_key_to_arrow(key):
    return key.replace('w', '▲').replace('s', '▼').replace('a', '◄').replace('d', '►')

def update_sequence(sequence, sequence_label):
    # Translate WASD to arrow characters
    sequence_arrows = ''.join(translate_key_to_arrow(k) for k in sequence)
    sequence_label.config(text=f"Input: {sequence_arrows}")

def stratagem_menu(sequence_label, command_label):
    sequence = ''
    while True:
        if keyboard.is_pressed('ctrl'):
            for key in 'wasd':
                if keyboard.is_pressed(key):
                    sequence += translate_key_to_arrow(key)
                    sequence_label.after(0, update_sequence, sequence, sequence_label)
                    while keyboard.is_pressed(key):
                        continue  # Wait until key is released to avoid repeated characters

            if sequence in stratagem_commands:
                command_label.config(text=f"Command: {stratagem_commands[sequence]}")
                while keyboard.is_pressed('ctrl'):
                    continue  # Wait until CTRL is released to reset
        else:
            if sequence:
                sequence = ''  # Reset sequence if CTRL is not held
                sequence_label.config(text="Input:")
                command_label.config(text="Command:")
                continue



def start_stratagem_menu_thread(sequence_label, command_label):
    threading.Thread(target=stratagem_menu, args=(sequence_label, command_label), daemon=True).start()

def main():
    root = tk.Tk()
    root.title("Stratagem Command")

    # Create a Listbox to display the list of commands
    command_listbox = tk.Listbox(root, font=('Helvetica', 14), height=30, width=50, bd=0)
    command_listbox.pack()

    # Add some commands to the Listbox
    commands = [
    ("Machine Gun", "▼◄▼▲►"),
    ("Anti-Material Rifle", "▼◄►▲▼"),
    ("Stalwart", "▼◄▼▲▲◄"),
    ("Expendable Anti-Tank", "▼▼◄▲►"),
    ("Recoilless Rifle", "▼◄►►◄"),
    ("Flamethrower", "▼◄▲▼▲"),
    ("Autocannon", "▼►◄▼▼▲▲►"),
    ("Railgun", "▼►◄▼▼▲◄▼►"),
    ("Spear", "▼▼▲▼▼"),
    ("Gatling Barrage", "►▼◄▲▲"),
    ("Airburst Strike", "►►►"),
    ("120MM HE Barrage", "►▼▼◄▼►▼▼"),
    ("380MM HE Barrage", "►▼▼▲▲◄▼▼▼"),
    ("Walking Barrage", "►▼►▼►▼"),
    ("Laser Strike", "►▲◄▲►◄"),
    ("Railcannon Strike", "►▼▲▼◄"),
    ("Eagle Strafing Run", "▲►►"),
    ("Eagle Airstrike", "▲►▼►"),
    ("Eagle Cluster Bomb", "▲►▼▼►▼"),
    ("Eagle Napalm Airstrike", "▲►▼▲"),
    ("Jump Pack", "▼▲▲▼▲"),
    ("Eagle Smoke Strike", "▲►▲▼"),
    ("Eagle 110MM Rocket Pods", "▲▼▲◄"),
    ("Eagle 500KG Bomb", "▲◄▼▼▼"),
    ("Orbital Precision Strikes", "►►▲"),
    ("Orbital Gas Strike", "►►▼►"),
    ("Orbital EMS Strike", "►►◄▼"),
    ("Orbital Smoke Strike", "►►▼▲"),
    ("HMG Emplacement", "▲▼◄►►◄"),
    ("Shield Generator Relay", "▼▲◄►◄▼"),
    ("Tesla Tower", "▼▲►▲◄►"),
    ("Anti-Personnel Minefield", "▼◄▼▲►"),
    ("Supply Pack", "▼◄▼▲▲▼"),
    ("Grenade Launcher", "▼◄▼▲◄▼▼"),
    ("Laser Cannon", "▼◄▼▲◄"),
    ("Incendiary Mines", "▼◄◄▼"),
    ("Guard Dog Rover", "▼◄▼▲◄▼▼"),
    ("Ballistic Shield Backpack", "▼◄▲▲►"),
    ("Arc Thrower", "▼►▲◄▼"),
    ("Shield Generator Pack", "▼▲◄▼►►"),
    ("Machine Gun Sentry", "▼▲►►▲"),
    ("Gatling Sentry", "▼▲►◄▼"),
    ("Mortar Sentry", "▼▲►►▼"),
    ("Guard Dog", "▼▲◄▲►▼"),
    ("Autocannon Sentry", "▼▲►▲◄▲"),
    ("Rocket Sentry", "▼▲►►◄"),
    ("EMS Mortar Sentry", "▼▼▲▲◄"),
    ("Reinforce", "▲▼►◄▲"),
    ("SOS Beacon", "▲▼►▲"),
    ("Super Earth Flag", "▼▲▼▲"),
    ("Upload Data", "◄►▲▲▲"),
    ("Hellbomb", "▼▲◄▼▲►▼▲"),
    ("Resupply", "▼▼▲►")
]
    for command_name, command_sequence in stratagem_commands.items():
        if len(command_name.split()) > 2:
            display_text = f"({command_name}) - {command_sequence}"
        else:
            display_text = f"{command_name} - {command_sequence}"
        command_listbox.insert(tk.END, display_text)

    sequence_label = tk.Label(root, text="Input:", font=('Helvetica', 14))
    sequence_label.pack()

    command_label = tk.Label(root, text="Command:", font=('Helvetica', 14))
    command_label.pack()

    start_stratagem_menu_thread(sequence_label, command_label)

    root.mainloop()

if __name__ == "__main__":
    main()

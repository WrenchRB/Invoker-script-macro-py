import time
import keyboard

useWhenMakeSpell = True
#for combo you need aghanim and refresher
#for combo2 you need aghanim
#Everything I do in here is assuming that the hotkeys for invoker are q for quas, e for wex, r for exort, s for ult, t and g are the spell buttons to cast and z for refresher item
#You should use quick casting in dota 2 for these to work
# Function to send key press
def send_key_press(key):
    key = key.lower()
    keyboard.press_and_release(key)

# Dota 2 abilities functions
def coldsnap(use=False):
    for key in 'QQQ':
        send_key_press(key)
        time.sleep(0.1)
    send_key_press('S')
    time.sleep(0.1)
    send_key_press('T')
    time.sleep(0.1)

def instantInvis(use=False):
    for key in 'QQE':
        send_key_press(key)
        time.sleep(0.1)
    send_key_press('S')
    time.sleep(0.1)
    for key in 'EEE':
        send_key_press(key)
        time.sleep(0.1)
    time.sleep(0.3)
    if use:
        send_key_press('T')
        time.sleep(0.1)

def iceWall(use=False):
    for key in 'QQR':
        send_key_press(key)
        time.sleep(0.1)
    send_key_press('S')
    time.sleep(0.1)
    if use:
        send_key_press('T')
        time.sleep(0.1)

def EMP(use=False):
    for key in 'EEE':
        send_key_press(key)
        time.sleep(0.1)
    send_key_press('S')
    time.sleep(0.1)
    if use:
        send_key_press('T')
        time.sleep(0.1)

def tornado(use=False):
    for key in 'EEQ':
        send_key_press(key)
        time.sleep(0.1)
    send_key_press('S')
    time.sleep(0.1)
    if use:
        send_key_press('T')
        time.sleep(0.1)

def alacrity(use=False):
    for key in 'EER':
        send_key_press(key)
        time.sleep(0.1)
    send_key_press('S')
    time.sleep(0.1)
    if use:
        keyboard.press('ALT')
        time.sleep(0.1)
        send_key_press('T')
        time.sleep(0.1)
        keyboard.release('ALT')


def sonicWave(use=False):
    for key in 'QER':
        send_key_press(key)
        time.sleep(0.1)
    send_key_press('S')
    time.sleep(0.1)
    if use:
        send_key_press('T')
        time.sleep(0.1)


def sunstrike(use=False):
    for key in 'RRR':
        send_key_press(key)
        time.sleep(0.1)
    send_key_press('S')
    if use:
        keyboard.press('ALT')
        time.sleep(0.1)
        send_key_press('T')
        time.sleep(0.1)
        keyboard.release('ALT')
        time.sleep(0.1)
        send_key_press('T')
        time.sleep(0.1)

def forgedSpirits(use=False):
    for key in 'RRQ':
        send_key_press(key)
        time.sleep(0.1)
    send_key_press('S')
    if use:
        time.sleep(0.1)
        send_key_press('T')

def meatball(use=False):
    for key in 'RRE':
        send_key_press(key)
        time.sleep(0.1)
    send_key_press('S')
    time.sleep(0.1)
    if use:
        send_key_press('T')
        time.sleep(0.1)

def eulsSunstrike(use=False):
    send_key_press('T')
    # time.sleep(0.1)
    sunstrike()
    time.sleep(0.2)
    send_key_press('T')

def fullCombo(use=False):
    tornado()
    time.sleep(0.3)
    sunstrike()
    time.sleep(0.1)
    send_key_press('G')
    time.sleep(0.5)
    EMP()
    time.sleep(0.1)
    send_key_press('T')
    time.sleep(0.1)
    time.sleep(0.2)
    keyboard.press('ALT')
    time.sleep(0.1)
    send_key_press('G')
    time.sleep(0.1)
    keyboard.release('ALT')
    time.sleep(0.1)
    sonicWave()
    time.sleep(0.6)
    meatball()
    time.sleep(0.5)
    send_key_press('T')
    time.sleep(0.1)
    send_key_press('G')
    time.sleep(0.1)
    
def fullCombo2(use=False):
    tornado()
    time.sleep(0.3)
    sunstrike()
    time.sleep(0.1)
    send_key_press('G')
    time.sleep(0.5)
    EMP()
    time.sleep(0.1)
    send_key_press('T')
    time.sleep(0.1)
    time.sleep(0.2)
    keyboard.press('ALT')
    time.sleep(0.1)
    send_key_press('G')
    time.sleep(0.1)
    keyboard.release('ALT')
    time.sleep(0.1)
    sonicWave()
    time.sleep(0.6)
    meatball()
    time.sleep(0.5)
    send_key_press('T')
    time.sleep(0.2)
    send_key_press('G')
    time.sleep(0.1)
    send_key_press('Z')
    tornado()
    time.sleep(0.3)
    sunstrike()
    time.sleep(0.1)
    send_key_press('G')
    time.sleep(0.5)
    EMP()
    time.sleep(0.1)
    send_key_press('T')
    time.sleep(0.1)
    time.sleep(0.2)
    keyboard.press('ALT')
    time.sleep(0.1)
    send_key_press('G')
    time.sleep(0.1)
    keyboard.release('ALT')
    time.sleep(0.1)
    sonicWave()
    time.sleep(0.6)
    meatball()
    time.sleep(0.5)
    send_key_press('T')
    time.sleep(0.2)
    send_key_press('G')
    time.sleep(0.1)

def fullCombo(use=False):
    tornado()
    time.sleep(0.3)
    sunstrike()
    time.sleep(0.1)
    send_key_press('G')
    time.sleep(0.5)
    EMP()
    time.sleep(0.1)
    send_key_press('T')
    time.sleep(0.1)
    time.sleep(0.2)
    keyboard.press('ALT')
    time.sleep(0.1)
    send_key_press('G')
    time.sleep(0.1)
    keyboard.release('ALT')
    time.sleep(0.1)
    sonicWave()
    time.sleep(0.6)
    meatball()
    time.sleep(0.5)
    send_key_press('T')
    time.sleep(0.2)
    send_key_press('G')
    time.sleep(0.1)
    send_key_press('T')
    
def fullCombo2(use=False):
    tornado()
    time.sleep(0.3)
    sunstrike()
    time.sleep(0.1)
    send_key_press('G')
    time.sleep(0.5)
    EMP()
    time.sleep(0.1)
    send_key_press('T')
    time.sleep(0.1)
    time.sleep(0.2)
    keyboard.press('ALT')
    time.sleep(0.1)
    send_key_press('G')
    time.sleep(0.1)
    keyboard.release('ALT')
    time.sleep(0.1)
    sonicWave()
    time.sleep(0.6)
    meatball()
    time.sleep(0.5)
    send_key_press('T')
    time.sleep(0.2)
    send_key_press('G')
    time.sleep(0.1)
    send_key_press('Z')
    tornado()
    time.sleep(0.3)
    sunstrike()
    time.sleep(0.1)
    send_key_press('G')
    time.sleep(0.5)
    EMP()
    time.sleep(0.1)
    send_key_press('T')
    time.sleep(0.1)
    time.sleep(0.2)
    keyboard.press('ALT')
    time.sleep(0.1)
    send_key_press('G')
    time.sleep(0.1)
    keyboard.release('ALT')
    time.sleep(0.1)
    sonicWave()
    time.sleep(0.6)
    meatball()
    time.sleep(0.5)
    send_key_press('T')
    time.sleep(0.2)
    send_key_press('G')
    time.sleep(0.1)
    send_key_press('T')

key_function_mapping = {
    '1': coldsnap,
    'f1': instantInvis,
    '4': iceWall,
    '6': EMP,
    '5': tornado,
    '3': alacrity,
    '7': sonicWave,
    '9': sunstrike,
    '2': forgedSpirits,
    '8': meatball,
    'f7': eulsSunstrike,
    'f6': fullCombo,
    'f5': fullCombo2,
}

while True:
    event = keyboard.read_event()
    if event.event_type == 'down':
        key = event.name.lower()
        if key in key_function_mapping:
            key_function_mapping[key](useWhenMakeSpell)
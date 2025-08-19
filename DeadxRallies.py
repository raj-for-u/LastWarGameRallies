from scapy.all import sniff, TCP, Raw, IP
import datetime
import pyautogui
import time
import random
import re
from pynput.mouse import Controller
from pynput.keyboard import Controller as KeyboardController, Key
import pyautogui
from constants import *

# Create a controller objects
keyboard = KeyboardController()
mouse = Controller()

def keyboard_esc(count=3):
    for _ in range(count):
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        time.sleep(1)

def check_exit():
    try:
        location = pyautogui.locateOnScreen('quit_game.png', confidence=0.9)
        if location:
            print("Quit game window found!")
            keyboard_esc(1)
        else:
            print("Image not found, but no exception raised.")
    except pyautogui.ImageNotFoundException:
        print("Handled: quit_game.png not found on screen (ImageNotFoundException)")

def packet_callback(packet):

    if packet.haslayer(TCP) and packet.haslayer(Raw):
        try:
            payload = packet[Raw].load

            if Rally_KEYWORD in payload and targetUid_KEYWORD in payload:

                pyautogui.moveTo(red_dot_x_y)
                pyautogui.click()

                time.sleep(1)
                pyautogui.moveTo(add_queue_x_y)
                time.sleep(1)
                pyautogui.click()

                time.sleep(1)
                pyautogui.moveTo(march_x_y)
                time.sleep(1)
                pyautogui.click()

                time.sleep(1)
                pyautogui.moveTo(hero_squad_x_y)  # Hero Squad rally 1/4
                pyautogui.click()

                keyboard_esc(3)
                check_exit()
                print("✅ Rally finished successfully!")

        except Exception as e:
            print("❌ Error processing packet:", e)

print("🎮 Sniffing for ONEC Rally March Events... (Press Ctrl+C to stop)")
sniff(iface=INTERFACE, prn=packet_callback, store=0)

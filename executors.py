import os
import sys
import webbrowser

def list():
    print("== List of Executors ==")
    print("1. Mono (99% sUNC!)")
    print("2. Velocity (Decompiler x 98% sUNC!)")
    print("3. Valex (Keyed x Decompiler x 94% sUNC!)")
    print("4. Potassium (Paid, OP, 100% sUNC $20, decompiler, and more!)")


def select():
    choice = input("Choose an option: ")
    if choice == "1":
        webbrowser.open('https://getmono.netlify.app/')
    elif choice == "2":
        webbrowser.open('https://getvelocity.live/')
    elif choice == "3":
        webbrowser.open('https://valex.io/')
    elif choice == "4":
        webbrowser.open('https://potassium.pro/')
    else:
        print("Please select a valid option, see the options using the multitool.")
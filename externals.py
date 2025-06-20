import os
import sys
import webbrowser

def externals():
    print("== List of External Exploits ==")
    print("1. Thunder External (Top Tier, Free x Keyless)")
    print("2. Matcha (Decompiler x Lua-U Engine x BEST External x Paid $11.50 Lifetime)")
    print("3. Valex (Keyed x Decompiler x Decent)")
    print("4. Canada External (Decompiler x Lua Execution x Internal Mode)")
    print("5. Matrix Hub (TONS OF GAME SUPPORT, Triggerbot, OP Silent Aim, $5 Lifetime)")


def openexternals():
    choice = input("Choose an option: ")
    if choice == "1":
        webbrowser.open('https://discord.gg/jWc9mf7Te9')
    elif choice == "2":
        webbrowser.open('https://discord.gg/eR6zF2YuQB')
    elif choice == "3":
        webbrowser.open('https://valex.io/')
    elif choice == "4":
        webbrowser.open('about:blank')
    elif choice == "5":
        webbrowser.open('https://matrixhubs.shop/')
    else:
        print("Please select a valid option, see the options using the multitool.")

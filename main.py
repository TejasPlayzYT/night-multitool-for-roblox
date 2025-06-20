from fishstrap import fishstrap, bloxstrap
from headlessxkorblox import korblox
from executors import list, select
from externals import externals, openexternals

print("== Night Multitool for Roblox ==")
print("1. Fishstrap")
print("2. Bloxstrap")
print("3. Korblox")
print("4. Executors")
print("5. External Exploits")
print("6. Exit")

choice = input("Choose an option:")
if choice == "1":
    print("Installing and optimizing Fishstrap...")
    fishstrap()
elif choice == "2":
    print("Installing and optimizing Bloxstrap...")
    bloxstrap()
elif choice == "3":
    print("Installing FOSS Application for Headless and Korblox Free!")
    korblox()
elif choice == "4":
    list()
    select()
elif choice == "5":
    externals()
    openexternals()
elif choice == "6":
    print("Goodbye!")
    exit()
else:
    print("Invalid choice. Please try again.")

import time
import os
from playsound import playsound


# Print user menu
def menu():
    print(5*'-' + " Choose " + 5*'-')
    print("1 : Study Time (25 minutes)")
    print("2 : Short Break (5 minutes)")
    print("3 : Long Break (15 minutes)")
    print("4 : Enter Your Custom Time")
    userChoice = input("Your choice : ")
    return userChoice


# Print time in clock way
def clockDisplay(m, s):
    # m : minute, s : second
    if m >= 0 and m < 10:
        print(f"0{m} : ", end="")
    else:
        print(f"{m} : ", end="")
    if s >= 0 and s < 10:
        print(f"0{s}")
    else:
        print(f"{s}")


# Run timer with specefic duration
def runTimer(minutes):
    seconds = 0
    while minutes != 0 or seconds != 0:
        clockDisplay(minutes, seconds)
        if seconds == 0:
            seconds = 59
            minutes -= 1
        else:
            seconds -= 1
        time.sleep(1)
        os.system("clear")


def main():
    duration = menu()
    if duration in ['1', 1]:
        runTimer(25)
    elif duration in ['2', 2]:
        runTimer(5)
    elif duration in ['3', 3]:
        runTimer(15)
    elif duration in ['4', 4]:
        specDur = int(input("Enter your specefic duration :"))
        runTimer(specDur)
    playsound("alarm.wav")


if __name__ == "__main__":
    main()

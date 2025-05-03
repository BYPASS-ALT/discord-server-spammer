import requests
import threading
import time
import os
import signal

PROXY = {
    "http": "your_proxy",
    "https": "your_proxy"
}

USE_PROXY = True  # Flip to False if proxy blocks
THREADS = 5       # Number of spam threads
DELAY = 1         # Delay between each message (seconds)

webhook_url = ""
message = ""
spam_count = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def logo():
    print(r"""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█░▄▀██▄██░▄▄█▀▄▀█▀▄▄▀█░▄▄▀█░▄▀███░▄▄█░▄▄█░▄▄▀█▀███▀█░▄▄█░▄▄▀███░▄▄█▀▄▄▀█░▄▄▀█░▄▀▄░█░▄▀▄░█░▄▄█░▄▄▀
█░█░██░▄█▄▄▀█░█▀█░██░█░▀▀▄█░█░███▄▄▀█░▄▄█░▀▀▄██░▀░██░▄▄█░▀▀▄███▄▄▀█░▀▀░█░▀▀░█░█▄█░█░█▄█░█░▄▄█░▀▀▄
█▄▄██▄▄▄█▄▄▄██▄███▄▄██▄█▄▄█▄▄████▄▄▄█▄▄▄█▄█▄▄███▄███▄▄▄█▄█▄▄███▄▄▄█░████▄██▄█▄███▄█▄███▄█▄▄▄█▄█▄▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

    >> MADE BY THE HUMAN ☠️
    """)

def send(webhook_url, message):
    global spam_count
    while spam_count > 0:
        try:
            response = requests.post(
                webhook_url,
                json={"content": message},
                proxies=PROXY if USE_PROXY else None,
                timeout=10
            )

            if response.status_code == 204:
                print("[+] Message sent")
            # Silent for all non-204 responses
            spam_count -= 1
        except:
            pass  # Silently ignore all errors

        time.sleep(DELAY)

def handle_exit_signal(signal, frame):
    print("\n[!] Please enjoy human's bomb ☠️")
    exit(0)

signal.signal(signal.SIGINT, handle_exit_signal)

def menu():
    global webhook_url, message, spam_count

    while True:
        clear()
        logo()

        print("""
        01: Enter Webhook URL
        02: Enter Message
        03: Enter Number of Messages to Spam
        04: Start Spamming
        05: Exit
        """)

        choice = input("Choose an option ➤ ").strip()

        if choice == "1":
            webhook_url = input("\nEnter Webhook URL ➤ ").strip()
            print("[+] Webhook URL set successfully")
            time.sleep(1)

        elif choice == "2":
            message = input("Enter Message ➤ ").strip()
            print("[+] Message set successfully")
            time.sleep(1)

        elif choice == "3":
            try:
                spam_count = int(input("Enter number of messages to spam ➤ ").strip())
                print(f"[+] Spamming {spam_count} messages")
                time.sleep(1)
            except ValueError:
                print("[!] Please enter a valid number.")
                time.sleep(1)

        elif choice == "4":
            if not webhook_url or not message or spam_count == 0:
                print("[!] Please set the Webhook URL, Message, and Spam Count first.")
                time.sleep(1)
                continue
            print("[+] Starting the spamming process...")
            for _ in range(THREADS):
                threading.Thread(target=send, args=(webhook_url, message), daemon=True).start()
            time.sleep(1)

        elif choice == "5":
            print("please enjoy human's bomb")
            exit(0)

        else:
            print("[!] Invalid choice. Please try again.")
            time.sleep(1)

def main():
    clear()
    menu()

if __name__ == "__main__":
    main()

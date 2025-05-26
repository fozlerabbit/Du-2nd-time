import webbrowser
import pyautogui
import time
import os
import random

# Files
numbers_file = 'numbers.txt'
sent_file = 'sent_numbers.txt'

# How many times to send the message per number
SEND_COUNT = 1

# Ensure sent_numbers.txt exists
if not os.path.exists(sent_file):
    with open(sent_file, 'w') as f:
        pass  # Just create an empty file

# Load numbers from file
with open(numbers_file, 'r') as f:
    numbers = [line.strip() for line in f.readlines() if line.strip()]

sent_numbers = []

for num in numbers:
    if len(num) == 10 :
        num = '0' + num
       

    url = f"https://wa.me/{num}?text=%E2%80%98%E0%A6%A2%E0%A6%BE%E0%A6%95%E0%A6%BE%20%E0%A6%AC%E0%A6%BF%E0%A6%B6%E0%A7%8D%E0%A6%AC%E0%A6%AC%E0%A6%BF%E0%A6%A6%E0%A7%8D%E0%A6%AF%E0%A6%BE%E0%A6%B2%E0%A7%9F%E0%A7%87%20%E0%A6%B8%E0%A7%87%E0%A6%95%E0%A7%87%E0%A6%A8%E0%A7%8D%E0%A6%A1%20%E0%A6%9F%E0%A6%BE%E0%A6%87%E0%A6%AE%E2%80%99%20%E0%A6%A6%E0%A6%BE%E0%A6%AC%E0%A6%BF%E0%A6%A4%E0%A7%87%20%E0%A6%A8%E0%A6%BF%E0%A6%9C%E0%A7%87%20%E0%A6%AA%E0%A6%BF%E0%A6%9F%E0%A6%BF%E0%A6%B6%E0%A6%A8%20%E0%A6%AB%E0%A6%B0%E0%A6%AE%20%E0%A6%AA%E0%A7%82%E0%A6%B0%E0%A6%A3%20%E0%A6%95%E0%A6%B0%E0%A7%81%E0%A6%A8%20%E0%A6%8F%E0%A6%AC%E0%A6%82%20%E0%A6%85%E0%A6%A8%E0%A7%8D%E0%A6%AF%E0%A6%A6%E0%A7%87%E0%A6%B0%E0%A6%93%20%E0%A6%95%E0%A6%B0%E0%A6%A4%E0%A7%87%20%E0%A6%AC%E0%A6%B2%E0%A7%81%E0%A6%A8%E0%A5%A4%0A%0A%E0%A6%AB%E0%A6%B0%E0%A6%AE%20%E0%A6%B2%E0%A6%BF%E0%A6%82%E0%A6%95%3A%20https%3A%2F%2Fshorturl.at%2FG5xj1%0A%0A%E0%A6%AC%E0%A6%BF%E0%A6%B7%E0%A7%9F%E0%A6%9F%E0%A6%BF%20%E0%A6%85%E0%A6%A4%E0%A7%80%E0%A6%AC%20%E0%A6%9C%E0%A6%B0%E0%A7%81%E0%A6%B0%E0%A6%BF%E0%A5%A4%0A%0A~Pupils'%20Perspective"
    webbrowser.open(url)
    time.sleep(8)  # Wait for page to load

    try:
        # Press 'Enter' to go through WhatsApp buttons
        pyautogui.press('enter')  # Continue to Chat
        time.sleep(6)
        pyautogui.press('enter')  # Use WhatsApp Web
        time.sleep(12)

        # Send the message
        for _ in range(SEND_COUNT):
            pyautogui.typewrite(MESSAGE)
            pyautogui.press('enter')
            time.sleep(1)

        print(f"Message sent to: {num}")
        sent_numbers.append(num)

        # Wait 20–25 seconds randomly
        wait_time = random.randint(20, 25)
        time.sleep(wait_time)

    except Exception as e:
        print(f"Failed for number {num}: {e}")

# Append successful numbers to sent_numbers.txt
with open(sent_file, 'a') as f:
    for number in sent_numbers:
        f.write(f"{number}\n")

print("All done! Sent numbers saved to sent_numbers.txt.")

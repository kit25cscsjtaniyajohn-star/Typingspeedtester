
import time
text = "Typing speed test measures how fast and accurately you type."
print("Type the following text:\n")
print(text)
input("\nPress Enter when you are ready...")
start = time.time()
typed = input("\nStart typing:\n")
end = time.time()
time_taken = end - start
words = len(typed.split())
wpm = (words / time_taken) * 60
correct_chars = 0
for i in range(min(len(text), len(typed))):
    if text[i] == typed[i]:
        correct_chars += 1
accuracy = (correct_chars / len(text)) * 100
print("\nTime taken:", round(time_taken, 2), "seconds")
print("WPM:", round(wpm, 2))
print("Accuracy:", round(accuracy, 2), "%")

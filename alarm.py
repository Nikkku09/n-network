import time
import playsound
b =time.localtime()
formatted_time = time.strftime("%H:%M", b)
print(f"Current time (24-hour format using time module): {formatted_time}")


a= input()
b =time.time()

if a == formatted_time:
    audio_file_path = r"C:\Users\Prafu\Downloads\mixkit-classic-alarm-995.wav" # or .wav, etc.

    playsound(audio_file_path)
# SoundLevels.py
#
# Author: Aditya Thakur
# Date: March 2026

# Get user input for sound level
decibel = float(input("Enter the sound level in decibels: "))

# Determine the noise or range
if decibel < 40:
    message = "The sound is quieter than a quiet room."
elif decibel == 40:
    message = "This is the sound of a quiet room."
elif 40 < decibel < 70:
    message = "The sound is between a quiet room and an alarm clock."
elif decibel == 70:
    message = "This is the sound of an alarm clock."
elif 70 < decibel < 106:
    message = "The sound is between an alarm clock and a petrol lawnmower."
elif decibel == 106:
    message = "This is the sound of a petrol lawnmower."
elif 106 < decibel < 130:
    message = "The sound is between a petrol lawnmower and a jackhammer."
elif decibel == 130:
    message = "This is the sound of a jackhammer."
else:  # decibel > 130
    message = "The sound is louder than a jackhammer."


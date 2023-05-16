import os
import time
import random
import math
from pydub import AudioSegment
from pydub.playback import play


SOUND_DIRECTORY = os.path.abspath('sounds')  # Directory to load sounds from.
MIN_INTERVAL = 5*60  # Minimum time between sounds in seconds.
MAX_INTERVAL = 60*60  # Maximum time between sounds in seconds.
SIGMOID = True  # Uses the alternative delay generater, ignores MIN_INTERVAL


def get_valid_files(do_logging=False):
    files = os.listdir(SOUND_DIRECTORY)
    valid_files = []
    log = 'Loaded files:'

    for file in files:
        if file.endswith('.wav'):
            valid_files.append(file)
            if do_logging:
                log += ' ' + file
    print(log)
    return valid_files


def play_random_sound(options, do_logging=False):
    file = random.choice(options)
    wav = AudioSegment.from_wav(SOUND_DIRECTORY + '/' + file)
    play(wav)
    if do_logging:
        print('Played sound: ' + file)


def do_random_loop(min_seconds, max_seconds, sounds, sigmoid=True, do_logging=False):
    while True:
        if sigmoid:
            delay = calculate_delay_time(max_seconds)
        else:
            delay = random.randint(min_seconds, max_seconds)
        if do_logging:
            print("Delay set to " + str(delay) + " seconds.")
        time.sleep(delay)
        play_random_sound(sounds, do_logging)

def calculate_delay_time(max_seconds):
    x = random.uniform(0, 10)
    x = 6 - x
    x = math.e**x
    x = 1 + x
    x = max_seconds / x
    return math.ceil(x)

library = get_valid_files(True)
do_random_loop(MIN_INTERVAL, MAX_INTERVAL, library, SIGMOID, True)

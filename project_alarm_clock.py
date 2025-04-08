import time
import datetime
import pygame


def set_alarm(alram_time) :
    print(f"alarm set for {alram_time}")
    sound_file = "BRITISH VS AMERICAN ACCENT EXPLAINED(1080P_HD).mp4"
    is_ruuning = True
    while is_ruuning :
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        time.sleep(1)
        if current_time == alram_time :
            print("WAKE UP!!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() :
                   time.sleep(1)

            is_ruuning = False

alarm_time = input("please set your alarm(HH:MM:SS)")
set_alarm(alarm_time)
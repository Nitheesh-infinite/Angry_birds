import pygame
import constants as c

def play_music():
    sound = c.sound_files[c.current_sound_index]
    if sound:
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play(-1)
        c.music_playing = True
    else:
        stop_music()

def stop_music():
    pygame.mixer.music.stop()
    c.music_playing = False

def toggle_music():
    c.current_sound_index = (c.current_sound_index + 1) % len(c.sound_files)
    play_music()

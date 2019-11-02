import pygame, sys
file = song = '/root/Downloads/Antipozitiv.mp3'
def play(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
            pos = pygame.mixer.music.get_pos()/ 1000




    pygame.mixer.init(22050, -16, 2, 2048)
    pygame.mixer.music.set_volume(2.0)
    play(song)
    pygame.quit()


play(song)

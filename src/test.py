
    
import vlc
import threading
import time


def play(sound: vlc.MediaPlayer, start, end):
    sound.play()
    time.sleep(end - start)     # in seconds
    sound.stop()
    return True


if __name__ == '__main__':
    my_sound = vlc.MediaPlayer(obtenerPathAbsoluto("p1.wav", __file__))
    sound_thread = threading.Thread(target=play, args=([my_sound, 1, 2]))
    sound_thread.start()

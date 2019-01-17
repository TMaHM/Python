import time

screen_dir = 'D:\\hello\\'

cur_time = time.strftime("%m%d_%H%M%S", time.localtime())

stored_screen = ("%s_%s", screen_dir, cur_time)

print(stored_screen)
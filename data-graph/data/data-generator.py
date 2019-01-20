import csv, os, time
import numpy as np

if os.path.exists('data.csv'):
    os.remove('data.csv')

frame = -1
counter = 200

while True:
    time.sleep(1)
    frame += 1
    counter -= 2

    with open("data.csv", "a+", newline='') as f:
        w = csv.writer(f)
        w.writerow([frame, np.sin((np.pi/2) * frame), frame, counter, 4, 4, 4, 4, 4, 4, 4])

    print('update #', frame + 1)

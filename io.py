import os
import random

def loadPictures(path):
    accepted_extensions = ['jpg', 'png', 'jpeg', 'gif']
    pictures = []

    for subdir, dir, files in os.walk(path):
        for file in files:
            try:
                if accepted_extensions.index(os.path.splitext(file)[1][1:].lower()) >= 0:
                    pictures.append(file)
            except ValueError:
                # Maybe make a global error-handling method that sends an email to me when encountered
                print "Error: 1"

    try:
        pictures = random.sample(pictures, 5)
    except ValueError:
        print "Error: 2"

    return pictures

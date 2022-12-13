import random
import math
import matplotlib.pyplot as plt
from random import randint
from samila import GenerativeImage
from samila import Projection
from datetime import datetime

DEBUG_MODE = True

def f1(x,y):
    result = random.uniform(-1,1) * x**randint(0,10) - math.tan(y**randint(0,5)) + math.cos(y-x)
    return result
    
def f2(x,y):
    result = random.uniform(-1,1) * y**randint(0,10) - math.cos(x**randint(0,5)) + math.cos(x)
    return result

def main():
    primary_colors = ['lime', 'white', 'blue', 'red', 'cyan']
    background_colors = ['black', 'white']
    for p_color in primary_colors:
        for b_color in background_colors:
            # Check to see they don't conflict
            if p_color != b_color:
                create_image(p_color, b_color)
                
# Generate and display image before then saving it into a file
def create_image(p_color, b_color):
    if DEBUG_MODE:
        print('Generating image for primary color {p_color} and background color {b_color}')
    
    g = GenerativeImage(f1,f2)
    g.generate()
    g.plot(color=p_color,bgcolor=b_color,projection=Projection.POLAR)
    save_output_file(g)
    plt.close()

    if DEBUG_MODE:
        print('Closed file')

# Takes either relative or absolute path as input
def save_output_file(g):
    dateTimeObj = datetime.now()
    filename = f'GENERATIVE-ART-TEST-{str(dateTimeObj)}.png'
    g.save_image(file_adr=filename, depth=5)

if __name__ == '__main__':
    main()

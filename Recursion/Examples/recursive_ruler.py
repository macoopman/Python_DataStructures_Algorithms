
"""
A English ruler pattern is a simple example of a "fractal"
ie.e a shape that has a self-recursive structure at various levels of magnification
"""

def draw_line(tick_length, tick_label = ''):
    """Draw one line with given tick length (followed by optional label)"""
    line = '-' * tick_length
    if tick_label:
        line += " " + tick_label
    print(line)


def draw_interval(center_length):
    """Draw tick interval based upon a central tick length"""
    if center_length > 0:                       # stop when length drops to 0
        draw_interval(center_length - 1)        # recursively draw top ticks
        draw_line(center_length)                #draw center tick
        draw_interval(center_length - 1)        # recursively draw bottom tick

def draw_ruler(num_inches, major_length):
    """Draw English ruler with given number of inches, major tick length"""
    draw_line(major_length, '0')                # draw inch 0 lines
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))




if __name__ == "__main__":
    draw_ruler(10, 5)

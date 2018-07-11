def setup():
    size(150,375)
    x=12.5
    while x<150:
        y=12.5
        while y<375:
            ellipse (x,y,25,25)
            y=y+25
        x=x+25

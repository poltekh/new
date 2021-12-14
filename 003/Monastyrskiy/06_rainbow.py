import simple_draw as sd
    
sd.resolution = (1200, 600)
    
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    

start_x = 50
start_y = 50
end_x = 350
end_y = 450
step_x = 5
step_y = 5
    
for i in range(7):
    start_x+=i*step_x
    start_y+=i*step_y
    end_x+=i*step_x
    end_y+=i*step_y
    sd.line(start_point=sd.get_point(start_x, start_y), end_point=sd.get_point(end_x, end_y), color=rainbow_colors[i], width=4)

sd.pause()
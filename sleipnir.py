import brickpi3
from time import sleep, strftime

BP = brickpi3.BrickPi3()

BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_COLOR_COLOR)
BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.EV3_COLOR_COLOR)
BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_COLOR_COLOR)
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_COLOR_COLOR)

color = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]

def move(pw1, pw2):
    BP.offset_motor_encoder(BP.PORT_C, BP.get_motor_encoder(BP.PORT_C))
    BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))
    BP.set_motor_power(BP.PORT_C, pw1)
    BP.set_motor_power(BP.PORT_B, pw2)

def status():
    print("[{}] S1: {} | S2: {} | S3: {} | S4: {} ".format(strftime('%H:%M:%S'),color[c1],color[c2],color[c3],color[c4]))

def v_left():
    while color[c3] == "Green":
        move(40,40)
    else:
        if color[c3] == "Black":
            move(-20,-20)
            sleep(0.4)
            if color[c2] == "Green":
                move(100,-100)
                sleep(2)
            else:
                move(40,40)
                sleep(0.4)
                while color[c2] == "White":
                    move(75,-55)
                else:
                    move(-55,75)
                    sleep(0.2)
                    move(-50,-50)
                    sleep(0.3)

def v_right():
    while color[c2] == "Green":
        move(40,40)
    else:
        if color[c2] == "Black":
            move(-20,-20)
            sleep(0.4)
            if color[c3] == "Green":
                move(100,-100)
                sleep(2)
            else:
                move(40,40)
                sleep(0.4)
                while color[c3] == "White":
                    move(-55,75)
                else:
                    move(75,-55)
                    sleep(0.2)
                    move(-50,-50)
                    sleep(0.3)

def ponta_esc():
    if color[c3] == "Black":
        move(70,70)
        sleep(0.2)
        move(80,-55)
        sleep(0.9)
        move(-50,-50)
        sleep(0.1)
    else:
        pass

def ponta_dir():
    if color[c2] == "Black":
        move(70,70)
        sleep(0.2)
        move(-55,80)
        sleep(0.9)
        move(-50,-50)
        sleep(0.1)
    else:
        pass

try:
    while True:
        try:
            c1 = BP.get_sensor(BP.PORT_1)
            c2 = BP.get_sensor(BP.PORT_2)
            c3 = BP.get_sensor(BP.PORT_3)
            c4 = BP.get_sensor(BP.PORT_4)

            if color[c3] == "Green":
                v_left()
            elif color[c2] == "Green":
                v_right()
            elif color[c4] == "Black":
                ponta_esc()        
            elif color[c1] == "Black":
                ponta_dir()
                
            elif color[c4] == "White":
                if color[c1] == "White":
                    if color[c3] == "Black":
                        if color[c2] == "White":
                            move(75,-55)
                            status()
                    elif color[c2] == "Black":
                        if color[c3] == "White":
                            move(-55,75)
                            status()
                    elif color[c2] == "White":
                        move(40,40)
                        status()

        except brickpi3.SensorError as error:
            print(error)
except KeyboardInterrupt:
	BP.reset_all()

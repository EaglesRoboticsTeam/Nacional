#Copyright (c) 2018 Eagles Robotics Team
#Código base https://github.com/EaglesRoboticsTeam/BrickPi3/blob/master/Software/Python/Examples/EV3-Color_Sensor_Color.py
import brickpi3
from time import sleep

BP = brickpi3.BrickPi3()

#Definindo os sensores de cor EV3
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_COLOR_COLOR)
BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.EV3_COLOR_COLOR)
BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_COLOR_COLOR)
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_COLOR_COLOR)

color = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]

#Função dos motores
def move(pw1, pw2):
    #18-19 Reseta os motores
    BP.offset_motor_encoder(BP.PORT_C, BP.get_motor_encoder(port1))
    BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(port2))
    #Inicia o movimento dos motores
    BP.set_motor_power(BP.PORT_C, pw1)
    BP.set_motor_power(BP.PORT_B, pw2)

#Loop do seguidor
try:
    while True:
        try:
            c1 = BP.get_sensor(BP.PORT_1)
            c2 = BP.get_sensor(BP.PORT_2)
            c3 = BP.get_sensor(BP.PORT_3)
            c4 = BP.get_sensor(BP.PORT_4)

            if color[c4] == "Black":
                if color[c1] == "Black":
                    move(-20,-20)
                    sleep(0.3)
                    if color[c3] == "Green":
                        if color[c2] == "Green":
                            move(100,-100)
                            sleep(0.8)
                        else:
                            move(10,10)
                            sleep(0.2)
                            move(-75,100)
                            sleep(0.4)
                    elif color[c2] == "Green":
                        if color[c3] == "Green":
                            move(-100,100)
                            sleep(0.8)
                        else:
                            move(10,10)
                            sleep(0.2)
                            move(100,-75)
                            sleep(0.4)
                elif color[c1] == "White":
                    move(-75, 100)
                    sleep(0.4)
            elif color[c4] == "White":
                if color[c1] == "White":
                    if color[c3] == "Black":
                        if color[c2] == "White":
                            move(-75,100)    
                    elif color[c2] == "Black":
                        if color[c3] == "White":
                            move(100,-75)
                    elif color[c2] == "White":
                        move(50,50)
                        #go
        except brickpi3.SensorError as error:
            print(error)
except KeyboardInterrupt:
    BP.reset_all()

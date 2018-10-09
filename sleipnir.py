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
def move(port1, pw1, port2, pw2):
    #18-19 Reseta os motores
    BP.offset_motor_encoder(port1, BP.get_motor_encoder(port1))
    BP.offset_motor_encoder(port2, BP.get_motor_encoder(port2))
    #Inicia o movimento dos motores
    BP.set_motor_power(port1, pw1)
    BP.set_motor_power(port2, pw2)

#Loop do seguidor
try:
    while True:
        try:
            c1 = BP.get_sensor(BP.PORT_1)
            c2 = BP.get_sensor(BP.PORT_2)
            c3 = BP.get_sensor(BP.PORT_3)
            c4 = BP.get_sensor(BP.PORT_4)

            #seguidor aqui
            
        except brickpi3.SensorError as error:
            print(error)
except KeyboardInterrupt:
    BP.reset_all()

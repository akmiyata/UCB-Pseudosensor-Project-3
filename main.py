from pseudoSensor import PseudoSensor

ps = PseudoSensor()

for i in range(30):

    h,t = ps.generate_values()

    print("i ",i)

    print("H ",h)

    print("T ",t)
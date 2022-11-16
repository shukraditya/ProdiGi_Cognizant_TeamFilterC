def checkings():

    #toxicity of gas

    toxicity_gas = float(input()) #check for toxicity of the gas/gases released
    toxicity_threshold = float(input()) #check for it against the standard value of toxicity allowed in workplace
    if toxicity_threshold<toxicity_gas :
        print("Toxic Gas levels detected")

    depth_corrode = float(input()) #take from ultrasound sensor to see how much pipe has been decayed

    #capvolume of pipes
    pressure_gas = float(input()) #value taken from sensor
    wall_thickness = float(input()) #entered data theoretical value of pipe's thickness in ideal condition at manufacturing
    diameter=float(input())#outer diameter theoretical value
    diameter = diameter - depth_corrode
    allowed_stress = float(input()) #theoretical value of allowed stress
    capacity = (2 * wall_thickness * allowed_stress / diameter)
    P=float(input())#takes pressure from detector inside the pipeline
    if P >= capacity:
        print("Pipe flow over capacity!")
        valveStop()
        rrt()
        volume_flow_rate = float(input())  # volume flow rate taken from sensor
        cross_section = 4 * 3.14 * ((diameter / 2) ** 2)
        total_v = volume_flow_rate * cross_section
        area = float(input()) #total workplace area
        radiusAffected(total_v,area)



def valveStop():
    #function to control valves and stop it immediately when needed


def rrt():
    #contacts rapid response team



def radiusAffected(total_vol,area):
    affected_radius = (total_vol / area)
    print("Affected radius: ", affected_radius)
    return
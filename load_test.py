import numpy as np
import pybullet as p
import pybullet_data as pd

if __name__ == '__main__':
    p.connect(p.GUI)
    p.setAdditionalSearchPath(pd.getDataPath())
    p.setGravity(0, 0, -9.8)

    p.loadURDF("plane.urdf")
    p.loadURDF("urdf/robot_base.urdf")

    while True:
        p.stepSimulation()
    
    p.disconnet()
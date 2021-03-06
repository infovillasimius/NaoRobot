# Choregraphe simplified export in Python.
from naoqi import ALProxy


def saluta():
    names = list()
    times = list()
    keys = list()

    names.append("RElbowRoll")
    times.append([0.16, 0.64, 1.16, 1.64, 2.16, 2.52, 2.88, 3.24, 3.6, 3.92, 4.32, 5.04, 5.72, 6.08])
    keys.append(
        [0.49274, 0.49274, 0.382227, 0.49274, 0.49274, 0.49274, 0.49274, 0.49274, 0.49274, 0.49274, 0.49274, 0.49274,
         0.49274, 0.49274])

    names.append("RElbowYaw")
    times.append([0.16, 0.64, 1.16, 1.64, 2.16, 2.52, 2.88, 3.24, 3.6, 3.92, 4.32, 5.04, 5.72, 6.08])
    keys.append(
        [1.32107, 1.32107, 0.891863, 1.32107, 1.32107, 1.32107, 1.32107, 1.32107, 1.32107, 1.32107, 1.32107, 1.32107,
         1.32107, 1.32107])

    names.append("RHand")
    times.append([0.16, 0.64, 1.16, 1.64, 2.16, 2.52, 2.88, 3.24, 3.6, 3.92, 4.32, 5.04, 5.72, 6.08])
    keys.append(
        [0.32867, 0.32867, 0.32867, 0.32867, 0.91, 0.08, 0.91, 0.08, 0.91, 0.08, 0.91, 0.32867, 0.32867, 0.32867])

    names.append("RShoulderPitch")
    times.append([0.16, 0.64, 1.16, 1.64, 2.16, 2.52, 2.88, 3.24, 3.6, 3.92, 4.32, 5.04, 5.72, 6.08])
    keys.append(
        [1.42593, 0.0349066, -0.998328, -0.92677, -0.92677, -0.92677, -0.92677, -0.92677, -0.92677, -0.92677, -0.92677,
         0.0349066, 1.42593, 1.5865])

    names.append("RShoulderRoll")
    times.append([0.16, 0.64, 1.16, 1.64, 2.16, 2.52, 2.88, 3.24, 3.6, 3.92, 4.32, 5.04, 5.72, 6.08])
    keys.append(
        [-0.212363, -0.212363, -0.212363, -0.212363, -0.212363, -0.212363, -0.212363, -0.212363, -0.212363, -0.212363,
         -0.212363, -0.212363, -0.212363, -0.212363])

    names.append("RWristYaw")
    times.append([0.16, 0.64, 1.16, 1.64, 2.16, 2.52, 2.88, 3.24, 3.6, 3.92, 4.32, 5.04, 5.72, 6.08])
    keys.append(
        [0.150796, 0.150796, -0.919789, -1.49575, -1.49575, -1.49575, -1.49575, -1.49575, -1.49575, -1.49575, -1.49575,
         0.150796, 0.150796, 0.150796])

    try:
        # uncomment the following line and modify the IP if you use this script outside Choregraphe.
        motion = ALProxy("ALMotion", '127.0.0.1', 9559)
        # motion = ALProxy("ALMotion")
        motion.angleInterpolation(names, keys, times, True)
    except BaseException as err:
        print(err)

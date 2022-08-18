import paddle
from ppgan.apps import EDVRPredictor, RealSRPredictor

sr = RealSRPredictor()
sr.run("0.png")

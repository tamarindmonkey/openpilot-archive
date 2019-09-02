#import time
from selfdrive.virtualZSS import virtualZSS_wrapper
virtualZSS_model = virtualZSS_wrapper.get_wrapper()
virtualZSS_model.init_model()

model_output = virtualZSS_model.run_model_time_series(
  [0.21865889699193874, -0.516, 0.21865889699193874, -0.5226666666666666, 0.21865889699193874, -0.5293333333333333,
   0.21865889699193874, -0.536, 0.21865889699193874, -0.5426666666666666, 0.21865889699193874, -0.5493333333333333,
   0.21865889699193874, -0.556, 0.21865889699193874, -0.5626666666666666, 0.21865889699193874, -0.5693333333333334,
   0.21865889699193874, -0.576, 0.21865889699193874, -0.5826666666666667, 0.21865889699193874, -0.5893333333333334,
   0.21720116545120918, -0.596, 0.21720116545120918, -0.6026666666666667, 0.21720116545120918, -0.6093333333333333,
   0.21574343391047962, -0.616, 0.2142857301736666, -0.6226666666666667, 0.21282799863293703, -0.6293333333333333,
   0.21137026709220746, -0.6126666666666667, 0.2099125355514779, -0.596])
print(model_output)  # should be 0.20353005581912836

model_output = virtualZSS_model.run_model_time_series(
 [0.45626823189695337, -0.03266666666666666, 0.45626823189695337, -0.03933333333333333, 0.45626823189695337,
  -0.046, 0.45626823189695337, -0.05266666666666667, 0.45626823189695337, -0.059333333333333335,
  0.45626823189695337, -0.066, 0.45626823189695337, -0.07266666666666667, 0.45626823189695337,
  -0.07933333333333334, 0.45626823189695337, -0.086, 0.45626823189695337, -0.09266666666666666,
  0.45626823189695337, -0.09933333333333333, 0.45626823189695337, -0.106, 0.45626823189695337,
  -0.11266666666666666, 0.45626823189695337, -0.11933333333333333, 0.45626823189695337, -0.126,
  0.45626823189695337, -0.13266666666666665, 0.45626823189695337, -0.13933333333333334, 0.45626823189695337,
  -0.146, 0.45626823189695337, -0.15266666666666667, 0.45626823189695337, -0.15933333333333333])
print(model_output)  # should be 0.45780474704052376
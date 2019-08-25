import time
from selfdrive.df import df_wrapper
df_model = df_wrapper.get_wrapper()
df_model.init_model()
'''start = time.time()
for i in range(30):
 model_output = df_model.run_model(0.8653078153514447,
  0.46805728618371273,
  0.46805728618371273,
  0.28780443294609244,
  0.01075646532123655)
print(time.time() - startl)'''

model_output = df_model.run_model_lstm([0.66120759, 0.60160361, 0.4734589, 0.66109962, 0.60152763,
                                        0.4734589, 0.66098024, 0.60142257, 0.47431507, 0.66115285,
                                        0.6015472, 0.47431507, 0.66120613, 0.60162137, 0.47431507,
                                        0.66138414, 0.60178517, 0.47517123, 0.66161236, 0.60191151,
                                        0.47517123, 0.66226744, 0.59967074, 0.4760274, 0.66209118,
                                        0.59677719, 0.4760274, 0.6626518, 0.59718986, 0.4760274,
                                        0.6630379, 0.59757923, 0.47688356, 0.66327461, 0.60063031,
                                        0.47688356, 0.66335815, 0.60070805, 0.47688356, 0.66337073,
                                        0.60071491, 0.47773973, 0.66350517, 0.60083323, 0.47773973,
                                        0.66341275, 0.60076807, 0.47773973, 0.66360651, 0.59811086,
                                        0.47859589, 0.66393597, 0.59840147, 0.47859589, 0.66391847,
                                        0.59838847, 0.47859589, 0.66417497, 0.59861117, 0.47945205])
print(model_output)

model_output = df_model.run_model_lstm([0.48460677, 0.41526619, 0.10616438, 0.48456568, 0.41242759,
                                        0.10616438, 0.48453273, 0.41520008, 0.10616438, 0.48458192,
                                        0.41524371, 0.10616438, 0.48456715, 0.41523071, 0.10616438,
                                        0.48449822, 0.41518575, 0.10616438, 0.48447029, 0.41514546,
                                        0.10616438, 0.48436578, 0.41505348, 0.10530822, 0.48417714,
                                        0.41491684, 0.10530822, 0.48410934, 0.41482778, 0.10530822,
                                        0.48404758, 0.41477343, 0.10445205, 0.48389939, 0.4146814,
                                        0.10445205, 0.48367219, 0.41446415, 0.10445205, 0.48356047,
                                        0.41433279, 0.10445205, 0.48358718, 0.4143702, 0.10359589,
                                        0.48353595, 0.41432314, 0.10359589, 0.48335969, 0.414168,
                                        0.10359589, 0.48326878, 0.41687811, 0.10359589, 0.48323744,
                                        0.41687198, 0.10359589, 0.48290627, 0.41661243, 0.10273973])
print(model_output)
'''model_output = df_model.run_model(.3, 0.0, .3, .5)
print(model_output)
model_output = df_model.run_model(.05, .3, .4, .6)
print(model_output)
model_output = df_model.run_model(.7, .85, .55, .5)
print(model_output)'''
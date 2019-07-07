import time
from selfdrive.df import df_wrapper
df_model = df_wrapper.get_wrapper()
df_model.init_model()
start = time.time()
'''for i in range(100):
 model_output = df_model.run_model(0.8653078153514447,
  0.46805728618371273,
  0.46805728618371273,
  0.28780443294609244,
  0.01075646532123655)
print(time.time() - start)'''
inputData = [[29.02843475,  0.35738668, 30.92068291, 30.125     ,  0.31128621],
       [29.03630066,  0.3340371 , 30.78650856, 30.3125    ,  0.25114855],
       [29.05969238,  0.34852916, 30.86508942, 30.4375    ,  0.22096501],
       [29.08823013,  0.3746638 , 30.90961266, 30.5       ,  0.20591198],
       [29.09097672,  0.33888161, 30.99625397, 30.5625    ,  0.21543841],
       [29.09221268,  0.30252632, 30.9882412 , 30.75      ,  0.21784231],
       [29.12673378,  0.35487568, 30.9612751 , 30.8125    ,  0.20899191],
       [29.14589691,  0.35100389, 30.9978447 , 30.875     ,  0.20923389],
       [29.13115692,  0.28425407, 31.00173378, 31.0625    ,  0.20755437],
       [29.15645599,  0.30152702, 30.9848156 , 31.125     ,  0.19839042],
       [29.1782608 ,  0.31595507, 30.97490692, 31.125     ,  0.18525605],
       [29.19071198,  0.30920807, 30.99983597, 31.25      ,  0.17901972],
       [29.19393539,  0.28792161, 31.0241642 , 31.375     ,  -0.17832559],
       [29.21792221,  0.30898744, 30.02958679, 31.5       ,  -0.27676196],
       [29.2363472 ,  0.31690341, 29.00643539, 31.5       ,  -0.36635223],
       [29.25361443,  0.31393164, 40.99917221, 31.5625    ,  -0.45341491],
       [28.26693535,  0.308523  , 40.9863472 , 31.75      ,  -0.53701306],
       [27.28693962,  0.31767616, 40.02942467, 40    ,  7.93398354],
       [26.30378342,  0.32041737, 40.04216194, 41.875     ,  6.13323745],
       [25.31727791,  0.31508622, 40.9133625 , 45.9375    ,  5]]
inputData = [j for i in inputData for j in i]
model_output = df_model.run_model(inputData)
print(model_output)

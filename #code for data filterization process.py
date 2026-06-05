#code for data filterization process


import pandas as pd
import os
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb
import scipy
rcParams ['figure.figsize'] =5, 4
sb.set_style('whitegrid')
file_names=["outside humidity", "wind speed outside", "outside temperature", "out side co2 concentration", "inside humidity", "inside temperature" ]
frames=[]
for name in file_names:
    #print(r"C:\Users\selam\Downloads"+"\\"+name+".csv")
    data=pd.read_csv(name+".csv")
    frames.append(data)
#merging frames
result=pd.concat(frames,axis=1,sort=False)
result.columns
#dropping nan values
result=result.dropna()
result.shape[24]
result[result['carbon dioxide concentration']=='percentage']
result[result['carbon dioxide concentration']!='percentage']
result[result['carbon dioxide concentration']!='percentage']
result=result[result['carbon dioxide concentration']!='percentage']
cols = result.columns
cols = cols.map(lambda x: x.replace(' ', '_'))
result.columns = cols
result.columns
#remove the data out of input parameter
result['carbon_dioxide_concentration']=result.carbon_dioxide_concentration.astype('int64')
result =result[result.carbon_dioxide_concentration<31000]
result =result[result.carbon_dioxide_concentration>-31000]
result
result['Outside_Humidity']=result.Outside_Humidity.astype('int64')
result =result[result.Outside_Humidity<99.9]
result =result[result.Outside_Humidity>30]
result
result['wind_speed_']=result.wind_speed_.astype('float64')
result =result[result.wind_speed_<16]
result =result[result.wind_speed_>0]
result
result['Outside_Temperature_']=result.Outside_Temperature_.astype('int64')
result =result[result.Outside_Temperature_<44]
result =result[result.Outside_Temperature_>12]
result
result['Inside_Humidity']=result.Inside_Humidity.astype('int64')
result =result[result.Inside_Humidity<100]
result =result[result.Inside_Humidity>59]
result
result['Inside_Temperature_']=result.Inside_Temperature_.astype('int64')
result =result[result.Inside_Temperature_<35]
result =result[result.Inside_Temperature_>12]
result
result
plt.xlabel('no of sample')
plt.ylabel('ins temp Sensor Values')
plt.plot(result.Inside_Temperature_)
plt.savefig('filter ins temp.png', transparent=False)
plt.xlabel('no of sample')
plt.ylabel('ins humi Sensor Values')
plt.plot(result.Inside_Humidity)
plt.savefig('filter ins humi.png', transparent=False)
plt.xlabel('no of sample')
plt.ylabel('wind speed Sensor Values')
plt.plot(result.wind_speed_)
plt.savefig('filter wind speed.png', transparent=False)
plt.xlabel('no of sample')
plt.ylabel('out temp Sensor Values')
plt.plot(result.Outside_Temperature_)
plt.savefig('filter out temp.png', transparent=False)
plt.xlabel('no of sample')
plt.ylabel('out humi Sensor Values')
plt.plot(result.Outside_Humidity)
plt.savefig('filter out humi.png', transparent=False)
plt.xlabel('no of sample')
plt.ylabel('co2 Sensor Values')
plt.plot(result.carbon_dioxide_concentration)
plt.savefig('filter co2.png', transparent=False)
result.to_csv(r"results.csv")



import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb
import scipy
import sklearn
from sklearn import preprocessing
from sklearn.preprocessing import scale
#% matplotlib  inline
rcParams ['figure.figsize'] =5, 4
sb.set_style('whitegrid')
#normalize and scaling the data using min max prescaling
normalized= pd.read_csv('results.csv')
normalized.columns=['Time_','Outside_Humidity','Time_','wind_speed_','Time_','Outside_Temperature_','Time_','carbon_dioxide_concentration','Time_','Inside_Humidity','Time_','Inside_Temperature_']
Outside_Humidity=normalized.Outside_Humidity
plt.plot(Outside_Humidity)
wind_speed_=normalized.wind_speed_
plt.plot(wind_speed_)
Outside_Temperature_=normalized.Outside_Temperature_
plt.plot(Outside_Temperature_)
carbon_dioxide_concentration=normalized.carbon_dioxide_concentration
plt.plot(carbon_dioxide_concentration)
Inside_Humidity=normalized.Inside_Humidity
plt.plot(Inside_Humidity)
Inside_Temperature_=normalized.Inside_Temperature_
plt.plot(Inside_Temperature_)
normalized[['Outside_Humidity']].describe()
normalized[['wind_speed_']].describe()
normalized[['Outside_Temperature_']].describe()
normalized[['carbon_dioxide_concentration']].describe()
normalized[['Inside_Humidity']].describe()
normalized[['Inside_Temperature_']].describe()
Outside_Humidity_matrix=Outside_Humidity.values.reshape(-1,1)
wind_speed__matrix=wind_speed_.values.reshape(-1,1)
Outside_Temperature__matrix=Outside_Temperature_.values.reshape(-1,1)
carbon_dioxide_concentration_matrix=carbon_dioxide_concentration.values.reshape(-1,1)
Inside_Humidity_matrix=Inside_Humidity.values.reshape(-1,1)
Inside_Temperature__matrix=Inside_Temperature_.values.reshape(-1,1)
scaled=preprocessing.MinMaxScaler()
scaled_Outside_Humidity=scaled.fit_transform(Outside_Humidity_matrix)
scaled_wind_speed_=scaled.fit_transform(wind_speed__matrix)
scaled_Outside_Temperature_=scaled.fit_transform(Outside_Temperature__matrix)
scaled_carbon_dioxide_concentration=scaled.fit_transform(carbon_dioxide_concentration_matrix)
scaled_Inside_Humidity=scaled.fit_transform(Inside_Humidity_matrix)
scaled_Inside_Temperature_=scaled.fit_transform(Inside_Temperature__matrix)
plt.plot(scaled_Outside_Humidity)
plt.plot(scaled_wind_speed_)
plt.plot(scaled_Outside_Temperature_)
plt.plot(scaled_carbon_dioxide_concentration)
plt.plot(scaled_Inside_Humidity)
plt.plot(scaled_Inside_Temperature_)
np.savetxt("scaled out humi.csv", np.array(scaled_Outside_Humidity), delimiter=",")
np.savetxt("scaled out temp.csv", np.array(scaled_Outside_Temperature_), delimiter=",")
np.savetxt("scaled out wind.csv", np.array(scaled_wind_speed_), delimiter=",")
np.savetxt("scaled out co2.csv", np.array(scaled_carbon_dioxide_concentration), delimiter=",")
np.savetxt("scaled ins humi.csv", np.array(scaled_Inside_Humidity), delimiter=",")
np.savetxt("scaled ins temp.csv", np.array(scaled_Inside_Temperature_), delimiter=",")
scaled_Inside_Temperature_
scaled_Inside_Humidity
scaled_Outside_Humidity
scaled_wind_speed_
scaled_Outside_Temperature_
scaled_carbon_dioxide_concentration
Outside_Humidity_matrix=Outside_Humidity.values.reshape(-1,1)
scaled=preprocessing.MinMaxScaler(feature_range=(0,1))
scaledOutside_Humidity=scaled.fit_transform(Outside_Humidity_matrix)
plt.plot(scaledOutside_Humidity)
scaledOutside_Humidity
np.savetxt("scaled out humi feature.csv", np.array(scaledOutside_Humidity), delimiter=",")
plt.xlabel('no of sample')
plt.ylabel('scaled out humi Sensor Values')
plt.plot(scaledOutside_Humidity)
plt.savefig('scale_Outside_Humidity.png', transparent=True, bbox_inches='tight')
plt.savefig('scale_Outside_Humidity1.png', transparent=False)
wind_speed__matrix=wind_speed_.values.reshape(-1,1)
scaled=preprocessing.MinMaxScaler(feature_range=(0,1))
scaledwind_speed=scaled.fit_transform(wind_speed__matrix)
plt.plot(scaledwind_speed)
scaledwind_speed
np.savetxt("scaled wind speed feature.csv", np.array(scaledOutside_Humidity), delimiter=",")
plt.xlabel('no of sample')
plt.ylabel('scaled wind speed Sensor Values')
plt.plot(scaledwind_speed)
plt.savefig('scale_wind_speed.png', transparent=True, bbox_inches='tight')
plt.savefig('scale_wind_speed1.png', transparent=False)
Outside_Temperature__matrix=Outside_Temperature_.values.reshape(-1,1)
scaled=preprocessing.MinMaxScaler(feature_range=(0,1))
scaledOutside_Temperature=scaled.fit_transform(Outside_Temperature__matrix)
plt.plot(scaledOutside_Temperature)
scaledOutside_Temperature
np.savetxt("scaled out temp feature.csv", np.array(scaledOutside_Temperature), delimiter=",")
plt.xlabel('no of sample')
plt.ylabel('scaled out temp Sensor Values')
plt.plot(scaledOutside_Temperature)
plt.savefig('scale_Outside_Temperature.png', transparent=True, bbox_inches='tight')
plt.savefig('scale_Outside_Temperature1.png', transparent=False)
carbon_dioxide_concentration_matrix=carbon_dioxide_concentration.values.reshape(-1,1)
scaled=preprocessing.MinMaxScaler(feature_range=(0,1))
scaledcarbon_dioxide_concentration=scaled.fit_transform(carbon_dioxide_concentration_matrix)
plt.plot(scaledcarbon_dioxide_concentration)
scaledcarbon_dioxide_concentration
np.savetxt("scaled co2 feature.csv", np.array(scaledcarbon_dioxide_concentration), delimiter=",")
plt.xlabel('no of sample')
plt.ylabel('scaled co2 Sensor Values')
plt.plot(scaledcarbon_dioxide_concentration)
plt.savefig('scale_carbon_dioxide_concentration.png', transparent=True, bbox_inches='tight')
plt.savefig('scale_carbon_dioxide_concentration1.png', transparent=False)
Inside_Humidity_matrix=Inside_Humidity.values.reshape(-1,1)
scaled=preprocessing.MinMaxScaler(feature_range=(0,1))
scaledInside_Humidity=scaled.fit_transform(Inside_Humidity_matrix)
plt.plot(scaledInside_Humidity)
scaledInside_Humidity
np.savetxt("scaled ins humi feature.csv", np.array(scaledInside_Humidity), delimiter=",")
plt.xlabel('no of sample')
plt.ylabel('scaled ins humi Sensor Values')
plt.plot(scaledInside_Humidity)
plt.savefig('scale_Inside_Humidity.png', transparent=True, bbox_inches='tight')
plt.savefig('scale_Inside_Humidity1.png', transparent=False)
Inside_Temperature__matrix=Inside_Temperature_.values.reshape(-1,1)
scaled=preprocessing.MinMaxScaler(feature_range=(0,1))
scaledOutInside_Temperature_=scaled.fit_transform(Inside_Temperature__matrix)
plt.plot(scaledOutInside_Temperature_)
scaledOutInside_Temperature_
np.savetxt("scaled ins temp feature.csv", np.array(scaledOutInside_Temperature_), delimiter=",")
plt.xlabel('no of sample')
plt.ylabel('scaled in temp Sensor Values')
plt.plot(scaledOutInside_Temperature_)
plt.savefig('scale_Inside_Temperature.png', transparent=True, bbox_inches='tight')
plt.savefig('scale_Inside_Temperature1.png', transparent=False)
#standardized step
standardized_Outside_Humidity=scale(Outside_Humidity, axis= 0, with_mean=False, with_std=False)
plt.plot(standardized_Outside_Humidity)
standardized_wind_speed_=scale(wind_speed_, axis= 0, with_mean=False, with_std=False)
plt.plot(standardized_wind_speed_)
standardized_Outside_Temperature_=scale(Outside_Temperature_, axis= 0, with_mean=False, with_std=False)
plt.plot(standardized_Outside_Temperature_)
standardized_carbon_dioxide_concentration=scale(carbon_dioxide_concentration, axis= 0, with_mean=False, with_std=False)
plt.plot(standardized_carbon_dioxide_concentration)
standardized_Inside_Humidity=scale(Inside_Humidity, axis= 0, with_mean=False, with_std=False)
plt.plot(standardized_Inside_Humidity)
standardized_Inside_Temperature_=scale(Inside_Temperature_, axis= 0, with_mean=False, with_std=False)
plt.plot(standardized_Inside_Temperature_)
standardized_Inside_Temperature_=scale(Inside_Temperature_)
plt.xlabel('no of sample')
plt.ylabel('standardized ins temp Sensor Values')
plt.plot(standardized_Inside_Temperature_)
plt.savefig('stand_Inside_Temperature_.png', transparent=True, bbox_inches='tight')
plt.savefig('stand_Inside_Temperature_1.png', transparent=False)
np.savetxt("stan Inside_Temperature_.csv", np.array(standardized_Inside_Temperature_), delimiter=",")
standardized_Inside_Humidity=scale(Inside_Humidity)
plt.xlabel('no of sample')
plt.ylabel('standardized ins humi Sensor Values')
plt.plot(standardized_Inside_Humidity)
plt.savefig('stand_Inside_Humidity.png', transparent=True, bbox_inches='tight')
plt.savefig('stand_Inside_Humidity1.png', transparent=False)
np.savetxt("stan Inside_Humidity.csv", np.array(standardized_Inside_Humidity), delimiter=",")
standardized_carbon_dioxide_concentration=scale(carbon_dioxide_concentration)
plt.xlabel('no of sample')
plt.ylabel('standardized co2 Sensor Values')
plt.plot(standardized_carbon_dioxide_concentration)
plt.savefig('stand_carbon_dioxide_concentration.png', transparent=True, bbox_inches='tight')
plt.savefig('stand_carbon_dioxide_concentration1.png', transparent=False)
np.savetxt("stan carbon_dioxide_concentration.csv", np.array(standardized_carbon_dioxide_concentration), delimiter=",")
standardized_Outside_Temperature_=scale(Outside_Temperature_)
plt.xlabel('no of sample')
plt.ylabel('standardized out temp Sensor Values')
plt.plot(standardized_Outside_Temperature_)
plt.savefig('stand_Outside_Temperature_.png', transparent=True, bbox_inches='tight')
plt.savefig('stand_Outside_Temperature_1.png', transparent=False)
np.savetxt("stan Outside_Temperature_.csv", np.array(standardized_Outside_Temperature_), delimiter=",")
standardized_wind_speed_=scale(wind_speed_)
plt.xlabel('no of sample')
plt.ylabel('standardized wind speed Sensor Values')
plt.plot(standardized_wind_speed_)
plt.savefig('stand_Inside_Temperature_.png', transparent=True, bbox_inches='tight')
plt.savefig('stand_Inside_Temperature_1.png', transparent=False)
np.savetxt("stan wind_speed_.csv", np.array(standardized_wind_speed_), delimiter=",")
standardized_Outside_Humidity=scale(Outside_Humidity)
plt.xlabel('no of sample')
plt.ylabel('standardized out humi Sensor Values')
plt.plot(standardized_Outside_Humidity)
plt.savefig('stand_Outside_Humidity.png', transparent=True, bbox_inches='tight')
plt.savefig('stand_Outside_Humidity1.png', transparent=False)
np.savetxt("stan Outside_Humidity.csv", np.array(standardized_Outside_Humidity), delimiter=",")

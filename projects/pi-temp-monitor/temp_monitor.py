import os
import time

def get_temperature():
    temp = os.popen("vcgencmd measure_temp").readline()
    return float(temp.replace("temp=", "").replace("'C\n", ""))

while True:
    temp = get_temperature()
    print(f"Current Temperature: {temp}°C")
    
    if temp > 70:  # Seuil à ajuster
        print("⚠️ Warning! Temperature is too high!")

    time.sleep(60)  # Verif 1 min d'intervalle 

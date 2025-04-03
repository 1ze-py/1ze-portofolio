import time

def read_temp():
    """Reads the CPU temperature on a Raspberry Pi."""
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
            temp = int(file.read()) / 1000  
        return temp
    except FileNotFoundError:
        print("Error: Temperature file not found. Are you running this on a Raspberry Pi?")
        return None

while True:
    temperature = read_temp()
    if temperature is not None:
        print(f"🌡️ CPU Temperature: {temperature:.2f}°C")
        
        
        if temperature >= 80:
            print("⚠️ WARNING: High Temperature! Consider cooling solutions.")
    
    time.sleep(60)  

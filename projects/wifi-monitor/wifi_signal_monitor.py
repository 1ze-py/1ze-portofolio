import subprocess
import time

def get_wifi_signal():
    try:
        result = subprocess.check_output(["iwconfig"], universal_newlines=True)
        for line in result.split("\n"):
            if "Signal level" in line:
                signal_level = int(line.split("Signal level=")[1].split(" dBm")[0])
                return signal_level
    except Exception as e:
        print(f"Error: {e}")
    return None

while True:
    signal = get_wifi_signal()
    if signal is not None:
        print(f"📶 Wi-Fi Signal Strength: {signal} dBm")
        if signal < -70:
            print("⚠️ Warning! Weak Wi-Fi signal detected!")
    else:
        print("❌ Could not retrieve Wi-Fi signal strength.")
    
    time.sleep(120)  # Vérif 1 min 

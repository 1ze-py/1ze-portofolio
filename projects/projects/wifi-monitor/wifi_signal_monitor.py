import subprocess
import time
import re

def get_wifi_signal_strength():
    """Returns the Wi-Fi signal strength as a percentage (0-100)."""
    try:
        
        result = subprocess.run(["iwconfig", "wlan0"], capture_output=True, text=True)
        output = result.stdout

       
        match = re.search(r"Signal level=(-?\d+) dBm", output)
        if match:
            signal_dbm = int(match.group(1))

            
            if signal_dbm <= -100:
                return 0
            elif signal_dbm >= -50:
                return 100
            else:
                return 2 * (signal_dbm + 100)
        
        return None
    except Exception as e:
        print(f"Error getting Wi-Fi signal: {e}")
        return None

while True:
    strength = get_wifi_signal_strength()
    if strength is not None:
        print(f"📡 Wi-Fi Signal Strength: {strength:.0f}%")
        
       
        if strength < 30:
            print("⚠️ WARNING: Weak Wi-Fi signal detected!")
    
    time.sleep(60)  

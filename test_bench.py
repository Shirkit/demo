# This file should be ran by the client that would send a MQTT message to the server, ie: a raspberry that's a MQTT client

import paho.mqtt.client as mqtt
import json
import time

# --- CONFIGURATION ---
MQTT_BROKER = "wiser" # Change to your server's IP
STUDENT_NAME = "USUARIO" # Change to your username
# ---------------------

client = mqtt.Client()
client.connect(MQTT_BROKER, 1883, 60)

def send_test_data():
    # 1. Simple JSON
    simple_data = {"temp": 28.5, "hum": 45.2}
    client.publish(f"research/{STUDENT_NAME}/simple", json.dumps(simple_data))
    print(f"Sent Simple JSON to research/{STUDENT_NAME}/simple")

    # 2. Nested JSON
    nested_data = {
        "sensor_id": "orchid_01",
        "data": {"average_temperature": 31.2, "std_dev": 0.4}
    }
    client.publish(f"research/{STUDENT_NAME}/nested", json.dumps(nested_data))
    print(f"Sent Nested JSON to research/{STUDENT_NAME}/nested")

    # 3. Weather CSV
    # Format: timestamp,avg_temp,avg_hum,temp_std,hum_std,t_low,t_up,h_low,h_up
    timestamp = int(time.time())
    csv_data = f"{timestamp},30.0,90.5,0.1,0.2,29.9,30.1,90.3,90.7"
    client.publish(f"research/{STUDENT_NAME}/weather_csv", csv_data)
    print(f"Sent CSV to research/{STUDENT_NAME}/weather_csv")

if __name__ == "__main__":
    send_test_data()
    client.disconnect()

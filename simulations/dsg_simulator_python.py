# simulations/dsg_simulator_python.py
import pandas as pd
import numpy as np
import os

def generate_dsg_simulation_data():
    """DSG simülasyon verisi oluştur"""
    print("🚗 DSG Simülasyon Verisi Oluşturuluyor...")
    
    np.random.seed(42)  # Tekrarlanabilirlik için
    num_samples = 1000
    
    # Temel parametreler
    time = np.arange(num_samples)
    vehicle_speed = np.zeros(num_samples)
    engine_rpm = np.zeros(num_samples)
    throttle_position = np.zeros(num_samples)
    current_gear = np.ones(num_samples, dtype=int)
    clutch_temperature = np.zeros(num_samples)
    transmission_fluid_temp = np.zeros(num_samples)
    
    # Simülasyon
    for i in range(1, num_samples):
        # Araç hızı (km/h) - rastgele artış/azalış
        speed_change = np.random.normal(0, 2)
        vehicle_speed[i] = max(0, vehicle_speed[i-1] + speed_change)
        
        # Gaz pozisyonu (%)
        throttle_position[i] = max(0, min(100, throttle_position[i-1] + np.random.normal(0, 5)))
        
        # Motor RPM - hız ve gaz ile ilişkili
        engine_rpm[i] = vehicle_speed[i] * 80 + throttle_position[i] * 10 + np.random.normal(0, 100)
        engine_rpm[i] = max(500, min(7000, engine_rpm[i]))
        
        # Vites değişim mantığı
        if vehicle_speed[i] < 20:
            current_gear[i] = 1
        elif vehicle_speed[i] < 40:
            current_gear[i] = 2
        elif vehicle_speed[i] < 60:
            current_gear[i] = 3
        elif vehicle_speed[i] < 80:
            current_gear[i] = 4
        else:
            current_gear[i] = 5
        
        # Sıcaklık artışı
        clutch_heat = abs(throttle_position[i] * 0.1) + abs(vehicle_speed[i] * 0.05)
        clutch_temperature[i] = max(20, min(120, clutch_temperature[i-1] + clutch_heat - 0.5))
        
        fluid_heat = vehicle_speed[i] * 0.02 + engine_rpm[i] * 0.001
        transmission_fluid_temp[i] = max(20, min(100, transmission_fluid_temp[i-1] + fluid_heat - 0.3))
    
    # Veri çerçevesi oluştur
    data = pd.DataFrame({
        'timestamp': time,
        'vehicle_speed': vehicle_speed,
        'engine_rpm': engine_rpm,
        'throttle': throttle_position,
        'gear': current_gear,
        'clutch_temp': clutch_temperature,
        'fluid_temp': transmission_fluid_temp
    })
    
    # data klasörüne kaydet
    os.makedirs('../data', exist_ok=True)
    data.to_csv('../data/simulation_data.csv', index=False)
    print(f"✅ Simülasyon verisi oluşturuldu: {len(data)} kayıt")
    print("\n📊 İlk 5 kayıt:")
    print(data.head())
    
    return data

if __name__ == "__main__":
    generate_dsg_simulation_data()
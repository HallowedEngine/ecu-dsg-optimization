// simulations/dsg_simulator.c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct {
    double vehicle_speed;
    double engine_rpm;
    double throttle_position;
    int current_gear;
    double clutch_temperature;
    double transmission_fluid_temp;
} DSG_Data;

void simulate_gear_shift(DSG_Data* data) {
    // Basit vites değişim mantığı
    if (data->vehicle_speed < 20) data->current_gear = 1;
    else if (data->vehicle_speed < 40) data->current_gear = 2;
    else if (data->vehicle_speed < 60) data->current_gear = 3;
    else data->current_gear = 4;
    
    // Sıcaklık artışı simülasyonu
    data->clutch_temperature += fabs(data->throttle_position * 0.5);
    data->transmission_fluid_temp += data->vehicle_speed * 0.01;
}

void generate_simulation_data(const char* filename, int num_samples) {
    FILE* file = fopen(filename, "w");
    fprintf(file, "timestamp,vehicle_speed,engine_rpm,throttle,gear,clutch_temp,fluid_temp\n");
    
    DSG_Data data = {0};
    
    for (int i = 0; i < num_samples; i++) {
        data.vehicle_speed = 10 + (i % 100);
        data.engine_rpm = data.vehicle_speed * 80 + (rand() % 500);
        data.throttle_position = 0.3 + (sin(i * 0.1) * 0.3);
        
        simulate_gear_shift(&data);
        
        fprintf(file, "%d,%.2f,%.2f,%.2f,%d,%.2f,%.2f\n",
                i, data.vehicle_speed, data.engine_rpm, 
                data.throttle_position, data.current_gear,
                data.clutch_temperature, data.transmission_fluid_temp);
    }
    
    fclose(file);
}

int main() {
    generate_simulation_data("simulation_data.csv", 1000);
    printf("Simülasyon verisi oluşturuldu: simulation_data.csv\n");
    return 0;
}
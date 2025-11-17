# src/data_analysis/analyzer.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

class DSGAnalyzer:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.anomalies = None
        
    def exploratory_analysis(self):
        """Keşifsel veri analizi"""
        print("=== DSG SİMÜLASYON VERİ ANALİZİ ===")
        print(f"Toplam kayıt: {len(self.data)}")
        print("\nİstatistikler:")
        print(self.data.describe())
        
        # Korelasyon matrisi
        plt.figure(figsize=(10, 8))
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        correlation_matrix = self.data[numeric_cols].corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
        plt.title('DSG Parametreleri Korelasyon Matrisi')
        plt.tight_layout()
        plt.savefig('correlation_matrix.png')
        plt.close()
        
    def detect_anomalies(self, contamination=0.1):
        """Anomali tespiti"""
        features = ['vehicle_speed', 'engine_rpm', 'throttle', 'clutch_temp', 'fluid_temp']
        X = self.data[features]
        
        # Standardizasyon
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        # Anomali tespiti
        iso_forest = IsolationForest(contamination=contamination, random_state=42)
        anomalies = iso_forest.fit_predict(X_scaled)
        
        self.data['anomaly'] = anomalies
        self.data['anomaly'] = self.data['anomaly'].map({1: 0, -1: 1})  # 1: anomali, 0: normal
        
        anomaly_count = self.data['anomaly'].sum()
        print(f"Tespit edilen anomali sayısı: {anomaly_count} ({anomaly_count/len(self.data)*100:.2f}%)")
        
        return self.data
    
    def visualize_anomalies(self):
        """Anomalileri görselleştir"""
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # 1. Hız - RPM dağılımı
        normal_data = self.data[self.data['anomaly'] == 0]
        anomaly_data = self.data[self.data['anomaly'] == 1]
        
        axes[0,0].scatter(normal_data['vehicle_speed'], normal_data['engine_rpm'], 
                         c='blue', alpha=0.6, label='Normal', s=10)
        axes[0,0].scatter(anomaly_data['vehicle_speed'], anomaly_data['engine_rpm'], 
                         c='red', alpha=0.8, label='Anomali', s=20)
        axes[0,0].set_xlabel('Araç Hızı')
        axes[0,0].set_ylabel('Motor RPM')
        axes[0,0].legend()
        axes[0,0].set_title('Hız - RPM Dağılımı')
        
        # 2. Debriyaj sıcaklığı zaman serisi
        axes[0,1].plot(self.data['timestamp'], self.data['clutch_temp'], 'b-', alpha=0.7, label='Sıcaklık')
        axes[0,1].scatter(anomaly_data['timestamp'], anomaly_data['clutch_temp'], 
                         c='red', s=30, label='Anomali')
        axes[0,1].set_xlabel('Zaman')
        axes[0,1].set_ylabel('Debriyaj Sıcaklığı')
        axes[0,1].legend()
        axes[0,1].set_title('Debriyaj Sıcaklığı Zaman Serisi')
        
        # 3. Vites dağılımı
        gear_anomalies = self.data.groupby('gear')['anomaly'].mean()
        axes[1,0].bar(gear_anomalies.index, gear_anomalies.values * 100, color='orange')
        axes[1,0].set_xlabel('Vites')
        axes[1,0].set_ylabel('Anomali Yüzdesi (%)')
        axes[1,0].set_title('Viteslere Göre Anomali Dağılımı')
        
        # 4. Anomali özeti
        anomaly_features = self.data[self.data['anomaly'] == 1][['vehicle_speed', 'engine_rpm', 'clutch_temp']].mean()
        normal_features = self.data[self.data['anomaly'] == 0][['vehicle_speed', 'engine_rpm', 'clutch_temp']].mean()
        
        comparison = pd.DataFrame({'Normal': normal_features, 'Anomali': anomaly_features})
        comparison.plot(kind='bar', ax=axes[1,1])
        axes[1,1].set_title('Normal vs Anomali Parametre Karşılaştırması')
        axes[1,1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('anomaly_analysis.png', dpi=300, bbox_inches='tight')
        plt.close()

if __name__ == "__main__":
    # Analizi çalıştır
    analyzer = DSGAnalyzer('simulation_data.csv')
    analyzer.exploratory_analysis()
    analyzer.detect_anomalies()
    analyzer.visualize_anomalies()
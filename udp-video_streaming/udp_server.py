# import socket
# import time
# import json
# import random
# import keyboard

# def generate_fake_data():
#     """Sahte veri üretimi için bir fonksiyon."""
#     fake_data = {
#         "id": random.randint(1, 100),
#         "rastgeleHavaSicakligi": round(random.uniform(15.0, 30.0), 2),  # Rastgele sıcaklık
#         "rastgeleNemOrani": round(random.uniform(30.0, 70.0), 2),    # Rastgele nem oranı
#         "telemetriVerisi":time.strftime("%Y-%m-%d %H:%M:%S.%f")[-3], # Zaman döngüsü
        
#     } 
#     return fake_data

# def start_server():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     server_address = ('localhost', 55445)
#     server_socket.bind(server_address)

#     print("Sunucu çalışıyor, sahte veri üretiyor...")

#     try:
#         while True:
#             # Sahte veriyi üret
#             fake_data = generate_fake_data()

#             # Gelen istemci isteqğini bekle
#             print("İstemciden veri bekleniyor...")

#             if keyboard.is_pressed('a'):
#                 print("Sunucu Kapatılıyor...")
#                 break
#             data, client_address = server_socket.recvfrom(4096)

#             if data:
#                 print(f"İstemciden gelen: {data.decode()} - Gönderen: {client_address}")

#                 # Veriyi JSON formatında gönder
#                 server_socket.sendto(json.dumps(fake_data).encode('utf-8'), client_address)
#                 print(f"Gönderilen veri: {fake_data}")

#             # İstekler arasında bir süre beklemek için (isteğe bağlı)
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print("\nSunucu kapatılıyor...")
#     finally:
#         server_socket.close()

# if __name__ == "__main__":
#     start_server()

import time
import socket
import json
import random
import keyboard
from datetime import datetime  # datetime modülü saliseler için

def generate_fake_data():
    """Sahte veri üretimi için bir fonksiyon."""
    fake_data = {
        "id": random.randint(1, 100),
        "rastgeleHavaSicakligi": round(random.uniform(15.0, 30.0), 2),  # Rastgele sıcaklık
        "rastgeleNemOrani": round(random.uniform(30.0, 70.0), 2),      # Rastgele nem oranı
        #"telemetriVerisi": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3],  # Milisaniye eklenmiş zaman
        "takim_numarasi": 1,
        "iha_enlem": 41.508775,
        "iha_boylam": 36.118335,
        "iha_irtifa": 38,
        "iha_dikilme": 7,
        "iha_yonelme": 210,
        "iha_yatis": -30,
        "iha_hiz": 28,
        "iha_batarya": 50,
        "iha_otonom": 1,
        "iha_kilitlenme": 1,
        "hedef_merkez_X": 300,
        "hedef_merkez_Y": 230,
        "hedef_genislik": 30,
        "hedef_yukseklik":43,
        "gps_saati": {
        "saat": 11,
        "dakika": 38,
        "saniye": 37,
        "milisaniye": 654
        }
    }
    return fake_data

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 55445)  # Sunucu adresi ve portu
    server_socket.bind(server_address)

    print("Sunucu çalışıyor, sahte veri üretiyor...")

    try:
        while True:
            # Sahte veriyi üret
            fake_data = generate_fake_data()

            # Gelen istemci isteğini bekle
            print("İstemciden veri bekleniyor...")
            
            if keyboard.is_pressed('a'):  # Klavyeden 'a' tuşuna basılırsa sunucuyu kapat
                print("Sunucu Kapatılıyor...")
                break

            data, client_address = server_socket.recvfrom(4096)  # İstemciden veri al
            if data:
                print(f"İstemciden gelen: {data.decode()} - Gönderen: {client_address}")

                # Veriyi JSON formatında gönder
                server_socket.sendto(json.dumps(fake_data).encode('utf-8'), client_address)
                print(f"Gönderilen veri: {fake_data}")

            # İstekler arasında bir süre beklemek için (isteğe bağlı)
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("\nSunucu kapatılıyor...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()

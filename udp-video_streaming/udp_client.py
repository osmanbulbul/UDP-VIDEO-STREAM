import socket
import json
import keyboard

def request_data_from_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 55445)

    try:
        while True:
            # Sunucuya istek gönder
            message = "Sahte veri talebi"
            if keyboard.is_pressed('a'):
                print("İstemci Kapatıldı.")
                break
            client_socket.sendto(message.encode('utf-8'), server_address)

            # Sunucudan veri al
            data, _ = client_socket.recvfrom(4096)

            # Veriyi JSON formatında çöz ve yazdır
            fake_data = json.loads(data.decode('utf-8'))
            print(f"Sunucudan gelen sahte veri: {fake_data}")

    except KeyboardInterrupt:
        print("\nİstemci kapatılıyor...")
    finally:
        client_socket.close()

if __name__ == "__main__":
    request_data_from_server()

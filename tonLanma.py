import requests
import time

def send_post_request(address):
    url = "https://lama-backend-qd2o.onrender.com/user/freespin"
    payload = {"address": address}
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("POST request sent successfully")
        else:
            print(f"Failed to send POST request. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    while True:
        address = input("Masukkan alamat: ")
        send_post_request(address)
        time.sleep(61)

if __name__ == "__main__":
    main()
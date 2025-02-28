import requests

url = "http://192.168.45.54:35729"  # ໃຊ້ HTTP ຊັດເຈນ

try:
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        print("ລະບົບປົກກະຕິ!")
    elif response.status_code == 404:
        print("ເຊື່ອມຕໍ່ໄດ້ແຕ່ບໍ່ພົບຫນ້າ (404) - ກວດ URL ຫຼື Route ໃນ Django")
    else:
        print(f"ບັນຫາ! Status: {response.status_code}")
except Exception as e:
    print(f"ເຊື່ອມຕໍ່ບໍ່ໄດ້: {e}")
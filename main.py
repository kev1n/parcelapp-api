import requests

def parceladd(token, description, trknumber, courier):

    headers = {"cookie": "token={}; language=en".format(token), "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36", "content-type": "application/x-www-form-urlencoded"}

    data = "name={}&number={}&courier={}&postcode=&lang=en".format(description, trknumber, courier)

    r = requests.post("https://web.parcelapp.net/add-ajax.php", headers=headers, data=data)

    return r.text

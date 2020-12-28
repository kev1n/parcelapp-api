import requests
import json
from rich.console import Console
from rich.table import Table

class Parcel:
  def __init__(self, token):
    self.token = token
    self.headers = {"cookie": f"token={self.token}; language=en", "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36", "content-type": "application/x-www-form-urlencoded"}

  def parceladd(self, description, trknumber, courier):
      data = f"name={description}&number={trknumber}&courier={courier}&postcode=&lang=en"

      r = requests.post("https://web.parcelapp.net/add-ajax.php", headers=self.headers, data=data)

      return r.text

  def parcelrm(self, trknumber, courier):
      data = f"number={trknumber}&type={courier}"

      r = requests.post("https://web.parcelapp.net/delete-ajax.php", headers=self.headers, data=data)

      return r.text

  def parcellist(self, url):
      parcels = requests.get(url, headers=self.headers)

      parcels = json.loads(parcels.text.split("(", 1)[1][:-1])

      parcels = parcels[0]
      
      table = Table(title="Parcels")
      table.add_column("ID", justify="left", style="", no_wrap=True)
      table.add_column("Estimated Delivery Date", justify="left", style="", no_wrap=True)
      table.add_column("Parcel Name", justify="left", style="", no_wrap=True)
      table.add_column("Tracking Number", justify="left", style="", no_wrap=True)
      table.add_column("Status", justify="left", style="", no_wrap=False)

      i = 1

      for parcel in parcels:
          if parcel[5] == "":
              if "delivered" in parcel[4][0][0].lower():
                  parcel[5] = "Delivered"
              else:
                  parcel[5] = "No estimated date"
          else:
              parcel[5] = parcel[5].split(" ")[0]

          table.add_row(str(i), parcel[5], parcel[1], parcel[0], parcel[4][0][0])
          i += 1

      return table

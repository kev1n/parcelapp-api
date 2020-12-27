# parcelapp-api

This is an unofficial python API for interacting with the [Parcel app](https://parcelapp.net/). This API currently supports adding, removing, and listing parcels.

### Setup

Add [parcelapp-api.py](https://raw.githubusercontent.com/rynlu/parcelapp-api/main/parcelapp-api.py) to your package directory and import functions with the following line:

```python
from parcelapp-api import parceladd, parcelrm, parcellist
```

### Usage

```python
print(parceladd("TOKEN", "DESCRIPTION", "TRKNUMBER", "CARRIER CODE"))
> ADDED
```

```python
print(parcelrm("TOKEN", "TRKNUMBER", "CARRIER CODE"))
> SUCCESS
```

```python
parcellist("TOKEN", "REQUEST URL")
```

### Obtaining Token, Request URL, and Carrier Codes 
Your token can be found in your [web dashboard](https://web.parcelapp.net/) cookies:

![token_guide](https://cdn.discordapp.com/attachments/480736870540771329/790386685787504690/unknown.png)

Your request URL can be found through your Network tab of DevTools. Open the Network tab and then visit the [web dashboard](https://web.parcelapp.net/) on your browser. Look for a request with the name of `data.php?...` and click on it to get the Request URL. 

![request_url_guide](https://media.discordapp.net/attachments/480736870540771329/792793847712972840/unknown.png)

The carrier codes for USPS, UPS, and FedEx are `usps`, `ups`, and `fedex` respectively. Additional carrier codes can be found [here](https://ryanlau.dev/carriercodes).

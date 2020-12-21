# parcelapp-api

This is an unofficial python API for adding parcels to [Parcel](https://parcelapp.net/). More features may be added in the future.

#### Setup

Add [parceladd.py](https://raw.githubusercontent.com/rynlu/parcelapp-api/main/parceladd.py) to your package directory and import `parceladd()` with the following line:

```python
from parceladd import parceladd
```

Call the function within your code like so:

```python
print(parceladd("TOKEN", "DESCRIPTION", "TRKNUMBER", "CARRIER"))
> ADDED
```

Your token can be found in your [web dashboard](https://web.parcelapp.net/) cookies:

![image-20201220201439439](https://cdn.discordapp.com/attachments/480736870540771329/790386685787504690/unknown.png)

The carrier codes for USPS, UPS, and FedEx are `usps`, `ups`, and `fedex` respectively.

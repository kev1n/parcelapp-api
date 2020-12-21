# parcelapp-api

This is an official python API for adding parcels to [Parcel](https://parcelapp.net/). There are future plans to view added parcels but is not supported at this moment.

```python
print(parceladd("TOKEN", "DESCRIPTION", "TRKNUMBER", "CARRIER"))
> ADDED
```

Your token can be found in your [web dashboard](https://web.parcelapp.net/) cookies:

![image-20201220201439439](https://cdn.discordapp.com/attachments/480736870540771329/790386685787504690/unknown.png)

Common carrier codes are:

| **Carrier** | **Carrier Code** |
| ----------- | ---------------- |
| USPS        | usps             |
| UPS         | ups              |
| FedEx       | fedex            |

# parcelapp-api

This is an unofficial python API for adding parcels to [Parcel](https://parcelapp.net/). There are future plans to view previously added parcels and other features.

```python
print(parceladd("TOKEN", "DESCRIPTION", "TRKNUMBER", "CARRIER"))
> ADDED
```

Your token can be found in your [web dashboard](https://web.parcelapp.net/) cookies:

![image-20201220201439439](https://cdn.discordapp.com/attachments/480736870540771329/790386685787504690/unknown.png)

The carrier codes for USPS, UPS, and Fedex are `usps`, `ups`, and `fedex` respectively.

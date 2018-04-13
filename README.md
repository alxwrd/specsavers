# Specsavers :eyeglasses:
_A Python wrapper around the Specsavers appointment booking API_

```python
>>> import specsavers

# Find local stores
>>> stores = specsavers.locate(latitude=51.507879, longitude=0.087732)

# Closest / first store
>>> stores[0]
<Store name="londonwall">

# Store by name
>>> stores["strand"]
<Store name="strand">

# Lookup directly by name
>>>other_store = specsavers.find("nottingham")

>>> other_store.appointments() # Implies today
[<Appointment time="11:45">, <Appointment time="15:00">]

>>> other_store.appointments("tomorrow")[0]
<Appointment time="09:20">
```

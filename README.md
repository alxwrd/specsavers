# Specsavers :eyeglasses:
_A Python wrapper around the Specsavers appointment booking API_

> **IMPORTANT**: This project is NOT affiliated with Specsavers. Specsavers, nor this
library, should not be held responsible for any misinformation gained regarding
appointment information during the use of this library. 

> **NOTE**: Whilst this is a toy project, the endpoints it connects to are very real.
Please be responsible if you use this library: don't spam requests, and don't spam bookings.


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

|           3.6               |            Nightly              |
|-----------------------------|---------------------------------|
| [![3.6 build status][1]][3] | [![Nightly build status][2]][3] |

[1]: https://travis-matrix-badges.herokuapp.com/repos/alxwrd/specsavers/branches/master/1
[2]: https://travis-matrix-badges.herokuapp.com/repos/alxwrd/specsavers/branches/master/2
[3]: https://travis-ci.org/alxwrd/specsavers

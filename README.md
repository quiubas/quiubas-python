# Quiubas PHP Library

## Requirements
- Python Python 2.7.10 +
- `re` Library
- `requests` Library
- `urllib` Library
- `json` Library


## Installation

Install **quiubas** via pip

```bash
pip install quiubas
```

## Quickstart

### Send an SMS

```python
# install the library via pip install

from quiubas import Quiubas

quiubas = quiubas()
quiubas.setAuth( 'api_key', 'api_private' )

response = quiubas.sms.send( {
	'to_number': '+52552512421',
	'message' : 'Hello there'
})

print response
```
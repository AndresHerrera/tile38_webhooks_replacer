# Massive URL Webhooks replacer for tile38 

### Requirements
  
  - https://github.com/iwpnd/pyle38

```sh
pip install pyle38
```sh

### Configure

```python
NEW_ENDPOINT_URL = "https://nuevaurl.actiontracker.eu/api-detections/receive-message"
TILE38_SERVER = "redis://localhost:9852"
TILE38_CLI_COMMAND = "tile38-cli -h localhost -p 9852"
```

### Ejecutar script
```sh
python replace_url_hooks.py
```sh



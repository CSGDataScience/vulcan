# Vulcan Server

VulcanServer is a convention-heavy but light extension of the Flask Web Framework.
The VulcanServer class makes it simple to turn your [VulcanService](service.md) into a full
fledged REST API.

## Creating an API

```python
from my_project import MyVulcanService
from vulcan.server import VulcanServer

my_service_api = VulcanServer(__name__, service=MyVulcanService)

# VulcanServer.run supports all Flask.Application.run options
my_service_api.run(debug=True)
```

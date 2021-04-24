# Unpacker Karton Service

A modular Karton Framework service that unpacks common packers like UPX and others using the Qilling Framework.

![objects](docs/img/objects.png)

**Consumes:**
```json
{
    "type": "sample",
    "stage": "recognized",
    "kind": "runnable",
    "platform": "win32"
},
{
    "type": "sample", 
    "stage": "recognized",
    "kind": "runnable",
    "platform": "win64" 
},
{ 
    "type": "sample",
    "stage": "recognized",
    "kind": "runnable",
    "platform": "linux"
}
```

```json
{
    "type": "sample",
    "kind": "raw",
    "payload": {
        "sample": <Resource>,
        "parent": <Resource>,
    }
}
```

## Usage

Make sure you have setup the core system: https://github.com/CERT-Polska/karton

**Install from PyPi:**
```shell
$ pip install karton-unpacker
$ git clone https://github.com/c3rb3ru5d3d53c/karton-unpacker-modules.git modules/
$ find modules/ -name "requirements.txt" | while read i; do pip install -r $i; done
$ karton-unpacker --config-file /home/karton/karton.ini --modules modules/
```

**Install from Source:**
```shell
$ git clone --recursive https://github.com/c3rb3ru5d3d53c/karton-unpacker.git
$ cd karton-unpacker/
$ virtualenv venv/
$ source venv/bin/activate
$ pip install .
$ karton-unpacker --config-file /home/karton/karton.ini --modules modules/
```

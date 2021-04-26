# Unpacker Karton Service

[![build](https://travis-ci.org/c3rb3ru5d3d53c/karton-unpacker.svg?branch=master)](https://travis-ci.org/c3rb3ru5d3d53c/karton-unpacker)
![license](https://img.shields.io/github/license/c3rb3ru5d3d53c/karton-unpacker-modules)
![pypi-version](https://pypip.in/v/karton-unpacker/badge.png)
![pypi-downloads](https://pypip.in/d/karton-unpacker/badge.png)
![pypi-egg](https://pypip.in/wheel/karton-unpacker/badge.svg)
![issues](https://img.shields.io/github/issues/c3rb3ru5d3d53c/karton-unpacker-modules)
![stars](https://img.shields.io/github/stars/c3rb3ru5d3d53c/karton-unpacker-modules)

A modular Karton Framework service that unpacks common packers like UPX and others using the Qilling Framework.

This project is FREE as in FREE :beer:, use it commercially, privately or however you see fit.

If you like this project and wish to donate :moneybag: to support the fight against malware...

Buy me a :tea:, as I don't drink :beer:, by sending me some ₿ to `16oXesi7uv3jdPZxxwarHSD2f3cNMpaih9`

![objects](https://github.com/c3rb3ru5d3d53c/karton-unpacker/raw/master/docs/img/objects.png)
*Figure 1: Example of UPX Unpacked Children*

![qiling](https://github.com/c3rb3ru5d3d53c/karton-unpacker/raw/master/docs/img/qiling.jpeg)
*Figure 2: Qiling Framework Unpacking `calc.exe` shellcode from `tests/shellcode.exe`*

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
    "kind": "runnable",
    "stage": "recognized",
    "platform": <win32|win64> (If PE File in Dump),
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
$ git clone --recursive https://github.com/qilingframework/qiling.git
# Due to distribution restriction, Qiling Framework will not bundle Microsoft Windows DLL files and registry.
# Please use the script qiling/examples/scripts/dllscollector.bat on your Windows machine to collect the required DLLS for the rootfs
# Once the required DLLs have been collected copy them in the rootfs
$ karton-unpacker --config-file /home/karton/karton.ini --modules modules/ --rootfs qiling/examples/rootfs/ --debug
```

**Install from Source:**
```shell
$ git clone --recursive https://github.com/c3rb3ru5d3d53c/karton-unpacker.git
$ cd karton-unpacker/
$ virtualenv venv/
$ source venv/bin/activate
$ pip install .
$ git clone --recursive https://github.com/qilingframework/qiling.git
# Due to distribution restriction, Qiling Framework will not bundle Microsoft Windows DLL files and registry.
# Please use the script qiling/examples/scripts/dllscollector.bat on your Windows machine to collect the required DLLS for the rootfs
# Once the required DLLs have been collected copy them in the rootfs
$ karton-unpacker --config-file /home/karton/karton.ini --modules modules/ --rootfs qiling/examples/rootfs/ --debug
```

# Testing Your Installation

Once you have completed installing `karton-unpacker`, try uploading the file `tests/shellcode.exe` to mwdb.

If successful, you will see an file in relations with the name `unpacked`, this is the extracted shellcode to spawn `cmd.exe`.

# Contributing

If you wish to contribute your own modules to automatically unpack malware, please refer to [CONTRIBUTING.md](https://github.com/c3rb3ru5d3d53c/karton-unpacker/blob/master/CONTRIBUTING.md)

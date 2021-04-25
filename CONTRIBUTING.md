# Contributing Karton Unpacker Modules

Creating a Karton Unpacker modules is quite a simple process.

**Step 1: Download the Main Repository**
```bash
git clone --recursive https://github.com/c3rb3ru5d3d53c/karton-unpacker.git
cd karton-unpacker/modules/
```

**Step 2: Create your Module Directory with Required Files**
```bash
mkdir example/
touch README.md requirements.txt example.py
```

**Step 3: Write your Module**
```python
#!/usr/bin/env python3

import logging
import argparse
from karton.core import Task, Resource

__author__  = 'c3rb3ru5' # Take Pride in Your Work
__version__ = '1.0.0'    # Version of Your Module

log = logging.getLogger(__name__) # Setup Logging

class KartonUnpackerModule():

    """
    Example Unpacker Module (Description of your Module)
    """

    def __init__(self, sample, config):
        self.enabled = True        # Required to Determine if You Want to Run your Module
        self.config = config       # Required to Pass Configuration to Other Functions rootfs etc.
        self.data = sample.content # Required to Pass Packed Sample Data to Other Functions

    def main(self) -> list:
        # Perform Operations on self.data to unpack the sample
        unpacked_data = bytes('example'.encode())
        task = Task(
            headers={
                'type': 'sample',
                'kind': 'runnable',
                'stage': 'recognized'
            },
            payload={
                'parent': Resource(name='sample', content=self.data),      # Set Parent Data (Packed Sample)
                'sample': Resource(name='unpacked', content=unpacked_data) # Set Child Data (Unpacked Sample)
            }
        )
        # A list of tasks must be returned, as there can be more than one unpacked child
        return [task]

# The Following Code Allows You to Test Samples without Going through the Karton Pipeline
if __name__ in '__main__':
    parser = argparse.ArgumentParser(
        prog='example.py',
        description=f'Karton Unpacker Service Example Module v{__version__} (CLI Test Utility)',
        epilog=f'Author: {__author__}'
    )
    parser.add_argument('-i','--input', help='Input File', type=str, required=True)
    args = parser.parse_args()
    f = open(args.input, 'rb')
    sample = Resource(name=args.input, content=f.read())
    f.close()
    module = KartonUnpackerModule(sample)
    if module.enabled is True:
        task = module.main()
        data = json.loads(str(task))
        print(json.dumps(data, indent=4))
```

To test your module:
```bash
chmod +x example.py
./example.py --input sample.bin
```

Specify your Python dependencies in the `requirements.txt` file including the version number for each one.

Write a semi descriptive `README.md` so everyone can read about your module.

If your module also requires modification to the root `karton-unpacker` repository then DM me on Twitter or make a pull request there as well.

If you need more pointers on how to create a module, DM me on Twitter.

**Additional Resources**
- [Qiling Framework Documentation](https://docs.qiling.io/en/latest/)
- [Karton Framework Documentation](https://karton-core.readthedocs.io/en/latest/index.html)
- [YARA Python Documentation](https://yara.readthedocs.io/en/latest/index.html)
- [Capstone Engine Documentation](http://www.capstone-engine.org/documentation.html)
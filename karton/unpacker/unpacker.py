import logging
import subprocess
import glob
import pkgutil
import hashlib
import importlib
from karton.core import Config, Karton, Task, Resource
from typing import Optional

from .__version__ import __version__

log = logging.getLogger(__name__)

def unpacker_module_worker(sample, user_config, module) -> Task:
    spec = importlib.util.spec_from_file_location("module.name", module)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module = module.KartonUnpackerModule(sample=sample, config=user_config)
    if module.enabled is True:
        return module.main()
    return []

class Unpacker(Karton):

    """
    A modular Karton Framework service that unpacks common packers like UPX, MPress and others using the Qilling Framework.
    """

    identity = "karton.unpacker"

    filters = [
        {"type": "sample", "stage": "recognized", "kind": "runnable", "platform": "win32"},
        {"type": "sample", "stage": "recognized", "kind": "runnable", "platform": "win64" },
        {"type": "sample", "stage": "recognized", "kind": "runnable", "platform": "linux"}
    ]

    @classmethod
    def args_parser(cls):
        parser = super().args_parser()
        parser.add_argument("--modules", help="Modules Directory", type=str, required=True)
        parser.add_argument("--rootfs", help="Emulator RootFS", type=str, default=None, required=False)
        parser.add_argument("--timeout", help="Emulator Timeout", type=int, default=5000, required=False)
        parser.add_argument("--debug", help="Debug", action='store_true', default=False, required=False)
        return parser

    @classmethod
    def main(cls):
        parser = cls.args_parser()
        args = parser.parse_args()
        config = Config(args.config_file)
        user_config = {
            'modules': args.modules,
            'rootfs': args.rootfs,
            'timeout': args.timeout,
            'debug': args.debug
        }
        service = Unpacker(config=config, user_config=user_config)
        service.loop()

    def __init__(self, user_config: Optional[dict] = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        modules = user_config['modules']
        modules = modules or "modules"
        self.modules = glob.glob(f'{modules}/**/*.py', recursive=True)
        self.user_config = user_config

    def process(self, task: Task) -> None:
        sample = task.get_resource("sample")
        for module in self.modules:
            tasks = unpacker_module_worker(sample, self.user_config, module)
            for task in tasks:
                self.send_task(task)

if __name__ == "__main__":
    Unpacker().loop()

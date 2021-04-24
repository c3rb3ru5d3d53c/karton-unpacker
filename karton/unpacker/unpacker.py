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

def unpacker_module_worker(sample, module) -> Task:
    spec = importlib.util.spec_from_file_location("module.name", module)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module = module.KartonUnpackerModule(sample=sample)
    if module.enabled is True:
        return module.main()

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
        parser.add_argument("--modules", help="Modules Directory", required=True)
        return parser

    @classmethod
    def main(cls):
        parser = cls.args_parser()
        args = parser.parse_args()
        config = Config(args.config_file)
        service = Unpacker(config=config, modules=args.modules)
        service.loop()

    def __init__(self, modules: Optional[str] = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        modules = modules or "modules"
        self.modules = glob.glob(f'{modules}/**/*.py', recursive=True)

    def process(self, task: Task) -> None:
        sample = task.get_resource("sample")
        for module in self.modules:
            task = unpacker_module_worker(sample, module)
            if task is not None:
                log.info(f"successfully unpacked {sample.name}, sending task")
                self.send_task(task)

if __name__ == "__main__":
    Unpacker().loop()

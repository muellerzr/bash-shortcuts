# Shortcuts relating to pytest
from fastcore.script import call_parse
from subprocess import run
from typing import Union
import sys

@call_parse
def run_pytest(
    fname=None, # The filenames to test
    flags="sv", # Flags after `pytest`
    cuda="0,1", # CUDA_VISIBLE_DEVICES flag
    blocking=True, # CUDA_LAUNCH_BLOCKING
):
    "Runs pytest tests"
    cmd = [f'CUDA_VISIBLE_DEVICES={cuda}']
    if blocking:
        cmd += "CUDA_LAUNCH_BLOCKING=1"
    cmd += f'pytest {f"-{flags} " if flags != "" else ""}{fname}'
    run(cmd, stderr=sys.stderr, stdout=sys.stdout)

# Shortcuts relating to pytest
from fastcore.script import call_parse
from subprocess import run
from typing import Union
import sys

@call_parse
def run_pytest(
    fname:str, # The filenames to test
    flags:str="sv", # Flags after `pytest`
    cuda:str="0,1", # CUDA_VISIBLE_DEVICES flag
    blocking:bool=True, # CUDA_LAUNCH_BLOCKING
):
    "Runs pytest tests"
    cmd = [f'CUDA_VISIBLE_DEVICES="{cuda}"']
    if blocking:
        cmd += ['CUDA_LAUNCH_BLOCKING="1"']
    cmd += [f'pytest {f"-{flags} " if flags != "" else ""}{fname}']
    print(f'Running `{cmd}`')
    run(cmd, stderr=sys.stderr, stdout=sys.stdout)

# Shortcuts relating to pytest
from fastcore.script import call_parse
from pathlib import Path
from subprocess import run
from typing import Union
import sys, os

def _new_env(key_dict):
    env = os.environ.copy()
    for key,value in key_dict.items():
        env[key.upper()] = value
    return env

@call_parse
def run_pytest(
    fname:str, # The filenames to test
    flags:str="sv", # Flags after `pytest`
    cuda:str="0,1", # CUDA_VISIBLE_DEVICES flag
    blocking:bool=True, # CUDA_LAUNCH_BLOCKING
):
    "Runs pytest tests"
    env = {"cuda_visible_devices": cuda}
    if blocking:
        env['cuda_launch_blocking'] = "1"
    cmd = [f'pytest {f"-{flags} " if flags != "" else ""}{fname}']
    env = _new_env(env)
    run(cmd, stderr=sys.stderr, stdout=sys.stdout, env=env, shell=True)

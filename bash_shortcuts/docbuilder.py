# Shortcuts for working with hf-doc-builder
from subprocess import check_output, run
from pathlib import Path
from fastcore.script import call_parse

@call_parse
def launch_docs(
        source:Path="source", # The path to the documentation folder
    ):
    "Launches documentation for a git repo. Should be called from the `docs` folder"
    repo = check_output(['git', 'rev-parse', '--show-toplevel'])
    repo = check_output(['basename', repo]).strip()
    run(['doc-builder', 'preview', repo, source])
    
    

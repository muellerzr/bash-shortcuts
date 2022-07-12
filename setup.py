from setuptools import setup, find_packages

setup(
        name="bash-shortcuts",
        version="0.0.1",
        author="Zach Mueller",
        author_email="muellerzr@gmail.com",
        description="Some bash shortcuts made with fastcore",
        packages=find_packages(),
        entry_points={
                "console_scripts": [
                        "launch-docs=bash_shortcuts.docbuilder:launch_docs",
                        "run-pytest=bash_shortcuts.pytest:run_pytest"
                ]
        },
        python_requires=">=3.7.0",
        install_requires=['fastcore', 'hf-doc-builder']
)

# !/usr/bin/env python
# -*- coding: utf-8 -*-
import shutil
import subprocess

if __name__ == "__main__":
    shutil.rmtree("licenses", ignore_errors=True)

    msg = ""
    # try to run git init
    try:
        subprocess.run(["git", "init", "-q"])
        subprocess.run(["git", "checkout", "-b", "main"])
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-q", "-m", "initial commit"])
        subprocess.run(
            [
                "git",
                "remote",
                "add",
                "origin",
                "https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.package_name}}.git",
            ]
        )
    except Exception:
        msg += ""

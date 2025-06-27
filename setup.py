#!/usr/bin/env python3
"""
Packaging setup for Arsenal – updated to bootstrap PyWhisker and PKINITtools
into the active virtual-env after pip install.
"""
import os
import pathlib
import subprocess
import sys
from setuptools import find_packages, setup
from setuptools.command.install import install

HERE = pathlib.Path(__file__).parent


def parse_requirements(path: pathlib.Path) -> list[str]:
    """Return a clean list of requirements (skip blanks / comments)."""
    lines = path.read_text().splitlines()
    return [ln.strip() for ln in lines if ln.strip() and not ln.startswith("#")]


class PostInstall(install):
    """Run extra steps *after* pip install finishes."""

    def run(self) -> None:
        # 1) normal installation first
        super().run()

        # 2) only proceed inside a virtual-env
        venv_root = os.environ.get("VIRTUAL_ENV")
        if not venv_root:
            print(
                "\n[!] Not inside a virtual-environment – skipping external tool bootstrap."
            )
            return

        venv_root = pathlib.Path(venv_root)
        venv_bin = venv_root / "bin"
        ext_dir = venv_root / "ext"
        ext_dir.mkdir(exist_ok=True)

        # helper for subprocess calls
        def sh(cmd: list[str]) -> None:
            print(f"[+] {' '.join(cmd)}")
            subprocess.check_call(cmd)

        # ────────────────────────────  PyWhisker  ────────────────────────────
        pywhisker_dir = ext_dir / "pywhisker"
        if not pywhisker_dir.exists():
            sh(["git", "clone", "-q", "https://github.com/ShutdownRepo/pywhisker", str(pywhisker_dir)])
            sh([sys.executable, "-m", "pip", "install", "-r", str(pywhisker_dir / "requirements.txt")])
            sh([sys.executable, str(pywhisker_dir / "setup.py"), "install"])

        # ────────────────────────────  PKINITtools  ────────────────────────────
        pkinit_dir = ext_dir / "PKINITtools"
        if not pkinit_dir.exists():
            sh(["git", "clone", "-q", "https://github.com/dirkjanm/PKINITtools", str(pkinit_dir)])

        # ensure runtime deps (impacket, minikerberos, oscrypto-git) are present
        sh([sys.executable, "-m", "pip", "install", "impacket", "minikerberos"])
        sh([sys.executable, "-m", "pip", "install", "-I", "git+https://github.com/wbond/oscrypto.git"])

        # symlink helper scripts into <venv>/bin
        for script in ("gettgtpkinit.py", "getNThash.py"):
            target = pkinit_dir / script
            link = venv_bin / script
            if not link.exists():
                link.symlink_to(target)
                print(f"[+] Symlinked {link.relative_to(venv_root)} → {target.relative_to(venv_root)}")

        print("\n[✓] PyWhisker & PKINITtools bootstrapped inside the virtual-env.")


setup(
    name="armoury-cli",
    version="1.2.8",  # bumped because we changed install behaviour
    description="Arsenal is a quick inventory, reminder and launcher for pentest commands.",
    long_description=(HERE / "README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Guillaume Muh, mayfly",
    author_email="no-reply@orange.com",
    url="https://github.com/0xJam3z/armoury",
    license="GPL-3.0",
    python_requires=">=3.8",
    packages=find_packages(),
    include_package_data=True,
    package_data={"": ["data/cheats/*"]},
    exclude_package_data={"": ["my_cheats/", "mindmap/"]},
    install_requires=parse_requirements(HERE / "requirements.txt"),
    entry_points={"console_scripts": ["arsenal = arsenal.app:main"]},
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Topic :: Security",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    cmdclass={"install": PostInstall},  # 🔑 hook in the custom installer
)

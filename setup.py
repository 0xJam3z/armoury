#!/usr/bin/env python3
"""
Packaging setup for **Armoury** – revamped fork of Arsenal.
This installer still bootstraps PyWhisker and PKINITtools inside the active
virtual‑environment after a standard `pip install .`.
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
    return [
        ln.strip()
        for ln in path.read_text().splitlines()
        if ln.strip() and not ln.startswith("#")
    ]


class PostInstall(install):
    """Run extra steps *after* pip install finishes."""

    def run(self) -> None:  # noqa: D401 – imperative mood is fine for setuptools
        # 1) perform the regular installation first
        super().run()

        # 2) only continue if we're inside a virtual‑environment
        venv_root_s = os.environ.get("VIRTUAL_ENV")
        if not venv_root_s:
            print("[!] Not inside a virtual‑env — skipping external‑tool bootstrap.")
            return

        venv_root = pathlib.Path(venv_root_s)
        venv_bin = venv_root / "bin"
        ext_dir = venv_root / "ext"
        ext_dir.mkdir(exist_ok=True)

        def sh(cmd: list[str]) -> None:
            """Wrapper for subprocess calls with logging."""
            print(f"[+] {' '.join(cmd)}")
            subprocess.check_call(cmd)

        # ── PyWhisker ──────────────────────────────────────────────
        pw_dir = ext_dir / "pywhisker"
        if not pw_dir.exists():
            sh([
                "git",
                "clone",
                "-q",
                "https://github.com/ShutdownRepo/pywhisker",
                str(pw_dir),
            ])
            sh([
                sys.executable,
                "-m",
                "pip",
                "install",
                "-r",
                str(pw_dir / "requirements.txt"),
            ])
            sh([sys.executable, str(pw_dir / "setup.py"), "install"])

        # ── PKINITtools ────────────────────────────────────────────
        pk_dir = ext_dir / "PKINITtools"
        if not pk_dir.exists():
            sh([
                "git",
                "clone",
                "-q",
                "https://github.com/dirkjanm/PKINITtools",
                str(pk_dir),
            ])

        # ensure runtime deps
        sh([sys.executable, "-m", "pip", "install", "impacket", "minikerberos"])
        sh([
            sys.executable,
            "-m",
            "pip",
            "install",
            "-I",
            "git+https://github.com/wbond/oscrypto.git",
        ])

        # symlink helper scripts into <venv>/bin
        for script in ("gettgtpkinit.py", "getNThash.py"):
            target = pk_dir / script
            link = venv_bin / script
            if not link.exists():
                link.symlink_to(target)
                rel_link = link.relative_to(venv_root)
                rel_tgt = target.relative_to(venv_root)
                print(f"[+] Symlinked {rel_link} → {rel_tgt}")

        print("\n[✓] PyWhisker & PKINITtools bootstrapped inside the virtual‑env.")


setup(
    name="armoury-cli",            # ← new PyPI package name
    version="2.0.0",               # first public release of the rebranded fork
    description=(
        "Armoury — modernised inventory, reminder, and launcher for pentest commands"
    ),
    long_description=(HERE / "README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Guillaume Muh, mayfly, and the Armoury maintainers",
    author_email="no-reply@orange.com",
    url="https://github.com/0xJam3z/armoury",
    license="GPL-3.0",
    python_requires=">=3.8",
    packages=find_packages(),
    include_package_data=True,
    package_data={"": ["data/cheats/*"]},
    exclude_package_data={"": ["my_cheats/", "mindmap/"]},
    install_requires=parse_requirements(HERE / "requirements.txt"),
    entry_points={
        "console_scripts": [
            "armoury = arsenal.app:main",  # preferred new binary
            "arsenal  = arsenal.app:main",  # legacy shim for backward‑compat
        ]
    },
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
    cmdclass={"install": PostInstall},  # hook in the custom installer
)

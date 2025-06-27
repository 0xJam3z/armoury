#!/usr/bin/env python3
"""
Packaging setup for **Armoury** – revamped fork of Arsenal.
Includes an optional post‑install bootstrap that clones PyWhisker and
PKINITtools **only when the package is actually being installed** into a
user environment (not while building a wheel in an isolated build dir).
"""
import os
import pathlib
import subprocess
import sys
from setuptools import find_packages, setup
from setuptools.command.install import install

HERE = pathlib.Path(__file__).parent


# ───────────────────────────── helpers ──────────────────────────────

def parse_requirements(path: pathlib.Path) -> list[str]:
    """Return list of non‑empty, non‑comment lines from requirements.txt."""
    return [ln.strip() for ln in path.read_text().splitlines() if ln.strip() and not ln.startswith("#")]


def ensure_pip_available() -> None:
    """Some build environments (PEP‑517 wheel builds) lack pip.  Add it."""
    try:
        import pip  # noqa: F401 – just probing
    except ModuleNotFoundError:
        subprocess.check_call([sys.executable, "-m", "ensurepip", "--upgrade"])


# ───────────────────────────── post‑install ─────────────────────────

class PostInstall(install):
    """Run extra steps after *real* installation — skipped during wheel build."""

    def run(self):
        # 1. normal install first (copies files into site‑packages)
        super().run()

        # 2. Skip bootstrap when we're inside `bdist_wheel` (build isolation)
        if any(cmd in sys.argv for cmd in {"bdist_wheel", "egg_info"}):
            print("[~] Detected wheel build; skipping PyWhisker/PKINITtools bootstrap.")
            return

        # 3. Only proceed inside an activated virtual‑env (safer for Kali / PEP‑668)
        venv_root = os.environ.get("VIRTUAL_ENV")
        if not venv_root:
            print("[!] No VIRTUAL_ENV detected — skipping bootstrap.")
            return

        venv_root = pathlib.Path(venv_root)
        venv_bin = venv_root / "bin"
        ext_dir = venv_root / "ext"
        ext_dir.mkdir(exist_ok=True)

        def sh(cmd: list[str]):
            print(f"[+] {' '.join(cmd)}")
            subprocess.check_call(cmd)

        ensure_pip_available()

        # ── PyWhisker ────────────────────────────────────────────────
        pywhisker_dir = ext_dir / "pywhisker"
        if not pywhisker_dir.exists():
            sh(["git", "clone", "https://github.com/ShutdownRepo/pywhisker", str(pywhisker_dir)])
            sh([sys.executable, "-m", "pip", "install", "-r", str(pywhisker_dir / "requirements.txt")])
            sh([sys.executable, str(pywhisker_dir / "setup.py"), "install"])

        # ── PKINITtools ──────────────────────────────────────────────
        pkinit_dir = ext_dir / "PKINITtools"
        if not pkinit_dir.exists():
            sh(["git", "clone", "https://github.com/dirkjanm/PKINITtools", str(pkinit_dir)])

        sh([sys.executable, "-m", "pip", "install", "impacket", "minikerberos"])
        sh([sys.executable, "-m", "pip", "install", "-I", "git+https://github.com/wbond/oscrypto.git"])

        for script in ("gettgtpkinit.py", "getNThash.py"):
            target = pkinit_dir / script
            link = venv_bin / script
            if not link.exists():
                link.symlink_to(target)
                print(f"[+] Symlinked {link.relative_to(venv_root)} → {target.relative_to(venv_root)}")

        print("[✓] PyWhisker & PKINITtools bootstrapped inside the virtual‑env.")


# ───────────────────────────── setup() call ─────────────────────────

setup(
    name="armoury-cli",
    version="2.0.0",  # first public re‑branded release
    description="Armoury – streamlined inventory & launcher for pentest commands.",
    long_description=(HERE / "README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Forked from Guillaume Muh / mayfly",
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
            "armoury = arsenal.app:main",  # new binary
            "arsenal  = arsenal.app:main",  # legacy shim for backward compatibility
        ]
    },
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Topic :: Security",
        "Topic :: Utilities",
    ],
    cmdclass={"install": PostInstall},
)

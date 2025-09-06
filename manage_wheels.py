import argparse
import platform
import subprocess
import sys
import os

LIBS_DIR = "libs"
REQUIREMENTS = "requirements.txt"

def detect_platform():
    system = platform.system().lower()
    machine = platform.machine().lower()
    py_version = f"{sys.version_info.major}.{sys.version_info.minor}"

    if system == "darwin" and machine == "arm64":
        plat = "macosx_11_0_arm64"
    elif system == "darwin" and machine in ("x86_64", "amd64"):
        plat = "macosx_10_9_x86_64"
    elif system == "linux" and machine in ("x86_64", "amd64"):
        plat = "manylinux2014_x86_64"
    elif system == "windows" and machine in ("x86_64", "amd64"):
        plat = "win_amd64"
    else:
        raise RuntimeError(f"Unsupported platform: {system} {machine}")

    return plat, py_version

def download_packages():
    plat, py_version = detect_platform()
    target_dir = os.path.join(LIBS_DIR, f"{plat}_cp{py_version.replace('.', '')}")
    os.makedirs(target_dir, exist_ok=True)

    print(f"=== Downloading packages for Python {py_version} ===")
    subprocess.run(
        [
            sys.executable, "-m", "pip", "download",
            "-r", REQUIREMENTS,
            "-d", target_dir
        ],
        check=True
    )

    # Explicitly fetch common build dependencies
    build_deps = ["setuptools", "wheel", "scikit-build-core", "ninja", "cmake"]
    subprocess.run(
        [
            sys.executable, "-m", "pip", "download",
            "-d", target_dir,
            *build_deps
        ],
        check=True
    )

    print(f"DONE: Packages + build deps stored in: {target_dir}")

def install_packages():
    plat, py_version = detect_platform()
    target_dir = os.path.join(LIBS_DIR, f"{plat}_cp{py_version.replace('.', '')}")

    if not os.path.exists(target_dir):
        print(f"ERROR: No packages found for {plat}, Python {py_version}. Run with --download first.")
        sys.exit(1)

    print(f"=== Installing wheels from {target_dir} ===")
    subprocess.run(
        [
            sys.executable, "-m", "pip", "install",
            "--no-index", "--find-links", target_dir,
            "-r", REQUIREMENTS
        ],
        check=True
    )
    print("DONE: Installation complete!")


def main():
    parser = argparse.ArgumentParser(description="Manage wheels for offline installation")
    parser.add_argument("--download", action="store_true", help="Download wheels for current platform")
    parser.add_argument("--install", action="store_true", help="Install wheels for current platform")
    args = parser.parse_args()

    os.makedirs(LIBS_DIR, exist_ok=True)

    if args.download:
        download_packages()
    elif args.install:
        install_packages()
    else:
        print("ERROR: Must specify either --download or --install")

if __name__ == "__main__":
    main()

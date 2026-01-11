import os
import shutil
import subprocess
import string

BASE = "/data/data"
PKG_PREFIX = "com.roblox.clien"

# clienb -> clienm
CLIENTS = string.ascii_lowercase[
    string.ascii_lowercase.index("b"):
    string.ascii_lowercase.index("m") + 1
]

KEEP = {"app_webview", "shared_prefs"}

def force_stop(pkg):
    subprocess.run(
        ["am", "force-stop", pkg],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

def wipe_package(pkg):
    path = os.path.join(BASE, pkg)
    if not os.path.isdir(path):
        return

    print(f"\n[+] Resetting {pkg}")
    force_stop(pkg)

    for item in os.listdir(path):
        if item in KEEP:
            print(f"  [KEEP] {item}")
            continue

        full = os.path.join(path, item)
        try:
            if os.path.isdir(full):
                shutil.rmtree(full)
            else:
                os.remove(full)
            print(f"  [DEL ] {item}")
        except Exception as e:
            print(f"  [FAIL] {item}: {e}")

def main():
    for c in CLIENTS:
        wipe_package(PKG_PREFIX + c)

    print("\n✅ DONE — giống Clear Data nhưng KHÔNG logout")

if __name__ == "__main__":
    main()

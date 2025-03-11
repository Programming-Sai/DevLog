import os
import shutil
import sys
import subprocess

# Determine OS-specific installation path
if sys.platform.startswith("win"):
    install_dir = os.path.join(os.environ["LOCALAPPDATA"], "Programs", "DevLog")
    exe_name = "devlog.exe"
    path_var = "Path"
else:
    install_dir = "/usr/local/bin"
    exe_name = "devlog"

# Ensure the installation directory exists
os.makedirs(install_dir, exist_ok=True)

# Build the standalone executable
print("🔧 Building DevLog...")
os.system(f'pyinstaller --onefile --name {exe_name} main.py')

# Define paths
src_path = os.path.join("dist", exe_name)
dest_path = os.path.join(install_dir, exe_name)

# Move the executable to the global installation path
if os.path.exists(dest_path):
    print("♻️ Updating existing installation...")
    os.remove(dest_path)

shutil.copy(src_path, dest_path)

# Make it executable (Linux/macOS)
if not sys.platform.startswith("win"):
    os.chmod(dest_path, 0o755)

# Add to system PATH dynamically
def add_to_path_windows():
    current_path = os.environ.get(path_var, "")
    if install_dir not in current_path:
        print("🔧 Adding DevLog to system PATH...")
        try:
            subprocess.run(f'setx {path_var} "{current_path};{install_dir}"', shell=True)
            print("✅ DevLog added to PATH. Restart your terminal for changes to take effect.")
        except Exception as e:
            print(f"⚠️ Failed to add DevLog to PATH automatically: {e}")
            print(f"➡️ Please add `{install_dir}` to your system PATH manually.")

def add_to_path_linux():
    bashrc_path = os.path.expanduser("~/.bashrc")
    profile_path = os.path.expanduser("~/.profile")
    export_cmd = f'\nexport PATH="{install_dir}:$PATH"\n'

    if install_dir not in os.environ["PATH"]:
        print("🔧 Adding DevLog to system PATH...")
        try:
            with open(bashrc_path, "a") as f:
                f.write(export_cmd)
            with open(profile_path, "a") as f:
                f.write(export_cmd)
            print("✅ DevLog added to PATH. Restart your terminal or run `source ~/.bashrc`.")
        except Exception as e:
            print(f"⚠️ Failed to add DevLog to PATH automatically: {e}")
            print(f"➡️ Please add `{install_dir}` to your system PATH manually.")

# Apply changes based on OS
if sys.platform.startswith("win"):
    add_to_path_windows()
else:
    add_to_path_linux()

print(f"✅ DevLog installed globally! Run it using: `{exe_name}`")


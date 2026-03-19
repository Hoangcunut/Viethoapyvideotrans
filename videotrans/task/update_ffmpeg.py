"""
# License

This script for downloading/updating ffmpeg was created by Thiago Ramos.
Contact: thiagojramos@outlook.com

The ffmpeg executables (ffmpeg.exe and ffprobe.exe) are created and maintained by the FFmpeg developers.
For more information, visit the FFmpeg GitHub repository: https://github.com/BtbN/FFmpeg-Builds

This script is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the script or the use or other dealings in the script.
"""

import os
import shutil
import zipfile

import requests


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEST_DIR = os.path.join(SCRIPT_DIR, "..", "..", "ffmpeg")
TEMP_DIR = os.path.join(DEST_DIR, "temp_ffmpeg")
ZIP_PATH = os.path.join(DEST_DIR, "ffmpeg.zip")
ASSET_NAME = "ffmpeg-n7.0-latest-win64-gpl-7.0.zip"
API_URL = "https://api.github.com/repos/BtbN/FFmpeg-Builds/releases/latest"
REQUEST_TIMEOUT = 60
CHUNK_SIZE = 8192


def _safe_remove(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path, ignore_errors=True)
        else:
            os.remove(path)


def _find_download_url(release_json):
    for asset in release_json.get("assets", []):
        if asset.get("name") == ASSET_NAME:
            return asset.get("browser_download_url")
    raise RuntimeError(f"Could not find expected FFmpeg asset: {ASSET_NAME}")


def _extract_required_binaries(zip_path, temp_dir):
    required_suffixes = {
        "/bin/ffmpeg.exe": os.path.join(temp_dir, "ffmpeg.exe"),
        "/bin/ffprobe.exe": os.path.join(temp_dir, "ffprobe.exe"),
    }
    extracted = {}

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        members = zip_ref.namelist()
        for suffix, output_path in required_suffixes.items():
            member_name = next((name for name in members if name.endswith(suffix)), None)
            if not member_name:
                raise RuntimeError(f"Missing required binary in archive: {suffix}")

            normalized = member_name.replace("\\", "/")
            if normalized.startswith("/") or ".." in normalized.split("/"):
                raise RuntimeError(f"Unsafe archive member detected: {member_name}")

            with zip_ref.open(member_name, "r") as src, open(output_path, "wb") as dst:
                shutil.copyfileobj(src, dst)
            extracted[suffix] = output_path

    return extracted


def main():
    os.makedirs(DEST_DIR, exist_ok=True)
    _safe_remove(TEMP_DIR)
    os.makedirs(TEMP_DIR, exist_ok=True)

    try:
        print("Fetching latest FFmpeg release metadata...")
        response = requests.get(API_URL, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        latest_release = response.json()
        latest_version = latest_release.get("tag_name", "unknown")
        download_url = _find_download_url(latest_release)

        print(f"Downloading FFmpeg {latest_version}...")
        with requests.get(download_url, stream=True, timeout=REQUEST_TIMEOUT) as response:
            response.raise_for_status()
            with open(ZIP_PATH, "wb") as f:
                for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                    if chunk:
                        f.write(chunk)

        print("Extracting required binaries...")
        extracted = _extract_required_binaries(ZIP_PATH, TEMP_DIR)

        ffmpeg_target = os.path.join(DEST_DIR, "ffmpeg.exe")
        ffprobe_target = os.path.join(DEST_DIR, "ffprobe.exe")

        _safe_remove(ffmpeg_target)
        _safe_remove(ffprobe_target)

        print("Moving new binaries to destination...")
        shutil.move(extracted["/bin/ffmpeg.exe"], ffmpeg_target)
        shutil.move(extracted["/bin/ffprobe.exe"], ffprobe_target)

        print("Download and replacement completed safely.")
    finally:
        _safe_remove(ZIP_PATH)
        _safe_remove(TEMP_DIR)


if __name__ == "__main__":
    main()

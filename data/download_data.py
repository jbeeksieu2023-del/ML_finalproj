"""
download_data.py — One-command dataset download for ML_finalproj.

Usage:
    python data/download_data.py

    Requirements:
        pip install kaggle
            kaggle.json API key (see instructions printed if missing)
            """

import os
import sys
import zipfile
import subprocess

KAGGLE_DATASET = "ayushtankha/70k-job-applicants-data-human-resource"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "raw")


def check_kaggle_setup():
      try:
                import kaggle  # noqa: F401
except ImportError:
        print("ERROR: kaggle package not installed. Run:  pip install kaggle")
        sys.exit(1)

    paths = [
              os.path.expanduser("~/.kaggle/kaggle.json"),
              os.path.join(os.environ.get("USERPROFILE", ""), ".kaggle", "kaggle.json"),
    ]
    if not any(os.path.exists(p) for p in paths):
              print("\nERROR: kaggle.json API key not found.")
              print("\nSetup steps:")
              print("  1. Go to https://www.kaggle.com/settings")
              print("  2. Click API > Create New Token  (downloads kaggle.json)")
              print("  3. Move it to: ~/.kaggle/kaggle.json  (Mac/Linux)")
              print("                 C:\\Users\\YourName\\.kaggle\\kaggle.json  (Windows)")
              print("  4. Run this script again.\n")
              sys.exit(1)
          print("Kaggle setup OK.")


def download_dataset():
      os.makedirs(OUTPUT_DIR, exist_ok=True)
      print(f"\nDownloading: {KAGGLE_DATASET}")
      result = subprocess.run(
          ["kaggle", "datasets", "download", "-d", KAGGLE_DATASET, "-p", OUTPUT_DIR],
          capture_output=True, text=True
      )
      if result.returncode != 0:
                print("Download failed:\n", result.stderr)
                sys.exit(1)
            print(result.stdout.strip())
    print("Download complete.")


def unzip_dataset():
      for fname in os.listdir(OUTPUT_DIR):
                if fname.endswith(".zip"):
                              fpath = os.path.join(OUTPUT_DIR, fname)
                              print(f"Extracting {fname} ...")
                              with zipfile.ZipFile(fpath, "r") as z:
                                                z.extractall(OUTPUT_DIR)
                                            os.remove(fpath)
                              print(f"Removed zip after extraction.")


def rename_csv():
      csvs = [f for f in os.listdir(OUTPUT_DIR) if f.endswith(".csv")]
    if not csvs:
              print("WARNING: No CSV found in data/raw/. Check manually.")
              return
          target = "job_applicants.csv"
    if target not in csvs:
              src = os.path.join(OUTPUT_DIR, csvs[0])
              dst = os.path.join(OUTPUT_DIR, target)
              os.rename(src, dst)
              print(f"Renamed '{csvs[0]}' to '{target}'")
else:
        print(f"File already named correctly: {target}")


def main():
      print("=" * 55)
    print("  ML_finalproj - Dataset Download Script")
    print("=" * 55)
    check_kaggle_setup()
    download_dataset()
    unzip_dataset()
    rename_csv()
    final = os.path.join(OUTPUT_DIR, "job_applicants.csv")
    if os.path.exists(final):
              mb = os.path.getsize(final) / 1024 / 1024
              print(f"\nReady: data/raw/job_applicants.csv ({mb:.1f} MB)")
              print("Next: run notebooks/01_data_preprocessing.ipynb")
          print("=" * 55)


if __name__ == "__main__":
      main()

"""Download and extract the NASA C-MAPSS dataset."""

from pathlib import Path
from urllib.request import urlretrieve
from zipfile import ZipFile

DATA_URL = (
    "https://phm-datasets.s3.amazonaws.com/NASA/"
    "6.+Turbofan+Engine+Degradation+Simulation+Data+Set.zip"
)

# Define project paths from the repository root.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

DOWNLOAD_PATH = RAW_DATA_DIR / "cmapss.zip"
EXTRACTED_DIR = RAW_DATA_DIR / "cmapss"

INNER_ZIP_PATH = (
    EXTRACTED_DIR
    / "6. Turbofan Engine Degradation Simulation Data Set"
    / "CMAPSSData.zip"
)

CMAPSS_DATA_DIR = RAW_DATA_DIR / "CMAPSSData"

RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

# Download the dataset only if it is not already available locally.
if not DOWNLOAD_PATH.exists():
    urlretrieve(DATA_URL, DOWNLOAD_PATH)

# Extract the outer archive and then the main C-MAPSS archive.
with ZipFile(DOWNLOAD_PATH) as zip_file:
    zip_file.extractall(EXTRACTED_DIR)

with ZipFile(INNER_ZIP_PATH) as zip_file:
    zip_file.extractall(CMAPSS_DATA_DIR)

print(f"Data downloaded to: {CMAPSS_DATA_DIR}")
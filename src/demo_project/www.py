from pathlib import Path

from demo_project.main import main1
from demo_project.storage import load_storage

a = Path("wuyihan.json")
b = load_storage(a)
main1(b)

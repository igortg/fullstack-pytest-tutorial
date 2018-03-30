from pathlib import Path
import tempfile
import shutil
import pytest


@pytest.fixture()
def tmp_data_folder():
    tempdir = tempfile.mkdtemp('roman7')
    yield Path(tempdir)
    shutil.rmtree(tempdir)

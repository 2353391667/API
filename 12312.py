import pytest

import KTDX.data
import yaml
import KTDX.config as config

with open(f"{config.BASE_PATH}\\data\\login1.yml") as f:
    data = yaml.safe_load(f)
    print(data)
    print(data["name3"])
    print(data["name1"]["name"])


@pytest.mark.parametrize("key", data()["name"])
def test01(key):
    print(key)

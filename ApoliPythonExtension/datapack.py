import json
from pathlib import Path

from blocks import Power, Base
import os
class PackMcMeta(Base):
    def __init__(self, pack_format: int = 9, description: str = "description"):
        super().__init__()
        self.pack = {"pack_format": pack_format, "description": description}
class Datapack:
    def __init__(self, name: str, namespace: str = "minecraft", path: str = "./", pack_mcmeta: PackMcMeta = PackMcMeta()):
        self.name = name
        self.pack_mcmeta = pack_mcmeta
        self.namespace = namespace
        self.path = path
        self.powers = {}

    def add_power(self, power: Power, name: str):
        self.powers[name] = power

    def save(self):
        os.makedirs(self.path + self.name, exist_ok=True)
        with open(self.path + self.name + "/pack.mcmeta", "w+") as pack_mcmeta:
            pack_mcmeta.write(json.dumps(self.pack_mcmeta.to_json(), indent=4))

        os.makedirs(os.path.dirname(self.path + self.name + f"/data/{self.namespace}/functions/"), exist_ok=True)
        with open(self.path + self.name + f"/data/{self.namespace}/functions/grant_powers.mcfunction", "w+") as func:
            for name, power in self.powers.items():
                func.write(f"power grant @s {self.namespace}:{name}\n")

        for name, power in self.powers.items():
            os.makedirs(os.path.dirname(self.path + self.name + f"/data/{self.namespace}/powers/{name}.json"), exist_ok=True)
            with open(self.path + self.name + f"/data/{self.namespace}/powers/{name}.json", "w+") as power_file:
                power_file.write(json.dumps(power.to_json(), indent=4))

class Resourcepack:
    def __init__(self, name: str, namespace: str = "minecraft", path: str = "./", pack_mcmeta: PackMcMeta = PackMcMeta()):
        self.name = name
        self.pack_mcmeta = pack_mcmeta
        self.namespace = namespace
        self.path = path
        self.textures = {}

    def add_texture(self, image, name: str):
        self.textures[name] = image

    def add_audio(self, image, name: str):
        self.textures[name] = image

    def save(self):
        os.makedirs(self.path + self.name, exist_ok=True)
        with open(self.path + self.name + "/pack.mcmeta", "w+") as pack_mcmeta:
            pack_mcmeta.write(json.dumps(self.pack_mcmeta.to_json(), indent=4))

        for name, image in self.textures.items():
            os.makedirs(os.path.dirname(self.path + self.name + f"/assets/{self.namespace}/textures/{name}.png"), exist_ok=True)
            image.save(self.path + self.name + f"/assets/{self.namespace}/textures/{name}.png")
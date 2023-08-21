import json
from enum import Enum
from typing import List


class Base:
    def __init__(self):
        return

    def to_json(self):
        non_null = clean_nones(json.loads(json.dumps(self, default=lambda o: get_enum_or_dict(o))))
        return non_null

def clean_nones(value):
    """
    Recursively remove all None values from dictionaries and lists, and returns
    the result as a new dictionary or list.
    """
    if isinstance(value, list):
        return [clean_nones(x) for x in value if x is not None]
    elif isinstance(value, dict):
        return {
            key: clean_nones(val)
            for key, val in value.items()
            if val is not None
        }
    else:
        return value

class Action(Base):
    def __init__(self, type_):
        super().__init__()
        self.type = type_

class Condition(Base):
    def __init__(self, type_):
        super().__init__()
        self.type = type_

class Badge(Base):
    def __init__(self, type_):
        super().__init__()
        self.type = type_


class BientityAction(Action):
    def __init__(self, type_):
        super().__init__(type_)


class BientityCondition(Condition):
    def __init__(self, type_, inverted: bool = False):
        super().__init__(type_)
        self.inverted = inverted


class BiomeCondition(Condition):
    def __init__(self, type_, inverted: bool = False):
        super().__init__(type_)
        self.inverted = inverted


class BlockAction(Action):
    def __init__(self, type_):
        super().__init__(type_)


class BlockCondition(Condition):
    def __init__(self, type_, inverted: bool = False):
        super().__init__(type_)
        self.inverted = inverted


class DamageCondition(Condition):
    def __init__(self, type_, inverted: bool = False):
        super().__init__(type_)
        self.inverted = inverted


class EntityAction(Action):
    def __init__(self, type_):
        super().__init__(type_)


class EntityCondition(Condition):
    def __init__(self, type_, inverted: bool = False):
        super().__init__(type_)
        self.inverted = inverted


class FluidCondition(Condition):
    def __init__(self, type_, inverted: bool = False):
        super().__init__(type_)
        self.inverted = inverted


class ItemAction(Action):
    def __init__(self, type_):
        super().__init__(type_)


class ItemCondition(Condition):
    def __init__(self, type_, inverted: bool = False):
        super().__init__(type_)
        self.inverted = inverted


class Power(Base):
    def __init__(self, type_, name: str = None, description: str = None, hidden: bool = False,
                 condition: EntityCondition = None, loading_priority: int = 0, badges: List[Badge] = None):
        super().__init__()
        self.type = type_
        self.name = name
        self.description = description
        self.hidden = hidden
        self.condition = condition
        self.loading_priority = loading_priority
        self.badges = badges


class DamageSource(Base):
    def __init__(self, name: str, bypasses_armor: bool = False, fire: bool = False, unblockable: bool = False,
                 magic: bool = False, out_of_world: bool = False):
        super().__init__()
        self.name = name
        self.bypasses_armor = bypasses_armor
        self.fire = fire
        self.unblockable = unblockable
        self.magic = magic
        self.out_of_world = out_of_world


class ParticleEffect(Base):
    def __init__(self, type_: str, params: str):
        super().__init__()
        self.type_ = type_
        self.params = params


class Stat(Base):
    def __init__(self, type_: str, id_: str):
        super().__init__()
        self.type_ = type_
        self.id_ = id_


class CraftingRecipe(Base):
    def __init__(self, type_: str, id_: str, result: bool = False):
        super().__init__()
        self.type_ = type_
        self.id_ = id_
        self.result = result


class Ingredient(Base):
    def __init__(self, item: str = None, tag: str = None):
        super().__init__()
        self.item = item
        self.tag = tag


class ItemStack(Base):
    def __init__(self, item: str, amount: int = 1, tag: str = None):
        super().__init__()
        self.item = item
        self.amount = amount
        self.tag = tag


class PositionedItemStack(Base):
    def __init__(self, item: str, amount: int = 1, tag: str = None, slot: int = None):
        super().__init__()
        self.item = item
        self.amount = amount
        self.tag = tag
        self.slot = slot


class StatusEffectInstance(Base):
    def __init__(self, effect: str, duration: int = 100, amplifier: int = 0, is_ambient: bool = False,
                 show_particles: bool = True, show_icon: bool = True):
        super().__init__()
        self.effect = effect
        self.duration = duration
        self.amplifier = amplifier
        self.is_ambient = is_ambient
        self.show_particles = show_particles
        self.show_icon = show_icon


class InventoryType(Base):
    def __init__(self, inventory: str, power: str):
        super().__init__()
        self.inventory = inventory
        self.power = power


class AttributeModifier(Base):
    def __init__(self, operation: "AttributeModifierOperation", value: float, resource: str = None, name: str = None,
                 modifier: "AttributeModifier" = None):
        super().__init__()
        self.operation = operation
        self.value = value
        self.resource = resource
        self.name = name
        self.modifier = modifier


class AttriutedAttributeModifier(Base):
    def __init__(self, attribute: str, operation: "AttributedAttributeModifierOperation", value: float,
                 name: str = None):
        super().__init__()
        self.attribute = attribute
        self.operation = operation
        self.value = value
        self.name = name


class Vector(Base):
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        super().__init__()
        self.x = x
        self.y = y
        self.z = z


class FeatureRenderer(Enum):
    ARMOR = "armor"
    CAPE = "cape"
    CAT_COLLAR = "cat_collar"
    DEADMAU5 = "deadmau5"
    DOLPHIN_HELD_ITEM = "dolphin_held_item"
    DROWNED_OVERLAY = "drowned_overlay"
    ELYTRA = "elytra"
    ENDERMAN_BLOCK = "enderman_block"
    ENERGY_SWIRL_OVERLAY = "energy_swirl_overlay"
    EYES = "eyes"
    FOX_HELD_ITEM = "fox_held_item"
    HEAD = "head"
    HELD_ITEM = "held_item"
    HORSE_ARMOR = "horse_armor"
    HORSE_MARKING = "horse_marking"
    IRON_GOLEM_CRACK = "iron_golem_crack"
    IRON_GOLEM_FLOWER = "iron_golem_flower"
    LLAMA_DECOR = "llama_decor"
    MOOSHROOM_MUSHROOM = "mooshroom_mushroom"
    PANDA_HELD_ITEM = "panda_held_item"
    SADDLE = "saddle"
    SHEEP_WOOL = "sheep_wool"
    SHOULDER_PARROT = "shoulder_parrot"
    SHULKER_HEAD = "shulker_head"
    SLIME_OVERLAY = "slime_overlay"
    SNOWMAN_PUMPKIN = "snowman_pumpkin"
    STRAY_OVERLAY = "stray_overlay"
    STUCK_OBJECTS = "stuck_objects"
    TRIDENT_RIPTIDE = "trident_riptide"
    TROPICAL_FISH_COLOR = "tropical_fish_color"
    VILLAGER_CLOTHING = "villager_clothing"
    VILLAGER_HELD_ITEM = "villager_held_item"
    WOLF_COLLAR = "wolf_collar"


class AttributedAttributeModifierOperation(Enum):
    ADDITION = "addition"
    MULTIPLY_BASE = "multiply_base"
    MULTIPLY_TOTAL = "multiply_total"


class PlayerAbility(Enum):
    FLYING = "minecraft:flying"
    INSTABUILD = "minecraft:instabuild"
    INVULNERABLE = "minecraft:invulnerable"
    MAY_BUILD = "minecraft:mayBuild"
    MAY_FLY = "minecraft:mayfly"


class AttributeModifierOperation(Enum):
    ADD_BASE_EARLY = "add_base_early"
    MULTIPLY_BASE_ADDITIVE = "multiply_base_additive"
    MULTIPLY_BASE_MULTIPLICATIVE = "multiply_base_multiplicative"
    ADD_BASE_LATE = "add_base_late"
    MIN_BASE = "min_base"
    MAX_BASE = "max_base"
    SET_BASE = "set_base"
    MULTIPLY_TOTAL_ADDITIVE = "multiply_total_additive"
    MULTIPLY_TOTAL_MULTIPLICATIVE = "multiply_total_multiplicative"
    MIN_TOTAL = "min_total"
    MAX_TOTAL = "max_total"
    SET_TOTAL = "set_total"


class BiomeCategory(Enum):
    BEACH = "beach"
    DESERT = "desert"
    EXTREME_HILLS = "extreme_hills"
    FOREST = "forest"
    ICY = "icy"
    JUNGLE = "jungle"
    MESA = "mesa"
    MOUNTAIN = "mountain"
    MUSHROOM = "mushroom"
    NETHER = "nether"
    NONE = "none"
    OCEAN = "ocean"
    PLAINS = "plains"
    RIVER = "river"
    SAVANNA = "savanna"
    SWAMP = "swamp"
    TAIGA = "taiga"
    THE_END = "the_end"
    UNDERGROUND = "underground"


class ItemSlot(Enum):
    ARMOR_CHEST = "armor.chest"
    ARMOR_FEET = "armor.feet"
    ARMOR_HEAD = "armor.head"
    ARMOR_LEGS = "armor.legs"
    HORSE_ARMOR = "horse.armor"
    HORSE_SADDLE = "horse.saddle"
    WEAPON_MAINHAND = "weapon.mainhand"
    WEAPON_OFFHAND = "weapon.offhand"
    WEAPON = "weapon"
    CONTAINER_0 = "container.0"
    CONTAINER_1 = "container.1"
    CONTAINER_2 = "container.2"
    CONTAINER_3 = "container.3"
    CONTAINER_4 = "container.4"
    CONTAINER_5 = "container.5"
    CONTAINER_6 = "container.6"
    CONTAINER_7 = "container.7"
    CONTAINER_8 = "container.8"
    CONTAINER_9 = "container.9"
    CONTAINER_10 = "container.10"
    CONTAINER_11 = "container.11"
    CONTAINER_12 = "container.12"
    CONTAINER_13 = "container.13"
    CONTAINER_14 = "container.14"
    CONTAINER_15 = "container.15"
    CONTAINER_16 = "container.16"
    CONTAINER_17 = "container.17"
    CONTAINER_18 = "container.18"
    CONTAINER_19 = "container.19"
    CONTAINER_20 = "container.20"
    CONTAINER_21 = "container.21"
    CONTAINER_22 = "container.22"
    CONTAINER_23 = "container.23"
    CONTAINER_24 = "container.24"
    CONTAINER_25 = "container.25"
    CONTAINER_26 = "container.26"
    CONTAINER_27 = "container.27"
    CONTAINER_28 = "container.28"
    CONTAINER_29 = "container.29"
    CONTAINER_30 = "container.30"
    CONTAINER_31 = "container.31"
    CONTAINER_32 = "container.32"
    CONTAINER_33 = "container.33"
    CONTAINER_34 = "container.34"
    CONTAINER_35 = "container.35"
    CONTAINER_36 = "container.36"
    CONTAINER_37 = "container.37"
    CONTAINER_38 = "container.38"
    CONTAINER_39 = "container.39"
    CONTAINER_40 = "container.40"
    CONTAINER_41 = "container.41"
    CONTAINER_42 = "container.42"
    CONTAINER_43 = "container.43"
    CONTAINER_44 = "container.44"
    CONTAINER_45 = "container.45"
    CONTAINER_46 = "container.46"
    CONTAINER_47 = "container.47"
    CONTAINER_48 = "container.48"
    CONTAINER_49 = "container.49"
    CONTAINER_50 = "container.50"
    CONTAINER_51 = "container.51"
    CONTAINER_52 = "container.52"
    CONTAINER_53 = "container.53"
    ENDERCHEST_0 = "enderchest.0"
    ENDERCHEST_1 = "enderchest.1"
    ENDERCHEST_2 = "enderchest.2"
    ENDERCHEST_3 = "enderchest.3"
    ENDERCHEST_4 = "enderchest.4"
    ENDERCHEST_5 = "enderchest.5"
    ENDERCHEST_6 = "enderchest.6"
    ENDERCHEST_7 = "enderchest.7"
    ENDERCHEST_8 = "enderchest.8"
    ENDERCHEST_9 = "enderchest.9"
    ENDERCHEST_10 = "enderchest.10"
    ENDERCHEST_11 = "enderchest.11"
    ENDERCHEST_12 = "enderchest.12"
    ENDERCHEST_13 = "enderchest.13"
    ENDERCHEST_14 = "enderchest.14"
    ENDERCHEST_15 = "enderchest.15"
    ENDERCHEST_16 = "enderchest.16"
    ENDERCHEST_17 = "enderchest.17"
    ENDERCHEST_18 = "enderchest.18"
    ENDERCHEST_19 = "enderchest.19"
    ENDERCHEST_20 = "enderchest.20"
    ENDERCHEST_21 = "enderchest.21"
    ENDERCHEST_22 = "enderchest.22"
    ENDERCHEST_23 = "enderchest.23"
    ENDERCHEST_24 = "enderchest.24"
    ENDERCHEST_25 = "enderchest.25"
    ENDERCHEST_26 = "enderchest.26"
    HORSE_0 = "horse.0"
    HORSE_1 = "horse.1"
    HORSE_2 = "horse.2"
    HORSE_3 = "horse.3"
    HORSE_4 = "horse.4"
    HORSE_5 = "horse.5"
    HORSE_6 = "horse.6"
    HORSE_7 = "horse.7"
    HORSE_8 = "horse.8"
    HORSE_9 = "horse.9"
    HORSE_10 = "horse.10"
    HORSE_11 = "horse.11"
    HORSE_12 = "horse.12"
    HORSE_13 = "horse.13"
    HORSE_14 = "horse.14"
    HOTBAR_0 = "hotbar.0"
    HOTBAR_1 = "hotbar.1"
    HOTBAR_2 = "hotbar.2"
    HOTBAR_3 = "hotbar.3"
    HOTBAR_4 = "hotbar.4"
    HOTBAR_5 = "hotbar.5"
    HOTBAR_6 = "hotbar.6"
    HOTBAR_7 = "hotbar.7"
    HOTBAR_8 = "hotbar.8"
    INVENTORY_0 = "inventory.0"
    INVENTORY_1 = "inventory.1"
    INVENTORY_2 = "inventory.2"
    INVENTORY_3 = "inventory.3"
    INVENTORY_4 = "inventory.4"
    INVENTORY_5 = "inventory.5"
    INVENTORY_6 = "inventory.6"
    INVENTORY_7 = "inventory.7"
    INVENTORY_8 = "inventory.8"
    INVENTORY_9 = "inventory.9"
    INVENTORY_10 = "inventory.10"
    INVENTORY_11 = "inventory.11"
    INVENTORY_12 = "inventory.12"
    INVENTORY_13 = "inventory.13"
    INVENTORY_14 = "inventory.14"
    INVENTORY_15 = "inventory.15"
    INVENTORY_16 = "inventory.16"
    INVENTORY_17 = "inventory.17"
    INVENTORY_18 = "inventory.18"
    INVENTORY_19 = "inventory.19"
    INVENTORY_20 = "inventory.20"
    INVENTORY_21 = "inventory.21"
    INVENTORY_22 = "inventory.22"
    INVENTORY_23 = "inventory.23"
    INVENTORY_24 = "inventory.24"
    INVENTORY_25 = "inventory.25"
    INVENTORY_26 = "inventory.26"
    VILLAGER_0 = "villager.0"
    VILLAGER_1 = "villager.1"
    VILLAGER_2 = "villager.2"
    VILLAGER_3 = "villager.3"
    VILLAGER_4 = "villager.4"
    VILLAGER_5 = "villager.5"
    VILLAGER_6 = "villager.6"
    VILLAGER_7 = "villager.7"


class Comparison(Enum):
    LESS_THAN = "<"
    LESS_THAN_OR_EQUAL = "<="
    GREATER_THAN = ">"
    GREATER_THAN_OR_EQUAL = ">="
    EQUAL = "=="
    NOT_EQUAL = "!="


class ShapeType(Enum):
    COLLIDER = "collider"
    OUTLINE = "outline"
    VISUAL = "visual"


class FluidHandling(Enum):
    ANY = "any"
    NONE = "none"
    SOURCE_ONLY = "source_only"


class DestructionType(Enum):
    BREAK = "break"
    DESTROY = "destroy"
    NONE = "none"


class ActionResult(Enum):
    CONSUME_PARTIAL = "consume_partial"
    CONSUME = "consume"
    FAIL = "fail"
    PASS = "pass"
    SUCCESS = "success"


class ContainerType(Enum):
    CHEST = "chest"
    HOPPER = "hopper"
    DROPPER = "dropper"
    DISPENSER = "dispenser"
    DOUBLE_CHEST = "double_chest"


class Key(Base):
    def __init__(self, key: str, continuous: bool = False):
        super().__init__()
        self.key = key
        self.continuous = continuous


class HudRender(Base):
    def __init__(self, should_render: bool = True, sprite_location: str = "origins:textures/gui/resource_bar.png",
                 bar_index: int = 0, condition: EntityCondition = None, inverted: bool = False):
        super().__init__()
        self.should_render = should_render
        self.sprite_location = sprite_location
        self.bar_index = bar_index
        self.condition = condition
        self.inverted = inverted


def get_enum_or_dict(o):
    if isinstance(o, Enum):
        return o.value
    else:
        return getattr(o, '__dict__', str(o))


def remove_null(data):
    for key, value in list(data.items()):
        if value is None or value == "None":
            del data[key]
        elif isinstance(value, dict):
            remove_null(value)
    return data  # For convenience

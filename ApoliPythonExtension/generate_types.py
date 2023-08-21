import os
import re
from typing import Union

from blocks import *

pattern = '### *Fields\n*Field *\| *Type *\| *Default *\| *Description\n-+\|-+\|-+\|-+\n([\s\S]*?)\n*### *Examples'

data_type_types = {
    "Integer": int,
    "Float": float,
    "Boolean": bool,
    "String": str,
    "Identifier": str,
    "NBT": str,
    "Text Component": Union[str, dict, List[dict]],
    "Object": dict,
    "Item Slot": ItemSlot,
    "Shape Type": ShapeType,
    "Fluid Handling": FluidHandling,
    "Damage Source": DamageSource,
    "Hud Render": HudRender,
    "Destruction Type": DestructionType,
    "Action Result": ActionResult,
    "Container Type": ContainerType,
    "Crafting Recipe": CraftingRecipe,
    "Comparison": Comparison,
    "Key": Key,
    "Ingredient": Ingredient,
    "Item Stack": ItemStack,
    "Positioned Item Stack": PositionedItemStack,
    "Stat": Stat,
    "Vector": Vector,
    "Particle Effect": ParticleEffect,
    "Player Ability": PlayerAbility,
    "Feature Renderer": FeatureRenderer,
    "Status Effect Instance": StatusEffectInstance,
    "Inventory Type": InventoryType,
    "Biome Category": BiomeCategory,
    "Attribute Modifier": AttributeModifier,
    "Attributed Attribute Modifier": AttriutedAttributeModifier,
    "Badge Type": Badge,
    "Bi-entity Action Type": BientityAction,
    "Bi-entity Condition Type": BientityCondition,
    "Biome Condition Type": BiomeCondition,
    "Block Action Type": BlockAction,
    "Block Condition Type": BlockCondition,
    "Damage Condition Type": DamageCondition,
    "Entity Action Type": EntityAction,
    "Entity Condition Type": EntityCondition,
    "Fluid Condition Type": FluidCondition,
    "Item Action Type": ItemAction,
    "Item Condition Type": ItemCondition,
    "Meta Condition Type": Condition,
    "Meta Action Type": Action,
    "Action": Action,
    "Condition Type": Condition,
    "Power Type": Power
}

def generate_types():
    types = {}
    left_out_types = []
    for directory in os.listdir("../wiki/docs/types/"):
        if not directory.endswith(".md") and directory != "data_types":
            types[directory] = []
            for filename in os.listdir(f"./wiki/docs/types/{directory}"):
                with open("./wiki/docs/types/" + directory + "/" + filename, "r") as read_file:
                    text = read_file.read()
                    power = {}
                    type_id = re.search("Type ID: \`(\S*)\`", text)
                    power["type"] = type_id.group(1) if type_id else ""
                    found_lines = re.search(pattern, text)
                    lines = found_lines.group(1).split("\n") if found_lines else []
                    for line in lines:
                        if line is not None:
                            segments = re.split(" *\| *", line)[0:3]
                            if len(segments) > 2:
                                field = re.search("\`(\S*)\`", segments[0])
                                field_name = field.group(1) if field else ""
                                default_value = segments[2] if segments[2] != "" else None
                                is_optional = True if segments[2] == "_optional_" else False

                                if default_value is not None:
                                    default_value = default_value.replace("`", "")
                                    if default_value == "true" or default_value == "false":
                                        default_value = default_value.capitalize()
                                data_types = re.findall("\[([^]]+)\]", segments[1])
                                data_type = None
                                if len(data_types) > 0:
                                    if data_types[0] == "Array":
                                        if str(data_types[1])[:-1] in data_type_types:
                                            data_type = List[data_type_types[data_types[1][:-1]]]
                                    else:
                                        if data_types[0] in data_type_types:
                                            data_type = data_type_types[data_types[0]]
                                        else:
                                            if data_types[0] not in left_out_types:
                                                left_out_types.append(data_types[0])

                                if field_name != "" and field_name != "type" and data_type is not None:
                                    if default_value is not None and default_value.startswith("{") and default_value.endswith("}"):
                                        default_value = json.loads(default_value)
                                    power[field_name] = {
                                        "type": data_type,
                                        "required": not is_optional,
                                        "default_value": default_value
                                    }
                    types[directory].append(power)

    for sd_type, data in types.items():
        total_text = "from typing import List, Union\n\nfrom blocks import *\n"

        for power in data:
            class_name = ""
            for part in power["type"].split("_"):
                class_name += part.replace("origins:", "").capitalize()
            constructor_args = ""
            constructor_sets = ""
            post_sets = ""
            for key, value in power.items():
                if key != "type":
                    if key == "from" or key == "to" or key == "class":
                        key += "_value"
                    try:
                        value_type = value["type"].__name__
                    except AttributeError as e:
                        value_type = str(value["type"]).replace("blocks.", "").replace("typing.", "")
                    if value["default_value"] is not None:
                        str_value = value["default_value"] if value["default_value"] != "_optional_" and value["default_value"] != "**DEPRECATED**" else None

                        if value_type == "str":
                            if not str(str_value).startswith("\"") and not str(str_value).endswith("\""):
                                str_value = "\"" + str(str_value) + "\""
                        post_sets += ", " + key + ": " + value_type + " = " + str(str_value)
                    else:
                        constructor_args += ", " + key + ": " + value_type
                    constructor_sets += "self." + key + " = " + key + "\n        "
            constructor_args += post_sets
            if sd_type.startswith("meta_"):
                sd_type = sd_type.replace("meta_", "")

            type_name = sd_type.replace("_types", "").replace("_", " ").title().replace(" ", "")

            class_template = f"""
        
    class {class_name}{type_name}({type_name}):
        def __init__(self{constructor_args}, **kw):
            super().__init__("{power["type"]}", **kw)
            {constructor_sets}"""
            total_text += class_template

        with open(f"./types/{sd_type}.py", "w+") as write_file:
            write_file.write(total_text)

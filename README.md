Apoli Python Extension is a python package that allows you to create Datapacks and Resourcepacks using Apoli Powers.

# Example:
```py
"""
Demo of Apoli Python Package

This is a Demo of my Apoli Python Package to see how long it would take to create a relatively large apoli power.

This Power will be a power that applies 3 random status effects whenever you recieve any status effect.
"""

status_effects = [
    "speed", "slowness", "haste", "mining_fatigue",
    "strength", "instant_health", "instant_damage",
    "jump_boost", "nausea", "regeneration",
    "resistance", "fire_resistance", "water_breathing",
    "invisibility", "blindness", "night_vision", "hunger",
    "weakness", "poison", "wither", "health_boost", "absorption",
    "saturation", "glowing", "levitation", "luck", "unluck",
    "slow_falling", "conduit_power", "dolphins_grace",
    "bad_omen", "hero_of_the_village", "darkness",
]

datapack = Datapack(name="Test Demo DataPack", namespace="test_demo")

effect_actions = []

for effect in status_effects:
    effect_actions.append({
        "element": ApplyEffectEntityAction(effect="minecraft:" + effect),
        "weight": 10
    })

effect_action = ChoiceAction(actions=effect_actions)

has_effect = NbtEntityCondition(nbt="{ActiveEffects:[{Ambient:0b}]}")

three_effects = AndAction(actions=[effect_action,effect_action,effect_action])

rising_power = ActionOverTimePower(rising_action=three_effects, condition=has_effect, name="Easily Effected", description="Whenever you gain a potion effect, you gain some random extras")

datapack.add_power(power=rising_power, name="random_effect")

datapack.save()
```
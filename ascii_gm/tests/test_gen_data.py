from ascii_gm.text_generator import generate_text


gen_data = {}
gen_data["warrior"] = [
    "A {gender} {race} warrior, wearing {armor} and wielding {weapon}."
]
gen_data["gender"] = ["male", "female"]
gen_data["race"] = {"1-3": "human", "4-5": "dwarf", "6": "elf"}
gen_data["armor"] = {
    "01-50": "leather armor",
    "51-90": "chainmail",
    "91-00": "plate armor",
}
gen_data["weapon"] = [
    "{melee_weapon}",
    "{melee_weapon} and a shield",
    "twin blades",
    "{ranged_weapon}",
]
gen_data["melee_weapon"] = ["a battleaxe", "a mace", "a spear", "a sword"]
gen_data["ranged_weapon"] = ["a longbow and arrows", "a heavy crossbow"]


def test_generators():
    for key in gen_data.keys():
        assert generate_text(key, gen_data) is not None

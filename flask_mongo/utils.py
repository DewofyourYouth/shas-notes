from flask_mongo import app

GEM_VALS = {
    "gem_edgecases": {"15": "טו", "16": "טז"},
    "gem_ones": [
        "",
        "א",
        "ב",
        "ג",
        "ד",
        "ה",
        "ו",
        "ז",
        "ח",
        "ט",
    ],
    "gem_tens": [
        "",
        "י",
        "כ",
        "ל",
        "מ",
        "נ",
        "ס",
        "ע",
        "פ",
        "צ",
    ],
    "gem_hundreds": [
        "",
        "ק",
        "ר",
        "ש",
        "ת",
        "תק",
        "תר",
        "תש",
        "תת",
        "תתק",
    ],
}


@app.template_filter("gematria")
def convert_to_gematria(num: int) -> str:
    """Converts and int between 1 - 999 to a gematria string

    Args:
        num (int): the number ti convert

    Returns:
        str: The gematria string
    """
    gem_ones, gem_tens, gem_hundreds, gem_edgecases = GEM_VALS["gem_ones"], GEM_VALS["gem_tens"], GEM_VALS["gem_hundreds"], GEM_VALS["gem_edgecases"]
    num_str = str(num)
    nums = [gem_ones, gem_tens, gem_hundreds]
    ans = []
    if num < 10:
        return gem_ones[num]
    if num_str.endswith("15") or num_str.endswith("16"):
        ans.append(gem_edgecases[num_str[-2:]])
        num_str = num_str[:-2]
        nums = nums[2:]

    num_str = num_str[::-1]
    for i, v in enumerate(num_str):
        ans.append(nums[i][int(v)])
    return "".join(ans[::-1])


@app.template_filter("daf_gematria")
def convert_daf_to_gematria(num: int) -> str:
    """Converts the the page number (starting at one) to the daf (starting at beis)

    Args:
        num (int): Page number

    Returns:
        str: The daf as indicated in the Vilna Shas
    """
    num = num + 1
    return convert_to_gematria(num)
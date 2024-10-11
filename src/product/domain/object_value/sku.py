import hashlib


def generate_sku_from_description(sku_description: str) -> str:
    if not sku_description:
        return ''
    _hash = hashlib.md5()
    _hash.update(sku_description.encode('utf-8'))
    return str(int(_hash.hexdigest(), 16))[0:20]

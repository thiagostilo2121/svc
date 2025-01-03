__all__ = [
    "findNewVersion"
]

class VC():
    def __init__(self, x= None) -> None: ...
    def findNewVersion(self, version: int | str, type: str, name: str):
        STB_V = "1.0.0a1"
        STB_Va = "1.0.0a1"
        STB_Vb = None

        if name != "Streak TikTok Bot": return SyntaxError("'name' value is not valid")
        if version != STB_V: return "newVersionAvaliable" and STB_V
        else: "lastestVersion"
import pickle, warnings, json

Hex = "0123456789abcdef"

class FileHandler:
    
    def __init__(self, action, format_, object_):
        self.Action = action
        self.Format = format_
        operation = [self.Action, self.Format]
        
        match operation:
            case ["save" | "SAVE" | "Save", "ugf"]:
                self.Output = self.__ConvertToUGF(object_)
            case ["save" | "SAVE" | "Save", "ugfr"]:
                self.Output = self.__ConvertToUGF(object_, True)
            case ["save" | "SAVE" | "Save", "json"]:
                self.Output = self.__ConvertToJSON(object_)
            case ["save" | "SAVE" | "Save", _]:
                self.Output = object_
            case ["load" | "LOAD" | "Load", "ugf"]:
                self.Output = self.__LoadUGF(object_)
            case ["load" | "LOAD" | "Load", "ugfr"]:
                self.Output = self.__LoadUGF(object_, True)
            case ["load" | "LOAD" | "Load", _]:
                self.Output = open(object_, "r").read()
    
    def __HeaderValid(self, header):
        HeaderItems = "".join(map(chr, header[::-1])).split("/")
        if HeaderItems[0] == "Boris":
            if HeaderItems[1] in "UGF UGFR JSON".split():
                match HeaderItems[2]: # other types will be added later
                    case "Standard0.1":
                        return True
                    case _:
                        return False
            else:
                return False
        elif len(HeaderItems) <= 2:
            return False
        else:
            return False
    
    def __ConvertToUGF(self, content, raw=False):
        charxor = lambda char, val: ord(char) ^ val
        reversehex = lambda num: Hex.index(num[1]) << 4 | Hex.index(num[0])
        if not raw:
            EncodedTags = {
                "header": list(map(ord,"Boris/UGF/Standard0.1"))[::-1],
                "layers": [[[charxor(char, 77) for char in i[0]][::-1], reversehex(i[1][1:3])] for i in content]
            }
            EncodedTags["checksum"] = sum([i[0][0] for i in EncodedTags["layers"]])
        else:
            EncodedTags = {
                "header": list(map(ord,"Boris/UGFR/Standard0.1"))[::-1],
                "layers": content
            }
            EncodedTags["checksum"] = sum([ord(i[0][0]) for i in EncodedTags["layers"]])
        return EncodedTags
    
    def __LoadUGF(self, filename, raw=False):
        with open(filename, "rb") as out:
            Result = pickle.load(out)
        match self.Format:
            case "ugf":
                if sum([i[0][0] for i in Result["layers"]]) != Result["checksum"]:
                    warnings.warn("Checksum does not match", Warning)
                elif not self.__HeaderValid(Result["header"]):
                    raise Exception("Invalid header")
                else:
                    dexor = lambda num, val: num ^ val
                    colour = lambda num: f"[{Hex[num&15]}{Hex[num>>4]}]"
                    DecodedTags = [["".join(map(chr, [dexor(n, 77) for n in i[0]]))[::-1], colour(i[1])] for i in Result["layers"]]
            case "ugfr":
                if sum([ord(i[0][0]) for i in Result["layers"]]) != Result["checksum"]:
                    warnings.warn("Checksum does not match", Warning)
                elif not self.__HeaderValid(Result["header"]):
                    raise Exception("Invalid header")
                else:
                    DecodedTags = Result["layers"]
        return DecodedTags
    
    def __ConvertToJSON(self, content):
        EncodedTags = {
            "header": list(map(ord,"Boris/JSON/Standard0.1"))[::-1],
            "layers": content
        }
        EncodedTags["checksum"] = sum([ord(i[0][0]) for i in EncodedTags["layers"]])
        return EncodedTags
    
    def __LoadJSON(self, filename):
        with open(filename, "r") as out:
            Result = json.load(out)
        if sum([ord(i[0][0]) for i in Result["layers"]]) != Result["checksum"]:
            warnings.warn("Checksum does not match", Warning)
        elif not self.__HeaderValid(Result["header"]):
            raise Exception("Invalid header")
        else:
            DecodedTags = Result["layers"]
        return DecodedTags
    
    def Write(self, filename):
        match self.Format:
            case "ugf" | "ugfr":
                with open(filename, "wb") as out:
                    pickle.dump(self.Output, out)
            case "json":
                with open(filename, "w") as out:
                    json.dump(self.Output, out)
            case _:
                with open(filename, "w") as out:
                    out.write(self.Output)
    
    def Read(self):
        return self.Output

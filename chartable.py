import tkinter as tk, clipboard as cb

def CharTable(root, t):
    return {
        "BasicLatin": [
            [
                tk.Button(master=root, font=("jgs5", 12), text="!", command=lambda: cb.copy("!")),
                tk.Button(master=root, font=("jgs5", 12), text='"', command=lambda: cb.copy('"')),
                tk.Button(master=root, font=("jgs5", 12), text="#", command=lambda: cb.copy("#")),
                tk.Button(master=root, font=("jgs5", 12), text="$", command=lambda: cb.copy("$")),
                tk.Button(master=root, font=("jgs5", 12), text="%", command=lambda: cb.copy("%")),
                tk.Button(master=root, font=("jgs5", 12), text="&", command=lambda: cb.copy("&")),
                tk.Button(master=root, font=("jgs5", 12), text="'", command=lambda: cb.copy("'")),
                tk.Button(master=root, font=("jgs5", 12), text="(", command=lambda: cb.copy("(")),
                tk.Button(master=root, font=("jgs5", 12), text=")", command=lambda: cb.copy(")")),
                tk.Button(master=root, font=("jgs5", 12), text="*", command=lambda: cb.copy("*")),
                tk.Button(master=root, font=("jgs5", 12), text="+", command=lambda: cb.copy("+")),
                tk.Button(master=root, font=("jgs5", 12), text=",", command=lambda: cb.copy(",")),
                tk.Button(master=root, font=("jgs5", 12), text="-", command=lambda: cb.copy("-")),
                tk.Button(master=root, font=("jgs5", 12), text=".", command=lambda: cb.copy(".")),
                tk.Button(master=root, font=("jgs5", 12), text="/", command=lambda: cb.copy("/")),
                tk.Button(master=root, font=("jgs5", 12), text="0", command=lambda: cb.copy("0"))
            ],
            [
                tk.Button(master=root, font=("jgs5", 12), text="1", command=lambda: cb.copy("1")),
                tk.Button(master=root, font=("jgs5", 12), text="2", command=lambda: cb.copy("2")),
                tk.Button(master=root, font=("jgs5", 12), text="3", command=lambda: cb.copy("3")),
                tk.Button(master=root, font=("jgs5", 12), text="4", command=lambda: cb.copy("4")),
                tk.Button(master=root, font=("jgs5", 12), text="5", command=lambda: cb.copy("5")),
                tk.Button(master=root, font=("jgs5", 12), text="6", command=lambda: cb.copy("6")),
                tk.Button(master=root, font=("jgs5", 12), text="7", command=lambda: cb.copy("7")),
                tk.Button(master=root, font=("jgs5", 12), text="8", command=lambda: cb.copy("8")),
                tk.Button(master=root, font=("jgs5", 12), text="9", command=lambda: cb.copy("9")),
                tk.Button(master=root, font=("jgs5", 12), text=":", command=lambda: cb.copy(":")),
                tk.Button(master=root, font=("jgs5", 12), text=";", command=lambda: cb.copy(";")),
                tk.Button(master=root, font=("jgs5", 12), text="<", command=lambda: cb.copy("<")),
                tk.Button(master=root, font=("jgs5", 12), text="=", command=lambda: cb.copy("=")),
                tk.Button(master=root, font=("jgs5", 12), text=">", command=lambda: cb.copy(">")),
                tk.Button(master=root, font=("jgs5", 12), text="?", command=lambda: cb.copy("?")),
                tk.Button(master=root, font=("jgs5", 12), text="@", command=lambda: cb.copy("@"))
            ],
            [
                tk.Button(master=root, font=("jgs5", 12), text="A", command=lambda: cb.copy("A")),
                tk.Button(master=root, font=("jgs5", 12), text="B", command=lambda: cb.copy("B")),
                tk.Button(master=root, font=("jgs5", 12), text="C", command=lambda: cb.copy("C")),
                tk.Button(master=root, font=("jgs5", 12), text="D", command=lambda: cb.copy("D")),
                tk.Button(master=root, font=("jgs5", 12), text="E", command=lambda: cb.copy("E")),
                tk.Button(master=root, font=("jgs5", 12), text="F", command=lambda: cb.copy("F")),
                tk.Button(master=root, font=("jgs5", 12), text="G", command=lambda: cb.copy("G")),
                tk.Button(master=root, font=("jgs5", 12), text="H", command=lambda: cb.copy("H")),
                tk.Button(master=root, font=("jgs5", 12), text="I", command=lambda: cb.copy("I")),
                tk.Button(master=root, font=("jgs5", 12), text="J", command=lambda: cb.copy("J")),
                tk.Button(master=root, font=("jgs5", 12), text="K", command=lambda: cb.copy("K")),
                tk.Button(master=root, font=("jgs5", 12), text="L", command=lambda: cb.copy("L")),
                tk.Button(master=root, font=("jgs5", 12), text="M", command=lambda: cb.copy("M")),
                tk.Button(master=root, font=("jgs5", 12), text="N", command=lambda: cb.copy("N")),
                tk.Button(master=root, font=("jgs5", 12), text="O", command=lambda: cb.copy("O")),
                tk.Button(master=root, font=("jgs5", 12), text="P", command=lambda: cb.copy("P"))
            ],
            [
                tk.Button(master=root, font=("jgs5", 12), text="Q", command=lambda: cb.copy("Q")),
                tk.Button(master=root, font=("jgs5", 12), text="R", command=lambda: cb.copy("R")),
                tk.Button(master=root, font=("jgs5", 12), text="S", command=lambda: cb.copy("S")),
                tk.Button(master=root, font=("jgs5", 12), text="T", command=lambda: cb.copy("T")),
                tk.Button(master=root, font=("jgs5", 12), text="U", command=lambda: cb.copy("U")),
                tk.Button(master=root, font=("jgs5", 12), text="V", command=lambda: cb.copy("V")),
                tk.Button(master=root, font=("jgs5", 12), text="W", command=lambda: cb.copy("W")),
                tk.Button(master=root, font=("jgs5", 12), text="X", command=lambda: cb.copy("X")),
                tk.Button(master=root, font=("jgs5", 12), text="Y", command=lambda: cb.copy("Y")),
                tk.Button(master=root, font=("jgs5", 12), text="Z", command=lambda: cb.copy("Z")),
                tk.Button(master=root, font=("jgs5", 12), text="[", command=lambda: cb.copy("[")),
                tk.Button(master=root, font=("jgs5", 12), text="\\", command=lambda: cb.copy("\\")),
                tk.Button(master=root, font=("jgs5", 12), text="]", command=lambda: cb.copy("]")),
                tk.Button(master=root, font=("jgs5", 12), text="^", command=lambda: cb.copy("^")),
                tk.Button(master=root, font=("jgs5", 12), text="_", command=lambda: cb.copy("_")),
                tk.Button(master=root, font=("jgs5", 12), text="`", command=lambda: cb.copy("`"))
            ],
            [
                tk.Button(master=root, font=("jgs5", 12), text="a", command=lambda: cb.copy("a")),
                tk.Button(master=root, font=("jgs5", 12), text="b", command=lambda: cb.copy("b")),
                tk.Button(master=root, font=("jgs5", 12), text="c", command=lambda: cb.copy("c")),
                tk.Button(master=root, font=("jgs5", 12), text="d", command=lambda: cb.copy("d")),
                tk.Button(master=root, font=("jgs5", 12), text="e", command=lambda: cb.copy("e")),
                tk.Button(master=root, font=("jgs5", 12), text="f", command=lambda: cb.copy("f")),
                tk.Button(master=root, font=("jgs5", 12), text="g", command=lambda: cb.copy("g")),
                tk.Button(master=root, font=("jgs5", 12), text="h", command=lambda: cb.copy("h")),
                tk.Button(master=root, font=("jgs5", 12), text="i", command=lambda: cb.copy("i")),
                tk.Button(master=root, font=("jgs5", 12), text="j", command=lambda: cb.copy("j")),
                tk.Button(master=root, font=("jgs5", 12), text="k", command=lambda: cb.copy("k")),
                tk.Button(master=root, font=("jgs5", 12), text="l", command=lambda: cb.copy("l")),
                tk.Button(master=root, font=("jgs5", 12), text="m", command=lambda: cb.copy("m")),
                tk.Button(master=root, font=("jgs5", 12), text="n", command=lambda: cb.copy("n")),
                tk.Button(master=root, font=("jgs5", 12), text="o", command=lambda: cb.copy("o")),
                tk.Button(master=root, font=("jgs5", 12), text="p", command=lambda: cb.copy("p"))
            ],
            [
                tk.Button(master=root, font=("jgs5", 12), text="q", command=lambda: cb.copy("q")),
                tk.Button(master=root, font=("jgs5", 12), text="r", command=lambda: cb.copy("r")),
                tk.Button(master=root, font=("jgs5", 12), text="s", command=lambda: cb.copy("s")),
                tk.Button(master=root, font=("jgs5", 12), text="t", command=lambda: cb.copy("t")),
                tk.Button(master=root, font=("jgs5", 12), text="u", command=lambda: cb.copy("u")),
                tk.Button(master=root, font=("jgs5", 12), text="v", command=lambda: cb.copy("v")),
                tk.Button(master=root, font=("jgs5", 12), text="w", command=lambda: cb.copy("w")),
                tk.Button(master=root, font=("jgs5", 12), text="x", command=lambda: cb.copy("x")),
                tk.Button(master=root, font=("jgs5", 12), text="y", command=lambda: cb.copy("y")),
                tk.Button(master=root, font=("jgs5", 12), text="z", command=lambda: cb.copy("z")),
                tk.Button(master=root, font=("jgs5", 12), text="{", command=lambda: cb.copy("{")),
                tk.Button(master=root, font=("jgs5", 12), text="|", command=lambda: cb.copy("|")),
                tk.Button(master=root, font=("jgs5", 12), text="}", command=lambda: cb.copy("}")),
                tk.Button(master=root, font=("jgs5", 12), text="~", command=lambda: cb.copy("~"))
            ]
        ],
        "AdditionalChar": [
            [
                tk.Button(master=root, font=("jgs5", 12), text="¡", command=lambda: cb.copy("¡")),
                tk.Button(master=root, font=("jgs5", 12), text="¢", command=lambda: cb.copy("¢")),
                tk.Button(master=root, font=("jgs5", 12), text="£", command=lambda: cb.copy("£")),
                tk.Button(master=root, font=("jgs5", 12), text="¤", command=lambda: cb.copy("¤")),
                tk.Button(master=root, font=("jgs5", 12), text="¥", command=lambda: cb.copy("¥")),
                tk.Button(master=root, font=("jgs5", 12), text="¦", command=lambda: cb.copy("¦")),
                tk.Button(master=root, font=("jgs5", 12), text="§", command=lambda: cb.copy("§")),
                tk.Button(master=root, font=("jgs5", 12), text="¨", command=lambda: cb.copy("¨")),
                tk.Button(master=root, font=("jgs5", 12), text="©", command=lambda: cb.copy("©")),
                tk.Button(master=root, font=("jgs5", 12), text="ª", command=lambda: cb.copy("ª")),
                tk.Button(master=root, font=("jgs5", 12), text="«", command=lambda: cb.copy("«")),
                tk.Button(master=root, font=("jgs5", 12), text="¬", command=lambda: cb.copy("¬")),
                tk.Button(master=root, font=("jgs5", 12), text="®", command=lambda: cb.copy("®")),
                tk.Button(master=root, font=("jgs5", 12), text="¯", command=lambda: cb.copy("¯")),
                tk.Button(master=root, font=("jgs5", 12), text="°", command=lambda: cb.copy("°")),
                tk.Button(master=root, font=("jgs5", 12), text="±", command=lambda: cb.copy("±"))
            ],
            [
                tk.Button(master=root, font=("jgs5", 12), text="²", command=lambda: cb.copy("²")),
                tk.Button(master=root, font=("jgs5", 12), text="³", command=lambda: cb.copy("³")),
                tk.Button(master=root, font=("jgs5", 12), text="´", command=lambda: cb.copy("´")),
                tk.Button(master=root, font=("jgs5", 12), text="µ", command=lambda: cb.copy("µ")),
                tk.Button(master=root, font=("jgs5", 12), text="¶", command=lambda: cb.copy("¶")),
                tk.Button(master=root, font=("jgs5", 12), text="·", command=lambda: cb.copy("·")),
                tk.Button(master=root, font=("jgs5", 12), text="¸", command=lambda: cb.copy("¸")),
                tk.Button(master=root, font=("jgs5", 12), text="¹", command=lambda: cb.copy("¹")),
                tk.Button(master=root, font=("jgs5", 12), text="º", command=lambda: cb.copy("º")),
                tk.Button(master=root, font=("jgs5", 12), text="»", command=lambda: cb.copy("»")),
                tk.Button(master=root, font=("jgs5", 12), text="¼", command=lambda: cb.copy("¼")),
                tk.Button(master=root, font=("jgs5", 12), text="½", command=lambda: cb.copy("½")),
                tk.Button(master=root, font=("jgs5", 12), text="¾", command=lambda: cb.copy("¾")),
                tk.Button(master=root, font=("jgs5", 12), text="¿", command=lambda: cb.copy("¿")),
                tk.Button(master=root, font=("jgs5", 12), text="À", command=lambda: cb.copy("À")),
                tk.Button(master=root, font=("jgs5", 12), text="Á", command=lambda: cb.copy("Á"))
            ],
            [
                tk.Button(master=root, font=("jgs5", 12), text="Â", command=lambda: cb.copy("Â")),
                tk.Button(master=root, font=("jgs5", 12), text="Ã", command=lambda: cb.copy("Ã")),
                tk.Button(master=root, font=("jgs5", 12), text="Ä", command=lambda: cb.copy("Ä")),
                tk.Button(master=root, font=("jgs5", 12), text="Å", command=lambda: cb.copy("Å")),
                tk.Button(master=root, font=("jgs5", 12), text="Æ", command=lambda: cb.copy("Æ")),
                tk.Button(master=root, font=("jgs5", 12), text="Ç", command=lambda: cb.copy("Ç")),
                tk.Button(master=root, font=("jgs5", 12), text="È", command=lambda: cb.copy("È")),
                tk.Button(master=root, font=("jgs5", 12), text="É", command=lambda: cb.copy("É")),
                tk.Button(master=root, font=("jgs5", 12), text="Ê", command=lambda: cb.copy("Ê")),
                tk.Button(master=root, font=("jgs5", 12), text="Ë", command=lambda: cb.copy("Ë")),
                tk.Button(master=root, font=("jgs5", 12), text="Ì", command=lambda: cb.copy("Ì")),
                tk.Button(master=root, font=("jgs5", 12), text="Í", command=lambda: cb.copy("Í")),
                tk.Button(master=root, font=("jgs5", 12), text="Î", command=lambda: cb.copy("Î")),
                tk.Button(master=root, font=("jgs5", 12), text="Ï", command=lambda: cb.copy("Ï")),
                tk.Button(master=root, font=("jgs5", 12), text="Ð", command=lambda: cb.copy("Ð")),
                tk.Button(master=root, font=("jgs5", 12), text="Ñ", command=lambda: cb.copy("Ñ"))
            ],
            [
                tk.Button(master=root, font=("jgs5", 12), text="ã", command=lambda: cb.copy("ã")),
                tk.Button(master=root, font=("jgs5", 12), text="ä", command=lambda: cb.copy("ä")),
                tk.Button(master=root, font=("jgs5", 12), text="å", command=lambda: cb.copy("å")),
                tk.Button(master=root, font=("jgs5", 12), text="æ", command=lambda: cb.copy("æ")),
                tk.Button(master=root, font=("jgs5", 12), text="ç", command=lambda: cb.copy("ç")),
                tk.Button(master=root, font=("jgs5", 12), text="è", command=lambda: cb.copy("è")),
                tk.Button(master=root, font=("jgs5", 12), text="é", command=lambda: cb.copy("é")),
                tk.Button(master=root, font=("jgs5", 12), text="ê", command=lambda: cb.copy("ê")),
                tk.Button(master=root, font=("jgs5", 12), text="ë", command=lambda: cb.copy("ë")),
                tk.Button(master=root, font=("jgs5", 12), text="ì", command=lambda: cb.copy("ì")),
                tk.Button(master=root, font=("jgs5", 12), text="í", command=lambda: cb.copy("í")),
                tk.Button(master=root, font=("jgs5", 12), text="î", command=lambda: cb.copy("î")),
                tk.Button(master=root, font=("jgs5", 12), text="ï", command=lambda: cb.copy("ï")),
                tk.Button(master=root, font=("jgs5", 12), text="ð", command=lambda: cb.copy("ð")),
                tk.Button(master=root, font=("jgs5", 12), text="ñ", command=lambda: cb.copy("ñ")),
                tk.Button(master=root, font=("jgs5", 12), text="ò", command=lambda: cb.copy("ò"))
            ],
            [
                tk.Button(master=root, font=("jgs5", 12), text="ó", command=lambda: cb.copy("ó")),
                tk.Button(master=root, font=("jgs5", 12), text="ô", command=lambda: cb.copy("ô")),
                tk.Button(master=root, font=("jgs5", 12), text="õ", command=lambda: cb.copy("õ")),
                tk.Button(master=root, font=("jgs5", 12), text="ö", command=lambda: cb.copy("ö")),
                tk.Button(master=root, font=("jgs5", 12), text="÷", command=lambda: cb.copy("÷")),
                tk.Button(master=root, font=("jgs5", 12), text="ø", command=lambda: cb.copy("ø")),
                tk.Button(master=root, font=("jgs5", 12), text="ù", command=lambda: cb.copy("ù")),
                tk.Button(master=root, font=("jgs5", 12), text="ú", command=lambda: cb.copy("ú")),
                tk.Button(master=root, font=("jgs5", 12), text="û", command=lambda: cb.copy("û")),
                tk.Button(master=root, font=("jgs5", 12), text="ü", command=lambda: cb.copy("ü")),
                tk.Button(master=root, font=("jgs5", 12), text="ý", command=lambda: cb.copy("ý")),
                tk.Button(master=root, font=("jgs5", 12), text="þ", command=lambda: cb.copy("þ")),
                tk.Button(master=root, font=("jgs5", 12), text="ÿ", command=lambda: cb.copy("ÿ")),
                tk.Button(master=root, font=("jgs5", 12), text="‼", command=lambda: cb.copy("‼"))
            ]
        ],
        "GlyphSemigraph": [
            [
                tk.Button(master=root, font=("jgs5", 12), text="←", command=lambda: cb.copy("←")),
                tk.Button(master=root, font=("jgs5", 12), text="↑", command=lambda: cb.copy("↑")),
                tk.Button(master=root, font=("jgs5", 12), text="→", command=lambda: cb.copy("→")),
                tk.Button(master=root, font=("jgs5", 12), text="↓", command=lambda: cb.copy("↓")),
                tk.Button(master=root, font=("jgs5", 12), text="↔", command=lambda: cb.copy("↔")),
                tk.Button(master=root, font=("jgs5", 12), text="↕", command=lambda: cb.copy("↕")),
                tk.Button(master=root, font=("jgs5", 12), text="↨", command=lambda: cb.copy("↨"))
            ],
            [
                tk.Button(master=root, font=("jgs5", 12), text="▁", command=lambda: cb.copy("▁")),
                tk.Button(master=root, font=("jgs5", 12), text="▂", command=lambda: cb.copy("▂")),
                tk.Button(master=root, font=("jgs5", 12), text="▃", command=lambda: cb.copy("▃")),
                tk.Button(master=root, font=("jgs5", 12), text="▄", command=lambda: cb.copy("▄")),
                tk.Button(master=root, font=("jgs5", 12), text="▅", command=lambda: cb.copy("▅")),
                tk.Button(master=root, font=("jgs5", 12), text="▆", command=lambda: cb.copy("▆")),
                tk.Button(master=root, font=("jgs5", 12), text="▇", command=lambda: cb.copy("▇")),
                tk.Button(master=root, font=("jgs5", 12), text="█", command=lambda: cb.copy("█")),
                tk.Button(master=root, font=("jgs5", 12), text="░", command=lambda: cb.copy("░")),
                tk.Button(master=root, font=("jgs5", 12), text="▒", command=lambda: cb.copy("▒")),
                tk.Button(master=root, font=("jgs5", 12), text="▓", command=lambda: cb.copy("▓"))
            ],
            [
                tk.Button(master=root, font=("jgs5", 12), text="▀", command=lambda: cb.copy("▀")),
                tk.Button(master=root, font=("jgs5", 12), text="▄", command=lambda: cb.copy("▄")),
                tk.Button(master=root, font=("jgs5", 12), text="▌", command=lambda: cb.copy("▌")),
                tk.Button(master=root, font=("jgs5", 12), text="▐", command=lambda: cb.copy("▐")),
                tk.Button(master=root, font=("jgs5", 12), text="▚", command=lambda: cb.copy("▚")),
                tk.Button(master=root, font=("jgs5", 12), text="▞", command=lambda: cb.copy("▞")),
                tk.Button(master=root, font=("jgs5", 12), text="▙", command=lambda: cb.copy("▙")),
                tk.Button(master=root, font=("jgs5", 12), text="▛", command=lambda: cb.copy("▛")),
                tk.Button(master=root, font=("jgs5", 12), text="▜", command=lambda: cb.copy("▜")),
                tk.Button(master=root, font=("jgs5", 12), text="▟", command=lambda: cb.copy("▟")),
                tk.Button(master=root, font=("jgs5", 12), text="█", command=lambda: cb.copy("█")),
            ],
            [
                tk.Button(master=root, font=("jgs5", 12), text="▲", command=lambda: cb.copy("▲")),
                tk.Button(master=root, font=("jgs5", 12), text="▶", command=lambda: cb.copy("▶")),
                tk.Button(master=root, font=("jgs5", 12), text="▼", command=lambda: cb.copy("▼")),
                tk.Button(master=root, font=("jgs5", 12), text="◀", command=lambda: cb.copy("◀")),
                tk.Button(master=root, font=("jgs5", 12), text="○", command=lambda: cb.copy("○")),
                tk.Button(master=root, font=("jgs5", 12), text="◘", command=lambda: cb.copy("◘"))
            ],
            [
                tk.Button(master=root, font=("jgs5", 12), text="◙", command=lambda: cb.copy("◙")),
                tk.Button(master=root, font=("jgs5", 12), text="☺", command=lambda: cb.copy("☺")),
                tk.Button(master=root, font=("jgs5", 12), text="☻", command=lambda: cb.copy("☻")),
                tk.Button(master=root, font=("jgs5", 12), text="☼", command=lambda: cb.copy("☼")),
                tk.Button(master=root, font=("jgs5", 12), text="♀", command=lambda: cb.copy("♀")),
                tk.Button(master=root, font=("jgs5", 12), text="♂", command=lambda: cb.copy("♂")),
                tk.Button(master=root, font=("jgs5", 12), text="♠", command=lambda: cb.copy("♠")),
                tk.Button(master=root, font=("jgs5", 12), text="♣", command=lambda: cb.copy("♣")),
                tk.Button(master=root, font=("jgs5", 12), text="♥", command=lambda: cb.copy("♥")),
                tk.Button(master=root, font=("jgs5", 12), text="♦", command=lambda: cb.copy("♦")),
                tk.Button(master=root, font=("jgs5", 12), text="♩", command=lambda: cb.copy("♩")),
                tk.Button(master=root, font=("jgs5", 12), text="♫", command=lambda: cb.copy("♫"))
            ],
            [
                tk.Button(master=root, font=("jgs5", 12), text="◢", command=lambda: cb.copy("◢")),
                tk.Button(master=root, font=("jgs5", 12), text="◣", command=lambda: cb.copy("◣")),
                tk.Button(master=root, font=("jgs5", 12), text="◤", command=lambda: cb.copy("◤")),
                tk.Button(master=root, font=("jgs5", 12), text="◥", command=lambda: cb.copy("◥")),
                tk.Button(master=root, font=("jgs5", 12), text="●", command=lambda: cb.copy("●")),
                tk.Button(master=root, font=("jgs5", 12), text="◖", command=lambda: cb.copy("◖")),
                tk.Button(master=root, font=("jgs5", 12), text="◗", command=lambda: cb.copy("◗"))
            ]
        ]
    }[t]

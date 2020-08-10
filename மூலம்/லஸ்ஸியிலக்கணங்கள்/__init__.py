from .வாடிக்கையாளர் import நிரல்மொழிகள்


def தொகுத்தல்():
    return நிரல்மொழிகள்.தொகுத்தல்()


def இலக்கணம்_பேற(நிரல்மொழி, மொழி=None, எண்ணுரு=None, பதிப்பு=None):
    return '\n'.join(நிரல்மொழிகள்.இலக்கணம்_விதிகள்(நிரல்மொழி, மொழி=மொழி, எண்ணுரு=எண்ணுரு, பதிப்பு=பதிப்பு))


"""
சிறப்பு சொற்கள் (Keywords):
1.- : "பதிப்பி" வாக்கியம் (PRINT)
2.- : "நிறுத்து" வாக்கியம் (BREAK)
3.- : "தொடர்" வாக்கியம் (CONTINUE)
4.- : "பின்கொடு" வாக்கியம் (RETURN)
5.- : "ஆனால்", "இல்லைஆனால்", "இல்லை" வாக்கியம் (IF-ELSEIF-ELSE)
ஏதேனில்: ELSE
6.- : "முடி" வாக்கியம் (END)
7.- : "நிரல்பாகம்" வாக்கியம் (FUNCTION)
8.- : "வரை" வாக்கியம் (WHILE)
9.- : "ஆக","முடியேனில்" வாக்கியம் (DO-WHILE)
10.- : "தேர்ந்தெடு" வாக்கியம் (SELECT)
11.- : "தேர்வு" வாக்கியம் (CASE)
12.- : "ஒவ்வொன்றாக" வாக்கியம் (FOR-EACH)
https://github.com/Ezhil-Language-Foundation/Ezhil-Lang/blob/master/ezhil/ezhil_scanner.py
"""

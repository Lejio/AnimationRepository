from PySide6.QtGui import QColor

def borderColor(r, g, b, a=255):
    
    return f"""
border: 1px solid rgba({r}, {g}, {b}, {a});
"""

# def BgColor(r, g, b, a=255):
    
#     return f"""
# border: 3px solid rgba(143, 184, 237, 255);
# border-radius: 3px;
# background-color: rgba({r}, {g}, {b}, {a});
# """

def Style(c: QColor):
    
    return f"""
border: 3px solid rgba(143, 184, 237, 255);
border-radius: 3px;
background-color: rgba({c.red()}, {c.green()}, {c.blue()}, {c.alpha()});
"""


def styleCombiner(properties: list):
    
    style = ""
    
    for item in properties:
        
        style += item
        
    return style
"""Provides conversion dictionaries between languages"""

LANGS = ["asy", "tikz"]
CMDS = {
    "Intersect": "intersectionpoints",
    "Tangent": "tangents",
}

TYPES = {
    # Expression types
    "Point": "pair",
    "Numeric": "real",
    "Function": "path",
    # Command types
    "Circle": "circle",
    "Polygon": "path",
    "Intersect": "pair",
    "Tangent": "line[]",
    "AngularBisector": "line[]",
    "PerpendicularBisector": "line",
    "PerpendicularLine": "line",
}

JOINERS = [
    ["Polygon", "Segment"],
    ["Bezier"]
]

LINE_STYLE = {
    0: None,  # Default
    10: 'linetype("4 4")',
    15: 'dashed',
    20: 'dotted',
    25: 'dashdotted',
    30: 'linetype("8 4 0 4")',
}

LINE_WT = {
    1: 0.6,
    2: None,  # This is default
    3: 1.0,
    4: 1.2,
    5: 1.4,
    6: 1.6,
        7: 1.8
}

class GeoObj:
    """Represenation of geometric objects
    object is referenced in another command, and hence needs to be declared.
    Defaults to 0.  label: the label of the object.  color: the color the
    object should be drawn.  This applies to paths.  thick: specifies the
    object should be drawn with linewidth(x).  style: dashed, dotted,
    linestyle("4 4"), etc.  ggb_obj_type: the geogebra object type; e.g.
    "segment", "conic" asy_obj_type: the object type that should be declared;
    e.g. "pair", "path", etc.  needs_label: whether the object should be
    labelled in the actual diagram.  needs_pen: 1 if any of the attributes
    {color, thick, style} are not the default values, and 0 otherwise.  """

    # Essential attributes
    lang = 'asy' # Default language to translate to
    geotype = None # Default datatype
    out = None # Output argument
    inp = None # Input arguments
    cmd = None # command name
    index = 0 # for multiple output commands

    # Styling attributes
    isVisible = 1
    hasLabel = 1
    color = None  # Specify as RGB floats [.2, .4, .1]
    line_weight = None
    line_style = None  # dashed, etc.

    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    def __repr__(self):
        return "%s%s=%s%s" % (self.get_type(), self.out_args, self.get_cmd(), self.compose_args())

    def compose_args(self):
        """Returns function output in LANG"""
        if self.obj_type in JOINERS[0]:
            return "--".join(self.inp_args)
        if self.obj_type in JOINERS[1]:
            return "..".join(self.inp_args)
        return "("+",".join(self.inp_args)+")"

    def get_type(self):
        """Returns type of an object"""
        if self.obj_type is None or GeoObj.LANG not in LANGS:
            return ""
        if self.obj_type not in TYPES:
            return self.obj_type+" "
        return TYPES[self.obj_type]+" "

    def get_cmd(self):
        """Returns function used in LANG"""
        if self.cmd not in CMDS or GeoObj.LANG not in LANGS:
            return cmd.lower()
        return CMDS[self.cmd]

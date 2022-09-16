""" MED STT.txt ingest script data structures include
"""
def DataStructuresFunction():

    Shop_Section_Names_List = [
        "Chandelier Earrings",
        "Clip On Earrings",
        "Cuff and Wrap Earrings",
        "Dangle and Drop Earrings",
        "Ear Jackets",
        "Hoop Earrings",
        "Screwback Earrings",
        "Stud Earrings",
        "Threader Earrings",
        "French Hooks",
        "Single Earrings",
        "Stud Dangles",
    ]

    Shop_Section_IDs_List = []

    TagsParametersList = [
        "Theme1",
        "Theme2",
        "Style",
        "era",
        "Color1",
        "Color2",
        "Gemstone1",
        "Gemstone2",
        "Metal1",
        "Metal2",
        "Mineral1",
        "Mineral2",
        "Material1",
        "Material2",
        "Wearer1",
        "Wearer2",
        "Occasion1",
        "Occasion2",
        "Character1",
        "Character2",
        "Brand1",
        "Brand2",
        "Tag1",
        "Tag2",
    ]

    MaterialsParametersList = [
        "Gemstone1",
        "Gemstone2",
        "Metal1",
        "Metal2",
        "Mineral1",
        "Mineral2",
        "Material1",
        "Material2",
    ]

    EtsyDescriptionParametersList = [
        "Type",
        "Style",
        "Theme1",
        "Theme2",
        "Style",
        "era",
        "Color1",
        "Color2",
        "Gemstone1",
        "Gemstone2",
        "Metal1",
        "Metal2",
        "Mineral1",
        "Mineral2",
        "Material1",
        "Material2",
        "Wearer1",
        "Wearer2",
        "Occasion1",
        "Occasion2",
        "Character1",
        "Character2",
        "Brand1",
        "Brand2",
        "Tag1",
        "Tag2",
        "Gemstone1",
        "Gemstone2",
        "Metal1",
        "Metal2",
        "Mineral1",
        "Mineral2",
        "Material1",
        "Material2",
    ]

    Earring_Parameters_Dict = {
        "PR": "Price",
        "PT": "PriceTier",
        "QT": "Quantity",
        "TT": "Title",
        "DL": "Description",
        "DS": "ShortDescription",
        "TY": "Type",
        "C1": "Color1",
        "see one": "Color1",
        "sea one": "Color1",
        "C2": "Color2",
        "C to": "Color2",
        "C too": "Color2",
        "C two": "Color2",
        "sea two": "Color2",
        "see two": "Color2",
        "ME1": "Metal1",
        "ME 1": "Metal1",
        "ME one": "Metal1",
        "Me1": "Metal1",
        "ME2": "Metal2",
        "ME 2": "Metal2",
        "ME to": "Metal2",
        "ME too": "Metal2",
        "ME two": "Metal2",
        "Me2": "Metal2",
        "GE1": "Gemstone1",
        "GE 1": "Gemstone1",
        "GE one": "Gemstone1",
        "Ge1": "Gemstone1",
        "GE2": "Gemstone2",
        "GE 2": "Gemstone2",
        "GE to": "Gemstone2",
        "GE too": "Gemstone2",
        "GE two": "Gemstone2",
        "Ge2": "Gemstone2",
        "MA1": "Material1",
        "MA 1": "Material1",
        "MA one": "Material1",
        "M A1": "Material1",
        "Ma1": "Material1",
        "MA2": "Material2",
        "MA 2": "Material2",
        "MA to": "Material2",
        "MA too": "Material2",
        "MA two": "Material2",
        "Ma2": "Material2",
        "MI1": "Mineral1",
        "MI 1": "Mineral1",
        "MI one": "Mineral1",
        "Mi1": "Mineral1",
        "MI2": "Mineral2",
        "MI 2": "Mineral2",
        "MI to": "Mineral2",
        "MI too": "Mineral2",
        "MI two": "Mineral2",
        "Mi2": "Mineral2",
        "DH": "Height",
        "DW": "Width",
        "DD": "Diameter",
        "ER": "Era",
        "ERA": "Era",
        "era": "Era",
        "CN": "Condition",
        "ST": "Style",
        "WE1": "Wearer1",
        "WE 1": "Wearer1",
        "WE one": "Wearer1",
        "We1": "Wearer1",
        "WE2": "Wearer2",
        "WE 2": "Wearer2",
        "WE to": "Wearer2",
        "WE too": "Wearer2",
        "WE two": "Wearer2",
        "We2": "Wearer2",
        "TH1": "Theme1",
        "TH 1": "Theme1",
        "TH one": "Theme1",
        "Th1": "Theme11",
        "TH2": "Theme2",
        "TH 2": "Theme2",
        "TH to": "Theme2",
        "TH too": "Theme2",
        "TH two": "Theme2",
        "Th2": "Theme2",
        "OC1": "Occasion1",
        "OC 1": "Occasion1",
        "OC one": "Occasion1",
        "Oc1": "Occasion1",
        "OC2": "Occasion2",
        "OC 2": "Occasion2",
        "OC to": "Occasion2",
        "OC too": "Occasion2",
        "OC two": "Occasion2",
        "Oc2": "Occasion2",
        "CH1": "Character1",
        "CH 1": "Character1",
        "CH one": "Character1",
        "Ch1": "Character1",
        "CH2": "Character2",
        "CH 2": "Character2",
        "CH to": "Character2",
        "CH too": "Character2",
        "CH two": "Character2",
        "Ch2": "Character2",
        "BR1": "Brand1",
        "BR 1": "Brand1",
        "BR one": "Brand1",
        "Br1": "Brand1",
        "BR2": "Brand2",
        "BR 2": "Brand2",
        "BR to": "Brand2",
        "BR too": "Brand2",
        "BR two": "Brand2",
        "Br2": "Brand2",
        "SH1": "Shape1",
        "SH 1": "Shape1",
        "SH one": "Shape1",
        "Sh1": "Shape1",
        "SH2": "Shape2",
        "SH 2": "Shape2",
        "SH to": "Shape2",
        "SH too": "Shape2",
        "SH two": "Shape2",
        "Sh2": "Shape2",
        "TG1": "Tag1",
        "TG 1": "Tag1",
        "TG one": "Tag1",
        "TG one": "Tag1",
        "Tg1": "Tag1",
        "TG2": "Tag2",
        "TG 2": "Tag2",
        "TG to": "Tag2",
        "TG too": "Tag2",
        "TG two": "Tag2",
        "Tg2": "Tag2",
    }

    Current_Item_Parameters_Dict = {
        "Price": "",
        "PriceTier": "",
        "Quantity": "",
        "Title": "",
        "Description": "",
        "ShortDescription": "",
        "Type": "",
        "Color1": "",
        "Color2": "",
        "Metal1": "",
        "Metal2": "",
        "Gemstone1": "",
        "Gemstone2": "",
        "Material1": "",
        "Material2": "",
        "Mineral1": "",
        "Mineral2": "",
        "Height": "",
        "Width": "",
        "Diameter": "",
        "Era": "",
        "era": "",
        "Condition": "",
        "Style": "",
        "Wearer1": "",
        "Wearer2": "",
        "Theme1": "",
        "Theme2": "",
        "Occasion1": "",
        "Occasion2": "",
        "Character1": "",
        "Character2": "",
        "Brand1": "",
        "Brand2": "",
        "Shape1": "",
        "Shape2": "",
        "Tag1": "",
        "Tag2": "",
    }

    Section_Names_By_Type_Dict = {
        "French Hook": "Chandelier Earrings",
        "French hook": "Chandelier Earrings",
        "Clip": "Clip On Earrings",
        "Clips": "Clip On Earrings",
        "Cuff and Wrap Earrings": "Cuff and Wrap Earrings",
        "Ear Wire": "French Hook",
        "Post Dangle": "Dangle and Drop Earrings",
        "Ear Jackets": "Ear Jackets",
        "Ear Cuff": "Cuff and Wrap Earrings",
        "Hoop": "Hoop Earrings",
        "Screwback": "Screwback Earrings",
        "Screw Back": "Screwback Earrings",
        "Stud": "Stud Earrings",
        "Threader Earrings": "Threader Earrings",
        "French Hook": "French Hooks",
        "Lever Back": "Lever Back",
        "lever back": "Lever Back",
        "Leverback": "Lever Back",
        "Single": "Single Earrings",
        "Post": "Stud Dangles",
        "Post No Dangle": "Dangle and Drop Earrings",
    }

    Type_By_Section_Names_Dict = {
        "Chandelier Earrings": "French Hook",
        "Clip On Earrings": "Clip",
        "Cuff and Wrap Earrings": "Cuff and Wrap Earrings",
        "Dangle and Drop Earrings": "Post Dangle",
        "Ear Jackets": "Ear Jackets",
        "Hoop Earrings": "Hoop",
        "Screwback Earrings": "Screwback",
        "Stud Earrings": "Stud",
        "Threader Earrings": "Threader Earrings",
        "French Hooks": "French Hook",
        "Single Earrings": "Single",
        "Stud Dangles": "Post",
    }

    Section_IDs_By_Type_Dict = {
        "Post Dangle": "1208",
        "Post No Dangle": "1203",
        "Clip": "1205",
        "Clips": "1205",
        "Cluster": "1206",
        "French Hook": "1208",
        "Chandelier": "1204",
        "Hoop": "1212",
        "Screwback": "1213",
        "Leverback": "1213",
        "Adjustable Leverback": "1213",
        "Screw Back": "1213",
        "Lever Back": "1213",
        "Adjustable Lever Back": "1213",
        "Stud": "1214",
        "Post": "1208",
        "Earwire": "1203",
        "Ear Wire": "1203",
    }

    Etsy_Type_ID_Dict = {
        "Earrings": "1203",
        "Chandelier": "1204",
        "Clip On": "1205",
        "Cluster": "1206",
        "Cuff & Wrap": "1207",
        "Dangle & Drop": "1208",
        "Ear Jackets & Climbers": "2900",
        "Ear Weights": "1210",
        "Gauge & Plug": "1211",
        "Hoop Earrings": "1212",
        "Jhumka": "12185",
        "Kaan Chains": "1223",
        "Screw Back Earrings": "1213",
        "Stud Earrings": "1214",
        "Threader Earrings": "1215",
        "Earwire": "1203",
    }

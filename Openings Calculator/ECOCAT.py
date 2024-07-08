# Define the ECO code categories
ECO_CATEGORIES = {
    "A00": "Polish (Sokolsky) opening",
    "A01": "Nimzovich-Larsen attack",
    "A02-A03": "Bird's opening",
    "A04-A09": "Reti opening",
    "A10-A39": "English opening",
    "A40-A41": "Queen's pawn",
    "A42": "Modern defence, Averbakh system",
    "A43-A44": "Old Benoni defence",
    "A45-A46": "Queen's pawn game",
    "A47": "Queen's Indian defence",
    "A48-A49": "King's Indian, East Indian defence",
    "A50": "Queen's pawn game",
    "A51-A52": "Budapest defence",
    "A53-A55": "Old Indian defence",
    "A56": "Benoni defence",
    "A57-A59": "Benko gambit",
    "A60-A79": "Benoni defence",
    "A80-A99": "Dutch",
    "B00": "King's pawn opening",
    "B01": "Scandinavian (centre counter) defence",
    "B02-B05": "Alekhine's defence",
    "B06": "Robatsch (modern) defence",
    "B07-B09": "Pirc defence",
    "B10-B19": "Caro-Kann defence",
    "B20-B99": "Sicilian defence",
    "C00-C19": "French defence",
    "C20": "King's pawn game",
    "C21-C22": "Centre game",
    "C23-C24": "Bishop's opening",
    "C25-C29": "Vienna game",
    "C30-C39": "King's gambit",
    "C40": "King's knight opening",
    "C41": "Philidor's defence",
    "C42-C43": "Petrov's defence",
    "C44": "King's pawn game",
    "C45": "Scotch game",
    "C46": "Three knights game",
    "C47-C49": "Four knights, Scotch variation",
    "C50": "Italian Game",
    "C51-C52": "Evans gambit",
    "C53-C54": "Giuoco Piano",
    "C55-C59": "Two knights defence",
    "C60-C99": "Ruy Lopez (Spanish opening)",
    "D00": "Queen's pawn game",
    "D01": "Richter-Veresov attack",
    "D02": "Queen's pawn game",
    "D03": "Torre attack (Tartakower variation)",
    "D04-D05": "Queen's pawn game",
    "D06": "Queen's Gambit",
    "D07-D09": "Queen's Gambit Declined, Chigorin defence",
    "D10-D15": "Queen's Gambit Declined Slav defence",
    "D16": "Queen's Gambit Declined Slav accepted, Alapin variation",
    "D17-D19": "Queen's Gambit Declined Slav, Czech defence",
    "D20-D29": "Queen's gambit accepted",
    "D30-D42": "Queen's gambit declined",
    "D43-D49": "Queen's Gambit Declined semi-Slav",
    "D50-D69": "Queen's Gambit Declined, 4.Bg5",
    "D70-D79": "Neo-Gruenfeld defence",
    "D80-D99": "Gruenfeld defence",
    "E00": "Queen's pawn game",
    "E01-E09": "Catalan, closed",
    "E10": "Queen's pawn game",
    "E11": "Bogo-Indian defence",
    "E12-E19": "Queen's Indian defence",
    "E20-E59": "Nimzo-Indian defence",
    "E60-E99": "King's Indian defence"
}

# Function to categorize ECO code
def categorize_eco(eco_code):
    for category, opening in ECO_CATEGORIES.items():
        if '-' in category:
            start, end = category.split('-')
            if start <= eco_code <= end:
                return opening
        else:
            if eco_code == category:
                return opening
    return "Unknown ECO code"

# Example usage
# eco_codes = ["A00", "A03", "A15", "B01", "C44", "D10", "E12"]
# for code in eco_codes:
#     print(f"ECO Code: {code}, Opening: {categorize_eco(code)}")

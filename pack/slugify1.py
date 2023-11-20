from doublon import RetireDoublon

class Slugify:
    @staticmethod
    def text_to_slug(chen, ramplasman="-"):
        lis = "abcdefghijklmnopqrstuvwxyz1234567890-"
        chen=chen.lower()
        for element in chen:
            if element not in lis:
                chen = chen.replace(element, ramplasman)
        chen = RetireDoublon.retire_doublon(chen, ramplasman)
        return chen

class RetireAksan:
    @staticmethod
    def retirer_accent(chen):
        accent = {'à': 'a', 'á': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a', 'è': 'e', 'é': 'e', 'ê': 'e', 'ë': 'e', 'ì': 'i',
                  'í': 'i', 'î': 'i', 'ï': 'i', 'ò': 'o', 'ó': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o', 'ù': 'u', 'ú': 'u',
                  'û': 'u', 'ü': 'u', 'ñ': 'n', 'ç': 'c'}
        chen_san_aksan = ''.join(accent.get(c, c) for c in chen)
        return chen_san_aksan

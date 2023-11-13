from doublon import retire_doublon
def slugify(chen, ramplasman="-"):
    lis="abcdefghijklmnopqrstuvwxyz1234567890-"
    chen=chen.lower()
    for element in chen:
        if element not in lis:
            chen=chen.replace(element,ramplasman)
    chen=retire_doublon(chen, ramplasman)
    if chen[-1]==ramplasman:
        chen=chen[:-1]
    return chen
print(slugify("Badio+ ___Marcklens+ etudiant ESIH_"))

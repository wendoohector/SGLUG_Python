from slugify1 import Slugify, RetireAksan
texte = "Nenpòt text la li ye mèt gen aksan"
slug = Slugify()
texte_san_aksan = RetireAksan.retirer_accent(texte)
texte_slugifie = slug.text_to_slug(texte_san_aksan)

print(texte_slugifie)

# countries.py - Base de données des pays d'Afrique et d'Asie

PAYS_AFRIQUE = [
    "Afrique du Sud", "Algérie", "Angola", "Bénin", "Botswana", "Burkina Faso", "Burundi",
    "Cameroun", "Cap-Vert", "République Centrafricaine", "Comores", "Congo", "RDC",
    "Côte d'Ivoire", "Djibouti", "Égypte", "Érythrée", "Eswatini", "Éthiopie", "Gabon",
    "Gambie", "Ghana", "Guinée", "Guinée-Bissau", "Guinée équatoriale", "Kenya", "Lesotho",
    "Libéria", "Libye", "Madagascar", "Malawi", "Mali", "Maroc", "Maurice", "Mauritanie",
    "Mozambique", "Namibie", "Niger", "Négéria", "Ouganda", "Rwanda", "Sao Tomé-et-Principe",
    "Sénégal", "Seychelles", "Sierra Leone", "Somalie", "Soudan", "Soudan du Sud",
    "Tanzanie", "Tchad", "Togo", "Tunisie", "Zambie", "Zimbabwe"
]

PAYS_ASIE = [
    "Afghanistan", "Arabie Saoudite", "Arménie", "Azerbaïdjan", "Bahreïn", "Bangladesh",
    "Bhoutan", "Birmanie", "Brunei", "Cambodge", "Chine", "Chypre", "Corée du Nord",
    "Corée du Sud", "Émirats Arabes Unis", "Géorgie", "Inde", "Indonésie", "Irak", "Iran",
    "Israël", "Japon", "Jordanie", "Kazakhstan", "Kirghizistan", "Koweït", "Laos", "Liban",
    "Malaisie", "Maldives", "Mongolie", "Népal", "Oman", "Ouzbékistan", "Pakistan",
    "Palestine", "Philippines", "Qatar", "Singapour", "Sri Lanka", "Syrie", "Tadjikistan",
    "Thaïlande", "Timor oriental", "Turkménistan", "Turquie", "Viêt Nam", "Yémen"
]

TOUS_LES_PAYS = PAYS_AFRIQUE + PAYS_ASIE

def valider_pays(nom_saisi):
    """Vérifie si le pays fait bien partie d'Afrique ou d'Asie."""
    for pays in TOUS_LES_PAYS:
        if pays.lower() == nom_saisi.strip().lower():
            return pays
    return None


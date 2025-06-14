import random
import datetime
import math

tips = [
    'È buona pratica chiudere il rubinetto quando si lavano i denti.', #1
    'Utilizza lampadine LED e spegnere le luci inutili.', #2
    'Cerca di spostarti con trasporti pubblici, bici o veicoli elettrici.', #3
    'Consuma cibi stagionali, ad esempio evita ciliegie d\'inverno.',#4
    'Utilizza borse riutilizzabili mentre si fa la spesa.',#5
    'Stacca la spina di dispositivi elettronici quando non vengono utilizzati.',#6
    'Riduci la durata delle doccie per ridurre il consumo d\'acqua.',#7
    'Chiudi sempre la bombola del gas prima di dormire.', #8
    'Usa prese conformi e salvavita. (Soprattutto se ci sono bambini)', #9
    'Approfitta della luce del sole quando è possibile.', #10
    'Mangia evitando posate e piatti di plastica.', #11
    'Fai sport all\'aperto, meglio di andare in palestra.', #12
    'Arieggiare la casa ogni giorno per mantenere l\'aria fresca e pulita', #13
    'Utilizza detersivi ecologici per il bucato.', #14
    'Durante i mesi estivi, utilizza il ventilatore anziche il condizionatore.', #15
    'Rispetta la raccolta differenziata.' #16
]

quizzes = [
    { #1
        'Title': 'Quando ti lavi i denti, chiudi il rubinetto?',
        'one': 'Sì.',
        'two': 'No.',
        'amount': 2,
        'correct': 1,
    },
    { #2
        'Title': 'Cosa fai quando sei a casa?',
        'one': 'Spengo le luci quando non vengono utilizzate.',
        'two': 'Lascio le luci accese per convenienza.',
        'amount': 2,
        'correct': 1,
    },
    { #3
        'Title': 'Qual è il mezzo di trasporto che utilizzi di più?',
        'one': 'Bicicletta',
        'two': 'Automobile',
        'three': 'Moto',
        'amount': 3,
        'correct': 1,
    },
    { #4
        'Title': 'Quale frutto, fra questi due, mangi di più d\'estate?',
        'one': 'Anguria',
        'two': 'Kiwi',
        'amount': 2,
        'correct': 1,
    },
    { #5
        'Title': 'Quali buste utilizzi di più?',
        'one': 'Buste di plastica',
        'two': 'Buste riutilizzabili',
        'amount': 2,
        'correct': 2,
    },
    { #6
        'Title': 'Prima di dormire, lasci la TV in standby?',
        'one': 'Sì.',
        'two': 'No.',
        'amount': 2,
        'correct': 2,
    },
    { #7
        'Title': 'Cerchi di mantenere le doccie corte?',
        'one': 'Sì',
        'two': 'No',
        'amount': 2,
        'correct': 1,
    },
    { #8
        'Title': 'È buono controllare se il tappo della bombola è chiuso?',
        'one': 'Sì.',
        'two': 'No.',
        'amount': 2,
        'correct': 1,
    },
    { #9
        'Title': 'Controlli le prese?',
        'one': 'No, non controllo le prese.',
        'two': 'Sì, Controllo periodicamente le prese.',
        'amount': 2,
        'correct': 2,
    },
    { #10
        'Title': 'Compreresti una casa luminosa?.',
        'one': 'Sì.',
        'two': 'No.',
        'amount': 2,
        'correct': 1,
    },
    { #11
        'Title': 'Che tipo di posate usi quando si è con amici?',
        'one': 'Posate e piatti di ceramica, per evitare sprechi.',
        'two': 'Posate e piatti di plastica, per convenienza.',
        'amount': 2,
        'correct': 1,
    },
    { #12
        'Title': 'Approfitti della bella stagione per andare a fare footing al parco??',
        'one': 'Sì.',
        'two': 'No.',
        'amount': 2,
        'correct': 1,
    },
    { #13
        'Title': 'Al mattino, è fai prima la colazione o apri le finestre?',
        'one': 'Fare colazione.',
        'two': 'Aprire le finestre.',
        'amount': 2, 
        'correct': 2,
    },
    { #14
        'Title': 'Utilizzi detersivi ecologici?',
        'one': 'Sì',
        'two': 'No',
        'amount': 2,
        'correct': 1,
    },
    { #15
        'Title': 'Utilizzi di più il ventilatore o il condizionatore?',
        'one': 'Ventilatore.',
        'two': 'Condizionatore.',
        'amount': 2,
        'correct': 1,
    },
    { #16
        'Title': 'Rispetti gli orari per buttare la spazzatura?',
        'one': 'Sì',
        'two': 'No',
        'amount': 2,
        'correct': 1,
    },
]

def ranTip(day, month, year):
    a = round(math.sqrt(day*16384))
    b = round(math.sqrt(month*16384))
    c = round(math.sqrt(year*16384))
    return tips[(round(math.sqrt(a*b*c)))%(len(tips))-1]

def ranQuiz(day, month, year):
    a = round(math.sqrt(day*16384))
    b = round(math.sqrt(month*16384))
    c = round(math.sqrt(year*16384))
    return quizzes[(round(math.sqrt(a*b*c)))%(len(tips))-1]

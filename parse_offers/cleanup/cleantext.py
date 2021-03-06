
def cleanUpTitle(title):
    """Removes words from a string that are not useful."""

    badWords = ['PLUS ', 'Alle AH ', 'Diverse AH ', 'Alle ', 'AH ', '*', 'Jumbo ']

    title = title.replace("’", "'") # sanitize different kinds of apostrophes
    title = title.replace(" ", " ") # sanitize weird space character
    for word in badWords:
        title = title.replace(word, '')

    cleanTitle = title.strip().capitalize()
    
    return cleanTitle

def cleanUpInfo(infoText):
    """Removes words from a string that are not useful."""

    if 'Bijv.' in infoText:
        infoText = ""
    else:     
        badWords = ['PlUS ', 'Jumbo ', 'Alle soorten\n3 verpakkingen', 
                    'Alle soorten\n2 verpakkingen',
                    'Alle soorten ', 'Alle soorten\n', 'Alle soorten',
                    'Alle soorten\n2 ', 'Alle soorten\n3 ', 'Alle soorten, ', 
                    'Alle combinaties mogelijk ', 'Diverse soorten',
                    'Alle varianten', 'Per stuk', 'Alle verpakkingen', 
                    'Diverse varianten, combineren mogelijk', '<ul><li>',
                    '<li>', '</li><li>', '</li>', '</ul>', '&nbsp;','</li></ul>', '<p>', '</p>']

        infoText = infoText.replace("’", "'") # sanitize different kinds of apostrophes
        infoText = infoText.replace(" ", " ") # sanitize weird space character

        for word in badWords:
            infoText = infoText.replace(word, '')

    cleanInfoText = infoText.strip().capitalize()
    
    return cleanInfoText

import update

def banner():
    version = update.Update.getLocalVersion(update.Update.getFolder())
    spacing = len(version) - 5
    if spacing < 0: spacing = 0
    spacing = ' ' * spacing
    logo = [
        f'{spacing}  _____              __         ',
        f'{spacing} / ___/_____ _____  / /______ __',
        f'{spacing}/ /__/ __/ // / _ \\/ __/ -_) \\ /',
        f'{spacing}\\___/_/  \\_, / .__/\\__/\\__/_\\_\\ ',
        f' V:{version}/___/_/  OOP Edition    ',
        ' Locks only exist to keep honest',
        '          people honest         ',
    ]
    logo_len = max([len(item) for item in logo])
    
    art = [
        '    ____                                  __      _         ',
        '   / __ \  __  __   ____ ___     ____    / /__   (_)   ____ ',
        '  / /_/ / / / / /  / __ `__ \   / __ \\  / //_/  / /   / __ \\',
        ' / ____/ / /_/ /  / / / / / /  / /_/ / / ,<    / /   / / / /',
        '/_/      \\__,_/  /_/ /_/ /_/  / .___/ /_/|_|  /_/   /_/ /_/ ',
        '                             /_/                            ',
    ]
    art_len = max([len(item) for item in art])
    
    art_txt = ''
    for a in art: art_txt += a
        
    offset = ' ' * int((art_len / 2) - (logo_len / 2))
    
    for item in logo:
        print(f'{offset}{item}')
    for item in art:
        print(f'{item}')

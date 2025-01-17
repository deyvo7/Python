import re  # Importujemy moduł 're', który pozwala na pracę z wyrażeniami regularnymi

# Funkcja do pobierania adresu nadawcy z e-maila
def email_sender(email_content):
    # Wzór do wyciągania adresu nadawcy z pola "From"
    # Wzór: "From:" + dowolne znaki + <adres e-mail>
    # r"From:.*<(.+?)>"
    # "From:" - zaczynamy od szukania słowa "From:"
    # ".*" - oznacza dowolną ilość znaków (może być np. tekst przed adresem)
    # "<" - szukamy znaku "<" otwierającego adres e-mail
    # "(.+?)" - to jest nasza grupa, która wyciąga adres e-mail w nawiasie ostrym "<...>"
    # "?" powoduje, że regex zatrzymuje się na pierwszym możliwym dopasowaniu, czyli tuż przed ">"
    pattern = r"From:.*<(.+?)>"
    # szukamy wzorca w treści e-maila
    match = re.search(pattern, email_content)
    if match:
        # Jeśli znaleziono dopasowanie, zwracamy adres e-mail z grupy 1
        return match.group(1)
    return "Adres nadawcy nie znaleziony."

# Funkcja do pobierania adresu odbiorcy z e-maila
def email_recipient(email_content):
    # Wzór do wyciągania adresu odbiorcy z pola "To"
    # Wzór: "To:" + dowolne znaki + <adres e-mail>
    # r"To:.*<(.+?)>"
    # "To:" - zaczynamy od szukania słowa "To:"
    # ".*" - oznacza dowolne znaki między "To:" a adresem e-mail
    # "<" - szukamy znaku "<", który otacza adres e-mail
    # "(.+?)" - wyciągamy adres e-mail w nawiasach ostrych
    pattern = r"To:.*<(.+?)>"
    match = re.search(pattern, email_content)
    if match:
        # Jeśli znaleziono dopasowanie, zwracamy adres e-mail z grupy 1
        return match.group(1)
    return "Adres odbiorcy nie znaleziony."

# Funkcja do pobierania tematu wiadomości z e-maila
def email_subject(email_content):
    # Wzór do wyciągania tematu wiadomości z pola "Subject"
    # r"Subject: (.+)"
    # "Subject:" - szukamy dokładnie słowa "Subject:"
    # "(.+)" - to jest nasza grupa, która wyciąga wszystko po słowie "Subject:"
    # ".+" oznacza jedno lub więcej wystąpień dowolnego znaku
    pattern = r"Subject: (.+)"
    match = re.search(pattern, email_content)
    if match:
        # Jeśli znaleziono dopasowanie, zwracamy temat wiadomości
        return match.group(1)
    return "Temat nie znaleziony."

# Funkcja do pobierania treści wiadomości (po nagłówkach e-maila)
def email_body(email_content):
    # Wzór do wyciągania treści wiadomości po nagłówkach
    # r"\r?\n\r?\n(.*)"
    # "\r?\n" - oznacza znak nowej linii w systemach Windows ("\r\n") lub w systemach UNIX (tylko "\n")
    # "\r?" - opcjonalny znak powrotu karetki (czyli "\r" w systemach Windows)
    # "(.*)" - dopasowujemy wszystko, co znajduje się po dwóch nowych liniach (czyli treść wiadomości)
    # re.DOTALL pozwala na dopasowanie treści wieloliniowych, ponieważ domyślnie "." nie pasuje do nowych linii
    pattern = r"\r?\n\r?\n(.*)"
    match = re.search(pattern, email_content, re.DOTALL)  # re.DOTALL umożliwia dopasowanie także znaków nowych linii
    if match:
        # Jeśli znaleziono dopasowanie, zwracamy treść wiadomości
        return match.group(1).strip()  # strip() usuwa zbędne spacje na początku i końcu treści
    return "Treść wiadomości nie znaleziona."

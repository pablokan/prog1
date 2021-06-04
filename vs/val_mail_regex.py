def is_valid_email(email):
    import re

    body_regex = re.compile('''
        ^(?!\.)                            # name may not begin with a dot
        (
        [-a-z0-9!\#$%&'*+/=?^_`{|}~]     # all legal characters except dot
        |
        (?<!\.)\.                        # single dots only
        )+
        (?<!\.)$                            # name may not end with a dot
    ''', re.VERBOSE | re.IGNORECASE)
    domain_regex = re.compile('''
        (
        localhost
        |
        (
            [a-z0-9]
                # [sub]domain begins with alphanumeric
            (
            [-\w]*                         # alphanumeric, underscore, dot, hyphen
            [a-z0-9]                       # ending alphanumeric
            )?
        \.                               # ending dot
        )+
        [a-z]{2,}                        # TLD alpha-only
    )$
    ''', re.VERBOSE | re.IGNORECASE)

    if not isinstance(email, str) or not email or '@' not in email:
        return False
    
    body, domain = email.rsplit('@', 1)

    match_body = body_regex.match(body)
    match_domain = domain_regex.match(domain)

    if not match_domain:
        # check for Internationalized Domain Names
        # see https://docs.python.org/2/library/codecs.html#module-encodings.idna
        try:
            domain_encoded = domain.encode('idna').decode('ascii')
        except UnicodeError:
            return False
        match_domain = domain_regex.match(domain_encoded)

    return (match_body is not None) and (match_domain is not None)


print(is_valid_email('pablokan@itecriocuarto.org.ar'))
print(is_valid_email('pablo.kan@itecriocuarto.org.ar'))
print(is_valid_email('p.bunader@itecriocuarto.org.ar'))
print(is_valid_email('kan@itec.org'))



# print(is_valid_email('a@b.com'))  # True.
# print(is_valid_email('abc@def.com'))  # True.
# print(is_valid_email('abc@3def.com'))  # True.
# print(is_valid_email('abc@def.us'))  # True.
# print(is_valid_email('abc@d_-f.us'))  # True.
# print(is_valid_email('@def.com'))  # False.
# print(is_valid_email('"abc@def".com'))  # False.
# print(is_valid_email('abc+def.com'))  # False.
# print(is_valid_email('abc@def.x'))  # False.
# print(is_valid_email('abc@def.12'))  # False.
# print(is_valid_email('abc@def..com'))  # False.


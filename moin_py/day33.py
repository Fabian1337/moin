m = r'''
DER FRÜHE VOGEL FÄNGT DAS MOIN

                      1 /\ 1
                     0 1  1 0 _
                    /_/_   \." a. __
                ___  / /    ;  ;"`\ \
             ."`   `"./   ."   ;   1_1_
           ."          `;'     ;     \ \
          ."          .`    ',;       1 0
        ."  ; ; ;,            `=.      \_\_
     .-", ;  ; ;,       ; ,      `'=,    111111
    `""'"=-.;.;"       ";; ,         ;    0 1
      _     ."        _.; ; ;        ;    / /
    `;,`-.="      _.="   ; ; ;      ,'   0 0
      ;=;     _."`        `;;  ;   ;     1110
     , ;-"_;="              '=; ; ;         \ \
      `"."                     `=;(         / /
      ."                          `'       / /
                                          `"`
_http://ascii.co.uk/art/birds_
'''

def btd(binary):
    decimal = i = 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

def moin():
    a = [str(s) for s in list(m) if s.isdigit()]
    a += a[-4:]
    return "".join(map(chr, [btd(int("".join(a[i:i+7]))) for i in range(0, len(a), 7)]))

if __name__ == "__main__":
    print(moin())
class font:
    SPACE       =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]]
    EXCLAM      =  [[0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,0,0,0],
                    [0,0,1,0,0]]
    DQUOTE      =  [[0,1,0,1,0],
                    [0,1,0,1,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]]
    POUND       =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,1,0,1,0],
                    [1,1,1,1,1],
                    [0,1,0,1,0],
                    [1,1,1,1,1],
                    [0,1,0,1,0]]
    DOLLAR      =  [[0,0,1,0,0],
                    [0,1,1,1,1],
                    [1,0,0,0,0],
                    [0,1,1,1,0],
                    [0,0,0,0,1],
                    [1,1,1,1,0],
                    [0,0,1,0,0]]
    PERCENT     =  [[1,1,0,0,0],
                    [1,1,0,0,1],
                    [0,0,0,1,0],
                    [0,0,1,0,0],
                    [0,1,0,0,0],
                    [1,0,0,1,1],
                    [0,0,0,1,1]]
    AMPERSAND   =  [[0,1,1,0,0],
                    [1,0,0,1,0],
                    [1,0,0,1,0],
                    [0,1,1,0,0],
                    [1,0,0,1,1],
                    [1,0,0,1,0],
                    [0,1,1,0,1]]
    SQUOTE      =  [[0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]]
    LPAREN      =  [[0,0,1,0,0],
                    [0,1,0,0,0],
                    [1,0,0,0,0],
                    [1,0,0,0,0],
                    [1,0,0,0,0],
                    [0,1,0,0,0],
                    [0,0,1,0,0]]
    RPAREN      =  [[0,0,1,0,0],
                    [0,0,0,1,0],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [0,0,0,1,0],
                    [0,0,1,0,0]]
    ASTERISK    =  [[0,0,0,0,0],
                    [0,0,1,0,0],
                    [1,0,1,0,1],
                    [0,1,1,1,0],
                    [1,0,1,0,1],
                    [0,0,1,0,0],
                    [0,0,0,0,0]]
    PLUS        =  [[0,0,0,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [1,1,1,1,1],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,0,0,0]]
    COMMA       =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,1,0,0],
                    [0,1,0,0,0]]
    HYPHEN      =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [1,1,1,1,1],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]]
    PERIOD      =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,1,0,0,0]]
    FSLASH      =  [[0,0,0,0,1],
                    [0,0,0,1,0],
                    [0,0,0,1,0],
                    [0,0,1,0,0],
                    [0,1,0,0,0],
                    [0,1,0,0,0],
                    [1,0,0,0,0]]
    ZERO        =  [[0,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,1,1],
                    [1,0,1,0,1],
                    [1,1,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,0]]
    ONE         =  [[0,0,1,0,0],
                    [0,1,1,0,0],
                    [1,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0]]
    TWO         =  [[0,1,1,1,0],
                    [1,0,0,0,1],
                    [0,0,0,0,1],
                    [0,0,1,1,0],
                    [0,1,0,0,0],
                    [1,0,0,0,0],
                    [1,1,1,1,1]]
    THREE       =  [[1,1,1,1,1],
                    [0,0,0,1,0],
                    [0,0,1,0,0],
                    [0,1,1,1,0],
                    [0,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,0]]
    FOUR        =  [[0,0,0,1,0],
                    [0,0,1,1,0],
                    [0,1,0,1,0],
                    [1,0,0,1,0],
                    [1,1,1,1,1],
                    [0,0,0,1,0],
                    [0,0,0,1,0]]
    FIVE        =  [[1,1,1,1,1],
                    [1,0,0,0,0],
                    [1,1,1,1,0],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,0]]
    SIX         =  [[0,1,1,1,0],
                    [1,0,0,0,0],
                    [1,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,0]]
    SEVEN       =  [[1,1,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,1,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0]]
    EIGHT       =  [[0,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,0]]
    NINE        =  [[0,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,1],
                    [0,0,0,0,1],
                    [0,1,1,1,0]]
    COLON       =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,1,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,1,0,0],
                    [0,0,0,0,0]]
    SEMICOLON   =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,1,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,1,0,0],
                    [0,1,0,0,0]]
    LESSTHAN    =  [[0,0,0,1,0],
                    [0,0,1,0,0],
                    [0,1,0,0,0],
                    [1,0,0,0,0],
                    [0,1,0,0,0],
                    [0,0,1,0,0],
                    [0,0,0,1,0]]
    EQUALS      =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [1,1,1,1,1],
                    [0,0,0,0,0],
                    [1,1,1,1,1],
                    [0,0,0,0,0],
                    [0,0,0,0,0]]
    GREATERTHAN =  [[0,1,0,0,0],
                    [0,0,1,0,0],
                    [0,0,0,1,0],
                    [0,0,0,0,1],
                    [0,0,0,1,0],
                    [0,0,1,0,0],
                    [0,1,0,0,0]]
    QUESTION    =  [[0,1,1,1,0],
                    [1,0,0,0,1],
                    [0,0,0,0,1],
                    [0,0,0,1,0],
                    [0,0,1,0,0],
                    [0,0,0,0,0],
                    [0,0,1,0,0]]
    ATSIGN      =  [[0,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,1,1,1],
                    [1,0,1,0,1],
                    [1,0,1,1,1],
                    [1,0,0,0,0],
                    [0,1,1,1,0]]
    A           =  [[0,0,1,0,0],
                    [0,1,0,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,1,1,1,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1]]
    B           =  [[1,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,1,1,1,0]]
    C           =  [[0,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,0],
                    [1,0,0,0,0],
                    [1,0,0,0,0],
                    [1,0,0,0,1],
                    [0,1,1,1,0]]
    D           =  [[1,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,1,1,1,0]]
    E           =  [[1,1,1,1,1],
                    [1,0,0,0,0],
                    [1,0,0,0,0],
                    [1,1,1,1,0],
                    [1,0,0,0,0],
                    [1,0,0,0,0],
                    [1,1,1,1,1]]
    F           =  [[1,1,1,1,1],
                    [1,0,0,0,0],
                    [1,0,0,0,0],
                    [1,1,1,1,0],
                    [1,0,0,0,0],
                    [1,0,0,0,0],
                    [1,0,0,0,0]]
    G           =  [[0,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,0],
                    [1,0,1,1,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,1]]
    H           =  [[1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,1,1,1,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1]]
    I           =  [[0,1,1,1,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,1,1,1,0]]
    J           =  [[0,0,0,0,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,0]]
    K           =  [[1,0,0,0,1],
                    [1,0,0,1,0],
                    [1,0,1,0,0],
                    [1,1,0,0,0],
                    [1,0,1,0,0],
                    [1,0,0,1,0],
                    [1,0,0,0,1]]
    L           =  [[1,0,0,0,0],
                    [1,0,0,0,0],
                    [1,0,0,0,0],
                    [1,0,0,0,0],
                    [1,0,0,0,0],
                    [1,0,0,0,0],
                    [1,1,1,1,1]]
    M           =  [[1,0,0,0,1],
                    [1,1,0,1,1],
                    [1,0,1,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1]]
    N           =  [[1,0,0,0,1],
                    [1,1,0,0,1],
                    [1,0,1,0,1],
                    [1,0,0,1,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1]]
    O           =  [[0,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,0]]
    P           =  [[1,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,1,1,1,0],
                    [1,0,0,0,0],
                    [1,0,0,0,0]]
    Q           =  [[0,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,0],
                    [0,0,0,1,1]]
    R           =  [[1,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1]]
    S           =  [[0,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,0],
                    [0,1,1,1,0],
                    [0,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,0]]
    T           =  [[1,1,1,1,1],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0]]
    U           =  [[1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,0]]
    V           =  [[1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,0,1,0],
                    [0,0,1,0,0]]
    W           =  [[1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,1,0,1],
                    [1,0,1,0,1],
                    [0,1,0,1,0]]
    X           =  [[1,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,0,1,0],
                    [0,0,1,0,0],
                    [0,1,0,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1]]
    Y           =  [[1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,0,1,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0]]
    Z           =  [[1,1,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,1,0],
                    [0,0,1,0,0],
                    [0,1,0,0,0],
                    [1,0,0,0,0],
                    [1,1,1,1,1]]
    LBRACKET    =  [[1,1,1,0,0],
                    [1,0,0,0,0],
                    [1,0,0,0,0],
                    [1,0,0,0,0],
                    [1,0,0,0,0],
                    [1,0,0,0,0],
                    [1,1,1,0,0]]
    BSLASH      =  [[1,0,0,0,0],
                    [0,1,0,0,0],
                    [0,1,0,0,0],
                    [0,0,1,0,0],
                    [0,0,0,1,0],
                    [0,0,0,1,0],
                    [0,0,0,0,1]]
    RBRACKET    =  [[0,0,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1],
                    [0,0,1,1,1]]
    CARET       =  [[0,0,1,0,0],
                    [0,1,0,1,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]]
    UNDERSCORE  =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [1,1,1,1,1]]
    BACKTICK    =  [[0,1,0,0,0],
                    [0,0,1,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]]
    LA          =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,1,1,1,0],
                    [0,0,0,0,1],
                    [0,1,1,1,1],
                    [1,0,0,0,1],
                    [0,1,1,1,1]]
    LB          =  [[1,0,0,0,0],
                    [1,0,0,0,0],
                    [1,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,1,1,1,0]]
    LC          =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,0],
                    [1,0,0,0,0],
                    [0,1,1,1,1]]
    LD          =  [[0,0,0,0,1],
                    [0,0,0,0,1],
                    [0,1,1,1,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,1]]
    LE          =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,1,1,1,0],
                    [1,0,0,0,1],
                    [1,1,1,1,1],
                    [1,0,0,0,0],
                    [0,1,1,1,1]]
    LF          =  [[0,0,0,1,1],
                    [0,0,1,0,0],
                    [1,1,1,1,1],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0]]
    LG          =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,1,1,1,1],
                    [1,0,0,0,1],
                    [0,1,1,1,1],
                    [0,0,0,0,1],
                    [0,1,1,1,0]]
    LH          =  [[1,0,0,0,0],
                    [1,0,0,0,0],
                    [1,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1]]
    LI          =  [[0,0,1,0,0],
                    [0,0,0,0,0],
                    [0,1,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,1,0]]
    LJ          =  [[0,0,1,0,0],
                    [0,0,0,0,0],
                    [0,1,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [1,1,0,0,0]]
    LK          =  [[1,1,0,0,0],
                    [0,1,0,0,0],
                    [0,1,0,0,1],
                    [0,1,0,1,0],
                    [0,1,1,0,0],
                    [0,1,0,1,0],
                    [0,1,0,0,1]]
    LL          =  [[0,1,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,0,1,1]]
    LM          =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [1,1,1,1,0],
                    [1,0,1,0,1],
                    [1,0,1,0,1],
                    [1,0,1,0,1],
                    [1,0,1,0,1]]
    LN          =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [1,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1]]
    LO          =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,0]]
    LP          =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [1,1,1,1,0],
                    [1,0,0,0,1],
                    [1,1,1,1,0],
                    [1,0,0,0,0],
                    [1,0,0,0,0]]
    LQ          =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,1,1,1,1],
                    [1,0,0,0,1],
                    [0,1,1,1,1],
                    [0,0,0,0,1],
                    [0,0,0,0,1]]
    LR          =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [1,1,1,1,0],
                    [1,0,0,0,1],
                    [1,0,0,0,0],
                    [1,0,0,0,0],
                    [1,0,0,0,0]]
    LS          =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,1,1,1,0],
                    [1,0,0,0,0],
                    [0,1,1,1,0],
                    [0,0,0,0,1],
                    [1,1,1,1,0]]
    LT          =  [[0,1,0,0,0],
                    [0,1,0,0,0],
                    [1,1,1,1,0],
                    [0,1,0,0,0],
                    [0,1,0,0,0],
                    [0,1,0,0,0],
                    [0,0,1,1,1]]
    LU          =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,1]]
    LV          =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,0,1,0],
                    [0,0,1,0,0]]
    LW          =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [1,0,1,0,1],
                    [1,0,1,0,1],
                    [0,1,0,1,0]]
    LX          =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [1,0,0,0,1],
                    [0,1,0,1,0],
                    [0,0,1,0,0],
                    [0,1,0,1,0],
                    [1,0,0,0,1]]
    LY          =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [1,0,0,0,1],
                    [1,0,0,0,1],
                    [0,1,1,1,1],
                    [0,0,0,0,1],
                    [0,1,1,1,0]]
    LZ          =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [1,1,1,1,1],
                    [0,0,0,1,0],
                    [0,0,1,0,0],
                    [0,1,0,0,0],
                    [1,1,1,1,1]]
    LCURLY      =  [[0,0,1,0,0],
                    [0,1,0,0,0],
                    [0,1,0,0,0],
                    [1,0,0,0,0],
                    [0,1,0,0,0],
                    [0,1,0,0,0],
                    [0,0,1,0,0]]
    BAR         =  [[0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0]]
    RCURLY      =  [[0,0,1,0,0],
                    [0,0,0,1,0],
                    [0,0,0,1,0],
                    [0,0,0,0,1],
                    [0,0,0,1,0],
                    [0,0,0,1,0],
                    [0,0,1,0,0]]
    TILDE       =  [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,1,0,1,0],
                    [1,0,1,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]]

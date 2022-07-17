class tablaDeAnalisis:
    diccionario_tabla = {
        'ID': {'regla':['L', 'I', 'F', 'A', 'C']}, # C A F I L
        'C': {'regla':['DPUNTO' , 'NOMBRE', 'CLASE']},  # CLASE NOMBRE DPUNTO
        'A': {'regla':['V', 'S', 'NOMBRE']},  # NOMBRE S V
        'F': {'regla':['CONTENIDO', 'DPUNTO', 'LLAVEC', 'FSELF', 'LLAVEA', 'NOMBRE', 'FUNC']}, # FUNC NOMBRE LLAVEA FSELF LLAVEC DPUNTO CONTENIDO
        'I': {'regla':['LLAVEC', 'LLAVEA', 'NOMBRE', 'S', 'NOMBRE']}, # NOMBRE S NOMBRE LLAVEA LLAVEC
        'L': {'regla':['LLAVEC', 'LLAVEA', 'NOMBRE', 'PUNTO', 'NOMBRE']}, # NOMBRE PUNTO NOMBRE LLAVEA LLAVEC
        'CONTENIDO': {'regla':['LLAVEC', 'COMIC', 'NOMBRE', 'COMIA', 'LLAVEA', 'IMPRIMIR']},# IMPRIMIR LLAVEA COMIA NOMBRE COMIC LLAVEC
        'V': {'regla':['DIGITO']}, # RV DIGITO
        'DIGITO': {'regla':['0...9']}, # 
        'RV': {'regla':['DIGITO','RV']}, # RV  DIGITO 
        'NOMBRE': {'regla':['LETRA']}, # RN LETRA ------
        'RN': {'regla':['LETRA', 'RN']}, #RN  LETRA
        'LETRA': {'regla':['a...z']}, # A...Z, a...z  -----
        'S': {'regla':['=']}, # =
        'LLAVEA': {'regla':['(']}, # (
        'LLAVEC': {'regla':[')']}, # )
        'FUNC': {'regla':['def']},
        'FSELF': {'regla':['self']},
        'COMIA': {'regla':['´']},
        'COMIC': {'regla':['´']},
        'PUNTO': {'regla':['.']},
        'DPUNTO': {'regla':[':']},
        'IMPRIMIR': {'regla':['print']},
        'CLASE': {'regla':['class']}
    }
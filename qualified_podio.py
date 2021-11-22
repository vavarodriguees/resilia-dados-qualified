def podio_olimpico(tempo_1,tempo_2,tempo_3,nome_corredor1,nome_corredor2,nome_corredor3):
  
  primeiro = 0
  segundo = 0
  terceiro = 0
  nome_primeiro = ''
  nome_segundo = ''
  nome_terceiro = ''
  
  if tempo_1 < tempo_2 and tempo_1 < tempo_3:
    primeiro = tempo_1
    nome_primeiro = nome_corredor1
    if tempo_2 < tempo_3:
      segundo = tempo_2
      nome_segundo = nome_corredor2
      terceiro = tempo_3
      nome_terceiro = nome_corredor3
    else:
      segundo = tempo_3
      nome_segundo = nome_corredor3
      terceiro = tempo_2
      nome_terceiro = nome_corredor2
      
  elif tempo_2 < tempo_1 and tempo_2 < tempo_3:
    primeiro = tempo_2
    nome_primeiro = nome_corredor2
    if tempo_1 < tempo_3:
      segundo = tempo_1
      nome_segundo = nome_corredor1
      terceiro = tempo_3
      nome_terceiro = nome_corredor3
      
    else:
      segundo = tempo_3
      nome_segundo = nome_corredor3
      terceiro = tempo_1
      nome_terceiro = nome_corredor1
  else:
    primeiro = tempo_3
    nome_primeiro = nome_corredor3
    if tempo_1 < tempo_2:
      segundo = tempo_1
      nome_segundo = nome_corredor1
      terceiro = tempo_2
      nome_terceiro = nome_corredor2
    else:
      segundo = tempo_2
      nome_segundo = nome_corredor2
      terceiro = tempo_1 
      nome_terceiro = nome_corredor1

  return f'1 - {nome_primeiro} - {primeiro} minutos\n2 - {nome_segundo} - {segundo} minutos\n3 - {nome_terceiro} - {terceiro} minutos\n'

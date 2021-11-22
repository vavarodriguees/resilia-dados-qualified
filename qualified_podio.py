def podio_olimpico(tempo_1,tempo_2,tempo_3):
  print(tempo_1,tempo_2,tempo_3)
  primeiro = 0
  segundo = 0
  terceiro = 0
  if tempo_1 < tempo_2 and tempo_1 < tempo_3:
    primeiro = tempo_1
    if tempo_2 < tempo_3:
      segundo = tempo_2
      terceiro = tempo_3
    else:
      segundo = tempo_3
      terceiro = tempo_2
      
  elif tempo_2 < tempo_1 and tempo_2 < tempo_3:
    primeiro = tempo_2
    if tempo_1 < tempo_3:
      segundo = tempo_1
      terceiro = tempo_3
    else:
      segundo = tempo_3
      terceiro = tempo_1
      
  else:
    primeiro = tempo_3
    if tempo_1 < tempo_2:
      segundo = tempo_1
      terceiro = tempo_2
    else:
      segundo = tempo_2
      terceiro = tempo_1 

  return f'1 - {primeiro} minutos\n2 - {segundo} minutos\n3 - {terceiro} minutos\n'

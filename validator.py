def validate(x):
  for i in range(len(x)):
    try:
      float(x[i])
    except:
      print("ERROR: Enter positive numbers only")
      return 'false'
    if float(x[i]) < 0:
      print("ERROR: Enter positive numbers only")
      return 'false'
  return 'true'

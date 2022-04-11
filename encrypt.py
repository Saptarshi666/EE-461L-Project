def customEncrypt(inputText, N, D):
  """ 
  Takes a string called inputText and shifts each character N setps (based on the ASCII code) either right orleft, depending on the specified direction D
  """
  # print(inputText)
  rev = ""
  enc = ""
  for i in inputText:
    rev = i + rev
  rev = rev.replace("!", "")
  rev = rev.replace(" ", "")
  # print(rev)
  encList = list(rev)
  # print(encList)
  if D == 1:
    for i in rev:
      o = ord(i) + N
      if o > 126:
        o = o-92
      c = chr(o)
      # print(i, "->", c)
      enc = enc + c
      # print(enc)
    return str(enc)
 #   print(enc) 
  elif D == (-1):
    for i in rev:
      o = ord(i) - N
      if o <34:
        o = o+93
      c = chr(o)
     # print(ord(i), i, "->", c, o)
      enc = enc + c
  #  print(enc) 
    return str(enc)
  return enc
# end file
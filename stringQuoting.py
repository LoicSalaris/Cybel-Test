def quoting (a):
  b = a.replace('\'', '\\')
  return b.replace('\\', '\\\\')

print (quoting("Hello i'm here"))
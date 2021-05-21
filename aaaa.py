class Dad:
  gene = 'XX'
  
class Mom:
  gene = 'XY'

class Boy(Dad, Mom):
    pass
  
boy = Boy()
print(boy.gene)
  
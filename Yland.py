#!/usr/bin/env python3
# icmb
# ncmb
# stol
# load
    # stol
# _0x1AB2
# rconfig
    # icmb
    # _0x1AB2
    # ncmb
# vgroup
# backtrace
# yland
################################### ICMB
def icmb(n, t):
  '''Initial Combination'''
  c = []
  for j in range(t):
    c.append(j)
  c.extend([n, 0])
  return c #                        >>>>

################################### NCMB
def ncmb(c):
  '''Next Combination'''
  j = 0
  while c[j] + 1 == c[j + 1]:
    c[j] = j
    j += 1
  if not c[j + 1]: return False #   >>>>
  c[j] += 1
  return True #                     >>>>

################################### STOL
def stol(s):
  '''String to List'''
  ls = list(map(int, s.split()))
  return ls #                       >>>>

################################### GLOB
HRZ, VRT = 0, 1
Shape = None     # map dimensions
Const = [[], []] # constrains
debug = False
################################### LOAD
def load(filename):
  '''Load Input Data'''
  global Shape, Const, HRZ, VRT
  with open(filename) as f:
    bf = f.read().splitlines()
    bf = list(filter(None, bf))
  Shape = tuple(stol(bf.pop(0))* 2)
  for j in (HRZ, VRT):
    for i in range(Shape[j]):
      ls = stol(bf.pop(0))
      Const[j].append(ls) #         >>>>

################################ _0X1AB2
def _0x1AB2(width, poz, group):
  '''Cons Map Row'''
  ry = [0]* width
  for p, g in zip(poz, group):
    ry[p:p + g] = [1]* g
  return ry #                       >>>>
  
################################# CONFIG
# Return all yland configurations for a
# given ylands «group» and map «width».
# If we put a sea squares at the front #
# and the end of a map row, there is a #
# one to one correspondence with the ###
# number of different configurations and
# the number of positive solutions for #
# the remaining sea segments. ##########
def rconfig(width, group):
  '''x_1 + ... + x_k = n'''
  if debug: import pdb; pdb.set_trace()
  k = len(group) +1
  n = width+ 2 -sum(group)
  c = icmb(n -1, k- 1)
  bf = [] # buffer
  R = range(len(group))
  while True:
    j = c[:-2] # discard sentinels
    for a in R:
      j[a] += sum(group[:a])
    bf.append(_0x1AB2(width, j, group))
    if not ncmb(c): break
  return bf #                       >>>>

################################# VGROUP
def vgroup(j, config):
  """Get Vertical Group from «config»"""
  prev = 0
  ls = []
  copy = config[:] # Kakashi Sensei
  copy += [[0]* len(copy[0])] # Sentinel
  N = len(copy)
  for i in range(N):
    dif = copy[i][j] - prev
    prev = dif + prev
    if dif > 0: L = i
    if dif < 0: ls.append(i - L)
  return tuple(ls) #                >>>>

############################## BACKTRACE
def backtrace(D):
  '''First Blood'''
  if debug: import pdb; pdb.set_trace()  
  # [B1 Init]
  n = len(D)
  it = [None]* n
  it[0] = iter(D[0])
  x = [None]* n
  P = [True] *n
  l = 1
  bf = []
  while True: 
    # [B5 Backtrace]
    l -= 1
    if l < 0: return bf #           >>>>
    flag = True
    while flag:
      # [B4 Try Again]
      try: x[l] = next(it[l])
      except StopIteration: break
      while True:
        # [B3 Try]
        if not P[l]: break
        l += 1
        # [B2 ENTA]
        if not l < n:
          bf.append(x[:])
          flag = False
          break
        it[l] = iter(D[l])
        x[l] = next(it[l])

##################################### CK
def ck(config):
  pass

################################## YLAND
def yland():
  '''Main Function'''
  W = Shape[HRZ]
  ls = Const[HRZ]
  D = [rconfig(W, a) for a in ls]
  config = backtrace(D)
  ck(config[0])

########################################
if __name__ == '__main__':
  load('./config')
  yland()

################################### log:
#

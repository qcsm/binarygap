def solution(N):
  str_bin = str(bin(N))[2:]
  str_bin = str_bin.rstrip('0')
  str_bin = str_bin.lstrip('0')
  result = len(sorted(str_bin.split('1'), key=len).pop())
  return result

def subsequences(str)
  arr = str.split('')
  set = {}
  recurse(arr, 0, set)
  set
end

def recurse(arr, start, seen)
  return seen[start] if seen[start]
  # base case
  out = ['']
  return out if start >= arr.length
  rest = recurse(arr, start + 1, seen)
  # without arr[start]
  out = rest
  # with arr[start]
  out += rest.map { |s| arr[start] + s }
  seen[start] = out
end

p subsequences('abcd')
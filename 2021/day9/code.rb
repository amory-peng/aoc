require 'set'

def read_input(filename)
  File.open(filename).readlines.map(&:chomp)
end

def generate_map(file)
  file.map do |line|
    line.split("").map(&:to_i)
  end
end

def oob?(map, coords)
  x, y = coords
  return true if x < 0 || x >= map.length
  return true if y < 0 || y >= map[0].length
  false
end

def solve_1
  file = read_input("day9/input.txt")
  map = generate_map(file)
  risk = 0
  map.each_with_index do |row, i|
    row.each_with_index do |val, j|
      is_low_point = true
      [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]].each do |coords|
        next if oob?(map, coords)
        is_low_point = false if val >= map[coords[0]][coords[1]]
      end
      risk += 1 + val if is_low_point
    end
  end
  risk
end

def solve_2
  file = read_input("day9/input.txt")
  map = generate_map(file)
  low_points = []
  map.each_with_index do |row, i|
    row.each_with_index do |val, j|
      is_low_point = true
      [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]].each do |coords|
        next if oob?(map, coords)
        is_low_point = false if val >= map[coords[0]][coords[1]]
      end
      low_points << [i, j] if is_low_point
    end
  end
  sizes = low_points.map do |low_point|
    dfs(map, low_point)
  end
  sizes.sort.last(3).reduce(&:*)
end

def dfs(map, coords)
  dfs_helper(map, coords, Set.new)
end

def dfs_helper(map, coords, seen)
  coords
  seen << coords
  count = 1
  i, j = coords
  [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]].each do |n_coords|
    next if seen.include?(n_coords) || oob?(map, n_coords) || map[i][j] >= map[n_coords[0]][n_coords[1]] || map[n_coords[0]][n_coords[1]] == 9
    count += dfs_helper(map, n_coords, seen)
  end
  count
end

p solve_1
p solve_2
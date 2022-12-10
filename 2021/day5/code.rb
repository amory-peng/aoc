def parse_input(file)
  file = File.open(file).readlines.map(&:chomp)
  file.map do |str|
    str.split(" -> ").map { |coord| coord.split(",").map(&:to_i) }
  end
end

def fill_map!(coordinates, map, problem = 1)
  coordinates.each do |coordinate_set|
    x1, y1 = coordinate_set[0]
    x2, y2 = coordinate_set[1]
    # same row
    if x1 == x2
      start, stop = y1 >= y2 ? [y2, y1] : [y1, y2]
      start.upto(stop) { |y| map[x1][y] += 1 }
    end
    # same col
    if y1 == y2
      start, stop = x1 >= x2 ? [x2, x1] : [x1, x2]
      start.upto(stop) { |x| map[x][y1] += 1 }
    end
    if problem == 2
      # positive diagonal
      if (x2 - x1) != 0 && (y2 - y1) / (x2 - x1) == 1
        start, stop = x1 >= x2 ? [[x2, y2], [x1, y1]] : [[x1, y1], [x2, y2]]
        until start[0] > stop[0]
          map[start[0]][start[1]] += 1
          start[0] += 1
          start[1] += 1
        end
      end
      # negative diagonal
      if (x2 - x1) != 0 && (y2 - y1) / (x2 - x1) == -1
        start, stop = x1 >= x2 ? [[x2, y2], [x1, y1]] : [[x1, y1], [x2, y2]]
        until start[0] > stop[0]
          map[start[0]][start[1]] += 1
          start[0] += 1
          start[1] -= 1
        end
      end
    end
  end
end

def count_points(map)
  points = 0
  map.each do |row|
    row.each do |col|
      points += 1 if col > 1
    end
  end
  points
end

def solve_1
  coordinates = parse_input("day5/input.txt")
  map = Array.new(1000) { Array.new(1000, 0) }
  fill_map!(coordinates, map)
  p count_points(map)
end

def solve_2
  coordinates = parse_input("day5/input.txt")
  map = Array.new(1000) { Array.new(1000, 0) }
  fill_map!(coordinates, map, 2)
  p count_points(map)
end
solve_1
solve_2
def read_input(file)
  file = File.open(file).readlines.map(&:chomp)
  file.first.split(',').map(&:to_i)
end

def solve(problem = 1)
  positions = read_input("day7/input.txt")
  min = positions.min
  max = positions.max
  min_delta = Float::INFINITY
  curr_delta = 0
  (min..max).each do |final_pos|
    positions.each do |pos|
      steps = (pos - final_pos).abs
      curr_delta += problem == 1 ? steps : steps * (steps + 1) / 2
    end
    min_delta = [curr_delta, min_delta].min
    curr_delta = 0
  end
  min_delta
end

p solve(1)
p solve(2)
def read_input(file)
  file = File.open(file).readlines.map(&:chomp)
  file.first.split(',').map(&:to_i)
end

def get_state(fishes)
  state = Array.new(9, 0)
  fishes.each do |fish|
    state[fish] += 1
  end
  state
end

def tick(state)
  new_fishes = state.shift
  state << new_fishes
  state[6] += new_fishes
end

def solve(num)
  fishes = read_input("day6/input.txt")
  state = get_state(fishes)
  num.times do |i|
    tick(state)
  end
  state.reduce(&:+)
end

p solve(80)
p solve(256)

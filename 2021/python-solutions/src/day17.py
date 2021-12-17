# Advent of Code
# Day 17

def simulate_step(velocity, position):
  new_position = position + velocity
  if velocity.real > 0:
    new_velocity = velocity - 1
  elif velocity.real < 0:
    new_velocity = velocity + 1
  else:
    new_velocity = velocity
  return new_velocity - 1j, new_position

def hit_target(target_x, target_y, position):
  end, hit = False, False
  if target_x[0] <= position.real <= target_x[1] and target_y[0] <= position.imag <= target_y[1]:
    end, hit = True, True
  if position.real > target_x[1]:
    end = True
  if position.imag < target_y[0]:
    end = True
  return end, hit

def find_xv_limit(target_x):
  x, lower_xv, upper_xv = 0, 0, 0
  while x < target_x[0]:
    lower_xv += 1
    x = (lower_xv * (lower_xv + 1)) // 2
  upper_xv = lower_xv
  while x <= target_x[1]:
    upper_xv += 1
    x = (upper_xv * (upper_xv + 1)) // 2
  return lower_xv, upper_xv

def find_max_height(velocity):
  position = 0
  max_height = 0
  hit = False
  while not hit:
    velocity, position = simulate_step(velocity, position)
    if position.imag > max_height:
      max_height = position.imag
    _, hit = hit_target(target_x, target_y, position)
  return int(max_height)
  
def part1(target_x, target_y):
  position, velocity = 0, 0
  valid_velocities = []
  lower_xv, upper_xv = find_xv_limit(target_x)
  for xv in range(lower_xv, upper_xv + 1):
    for yv in range(100):
      position = 0 
      velocity = xv + yv * 1j
      end, hit = False, False
      while not end:
        velocity, position = simulate_step(velocity, position)
        end, hit = hit_target(target_x, target_y, position)
        if hit:
          valid_velocities.append(xv + yv * 1j)

  return max(valid_velocities, key=find_max_height)

def part2(target_x, target_y):
  position, velocity = 0, 0
  valid_velocities = []
  lower_xv, upper_xv = find_xv_limit(target_x)
  for xv in range(lower_xv, upper_xv + 500):
    for yv in range(-300, 300):
      position = 0 
      velocity = xv + yv * 1j
      end, hit = False, False
      while not end:
        velocity, position = simulate_step(velocity, position)
        end, hit = hit_target(target_x, target_y, position)
        if hit:
          valid_velocities.append(xv + yv * 1j)
  return len(valid_velocities)


if __name__ == '__main__':
  with open('input/day17.txt', 'r') as f:
    target_x, target_y = f.read()[12:].strip().split(', ')
  target_x = [int(num) for num in target_x[2:].split('..')]
  target_y = [int(num) for num in target_y[2:].split('..')]

  print('---- Part One ----')
  print(find_max_height(part1(target_x, target_y))) # 4560
  print('---- Part Two ----')
  print(part2(target_x, target_y)) # 3344

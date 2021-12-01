use aoc_runner_derive::{aoc, aoc_generator};

#[aoc_generator(day01)]
fn parse_input(input: &str) -> Vec<i32> {
  input.lines().map(|line| line.parse::<i32>().unwrap()).collect()
}

#[aoc(day01, part1, naive)]
fn naive_part1(input: &[i32]) -> usize {
  let mut last_reading: i32 = 0;
  let mut count = 0;
  for reading in input.iter() {
    if *reading > last_reading {
      count += 1;
    }
    last_reading = *reading;
  }
  count - 1 // Don't count the first reading
}

#[aoc(day01, part1)]
fn solve_part1(input: &[i32]) -> usize {
  input
    .iter()
    .zip(input.iter().skip(1))
    .filter(|(a, b)| b > a)
    .count()
}

#[aoc(day01, part2, naive)]
fn naive_part2(input: &[i32]) -> usize {
  let mut last_sum: i32 = 0;
  let mut count = 0;
  for window in input.windows(3) {
    let sum = window.iter().sum::<i32>();
    if sum > last_sum {
      count += 1;
    }
    last_sum = sum;
  }
  count - 1 // Don't count the first reading
}

#[aoc(day01, part2, zip_trick)]
fn solve_part2(input: &[i32]) -> usize {
  input
    .iter()
    .zip(input.iter().skip(3))
    .filter(|(a, b)| b > a)
    .count()
}

#[cfg(test)]
mod tests {
  use super::*;

  #[test]
  fn sample1() {
    let input = vec![199, 200, 208, 210, 200, 207, 240, 269, 260, 263];
    assert_eq!(solve_part1(&input), 7);
  }
  #[test]
  fn sample2() {
    let input = vec![199, 200, 208, 210, 200, 207, 240, 269, 260, 263];
    assert_eq!(solve_part2(&input), 5);
  }
}

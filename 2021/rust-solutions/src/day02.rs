use std::panic;

use aoc_runner_derive::{aoc, aoc_generator};

#[aoc_generator(day02)]
fn parse_input(input: &str) -> Vec<(String, u32)> {
  input
    .lines()
    .map(|line| {
      let mut split = line.split(' ');
      (
        split.next().unwrap().to_string(),
        split.next().unwrap().parse().unwrap(),
      )
    })
    .collect()
}

#[aoc(day02, part1)]
fn solve_part1(moves: &[(String, u32)]) -> u32 {
  let mut pos = (0, 0);
  for step in moves {
    match step.0.as_str() {
      "forward" => pos.0 += step.1,
      "up" => pos.1 -= step.1,
      "down" => pos.1 += step.1,
      x => panic!("Unknown direction {}", x),
    }
  }
  pos.0 * pos.1
}

#[aoc(day02, part2)]
fn solve_part2(moves: &[(String, u32)]) -> u32 {
  let mut pos = (0, 0);
  let mut aim = 0;
  for step in moves {
    match step.0.as_str() {
      "forward" => {
        pos.0 += step.1;
        pos.1 += aim * step.1;
      },
      "up" => aim -= step.1,
      "down" => aim += step.1,
      x => panic!("Unknown direction {}", x),
    }
  }
  pos.0 * pos.1
}

#[cfg(test)]
mod tests {
  use super::*;

  #[test]
  fn test_solve_part1() {
    let input = parse_input(
      "forward 5\ndown 5\nforward 8\nup 3\ndown 8\nforward 2\n"
    );
    assert_eq!(solve_part1(&input), 150);
  }

  #[test]
  fn test_solve_part2() {
    let input = parse_input(
      "forward 5\ndown 5\nforward 8\nup 3\ndown 8\nforward 2\n"
    );
    assert_eq!(solve_part2(&input), 900);
  }
}

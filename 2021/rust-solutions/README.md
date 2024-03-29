# Rust

Why not dip my toes into Rust this year after all?

## Usage notes

- `cargo aoc input` will download an input and store it in `input/{year}/day_{day}.txt`. (Specify other day with `cargo aoc input -d {day} -y {year}`).
- `cargo aoc` will run the latest implented day
- `cargo bench` will run the suite of benchmarks


## Day 01 - Sonar Sweep

What a struggle. The learning curve feels incredibly steep for Rust, not helped by the fact that I had some issues stemming from updating to macOS Monterey last night requiring that I run `xcode-select --install` to reinstall all the dev tools.
Additionally I ran into some problems where `rust-analyzer` wasn't playing nicely with my project due to the `Cargo.toml` not being at the root level. I solved this by creating `.vscode/settings.json` locally and adding:

```
{
  "rust-analyzer.linkedProjects": [
    "./2021/rust-solutions/Cargo.toml",
  ],
}
```

The final problem I was running into was a warning being thrown due to the `cargo aoc` CLI tool that I was using producing some kind of `macro-error`. I still don't really understand what the issue is as the project is building just fine so I also added another rule to the rust-analyzer config to suppress this. 

```
"rust-analyzer.diagnostics.disabled": [
  "macro-error"
]
```

Finally, with all the teething issues sorted out I was able to make a start on actually trying to solve this thing in Rust. I ended up implementing two solutions for each part - a naive solution, and 1 using the zip trick which I discovered afterwards on the subreddit. Interestingly enough the naive solutions were noticeably quicker in my benchmarking:

```
Day1 - Part1/(default)  time:   [1.8941 us 1.9007 us 1.9073 us]
Day1 - Part1/naive      time:   [943.80 ns 946.75 ns 950.07 ns]
Day1 - Part2/zip_trick  time:   [1.8892 us 1.8942 us 1.8996 us]
Day1 - Part2/naive      time:   [1.6386 us 1.6427 us 1.6473 us]
```

## Day 02 - Dive!

Round 2 versus the Rust compiler and I am taking a beating. Many errors seem to be stemming from my use of the `cargo-aoc` crate because honestly I don't yet understand well enough how it works under the hood to make sense of the mysterious errors that I seem to get. Today was an issue where rust 'expected a named lifetime parameter` for the runner function which I was eventually able to fix by refactoring my generator function and updating the type of my input arguments.

The logic for the solutions was pretty straightforward, things are going nice and smoothly in that department for the time being. I didn't attempt anything fancy as I spent more than enough time just trying to get to the right syntax.

Did some benchmarks again but without any different implentations using clever tricks to compare them to they feel a little bit pointless. It would be nice to come back and try a more functional approach later if I get some time.

```
Day2 - Part1/(default)  time:   [1.2693 us 1.2773 us 1.2859 us]
Day2 - Part2/(default)  time:   [1.3037 us 1.3108 us 1.3189 us]
```

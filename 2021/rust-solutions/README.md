# Rust

Why not dip my toes into Rust this year after all?

## Usage notes

- `cargo aoc input` will download an input and store it in `input/{year}/day_{day}.txt`. (Specify other day with `cargo aoc input -d {day} -y {year}`).
- `cargo aoc` will run the latest implented day


## Day 01

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

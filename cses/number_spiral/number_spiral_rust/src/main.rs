use std::cmp::max;
use std::io::{self, BufRead};

fn get_value(x: i64, y: i64) -> i64 {
    let m = max(y, x);
    let value: i64 = m * (m - 1) + 1 + (y - x) * (m % 2 * -2 + 1);
    value
}

fn main() {
    let mut input = String::new();
    let mut stdin = io::stdin().lock();
    stdin.read_line(&mut input).unwrap();
    let n: i32 = input
        .trim()
        .parse()
        .expect("please give me correct string number!");
    for _ in 0..n {
        input.clear();
        stdin.read_line(&mut input).unwrap();
        let pos: Vec<i64> = input
            .split_whitespace()
            .map(|a| -> i64 { a.trim().parse().unwrap() })
            .collect();
        let (y, x) = (pos[0], pos[1]);
        println!("{}", get_value(x, y));
    }
}

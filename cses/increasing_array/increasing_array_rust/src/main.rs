use std::cmp::max;
use std::io::stdin;
use std::iter::zip;

fn get_min_moves(numbers: Vec<i64>) -> i64 {
    let mut min_moves = 0;
    let mut change: i64 = 0;
    for (i, j) in zip(&numbers[..numbers.len() - 1], &numbers[1..]) {
        change = max(0, i - j + change);
        min_moves += change;
    }
    min_moves
}

fn main() {
    let mut input = String::new();
    stdin().read_line(&mut input).unwrap();
    let _n: usize = input.trim().parse().unwrap();
    input = String::new();
    stdin().read_line(&mut input).unwrap();
    let numbers: Vec<i64> = input
        .split(' ')
        .map(|x| -> i64 { x.trim().parse().unwrap() })
        .collect();
    println!("{}", get_min_moves(numbers));
}

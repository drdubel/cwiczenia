use std::io::stdin;

fn get_permutation(n: i32) {
    if 1 < n && n < 4 {
        println!("NO SOLUTION");
    } else {
        for i in (2..n + (n - 1) % 2).step_by(2) {
            print!("{} ", i);
        }
        for i in (1..n + n % 2).step_by(2) {
            print!("{} ", i);
        }
    }
}

fn main() {
    let mut user_input = String::new();
    let _ = stdin().read_line(&mut user_input);
    let n: i32 = user_input
        .trim()
        .parse()
        .expect("please give me correct string number!");
    get_permutation(n);
}

use std::io::stdin;

fn collatz(mut n: i64) {
    while n != 1 {
        print!("{} ", n);
        if n % 2 == 1 {
            n = n * 3 + 1;
        } else {
            n /= 2;
        }
    }
    print!("{}", n);
}

fn main() {
    let mut user_input = String::new();
    let _ = stdin().read_line(&mut user_input);
    let n = user_input
        .trim()
        .parse()
        .expect("please give me correct string number!");

    collatz(n);
}

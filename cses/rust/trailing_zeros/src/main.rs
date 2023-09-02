use std::io::stdin;

fn get_tra_zeros_len(mut n: i32) -> i32 {
    let mut m = 0;
    while n > 0 {
        n /= 5;
        m += n;
    }
    m
}

fn main() {
    let mut input = String::new();
    stdin().read_line(&mut input).unwrap();
    let n: i32 = input
        .trim()
        .parse()
        .expect("please give me correct string number!");

    print!("{}", get_tra_zeros_len(n));
}

use std::io::stdin;

fn main() {
    let mut word = String::new();
    stdin().read_line(&mut word).unwrap();
    let mut prev_char = ' ';
    let mut substring_len = 0;
    let mut max_substring_len = 1;
    word.trim().chars().for_each(|chr| {
        if chr == prev_char {
            substring_len += 1;
            if substring_len > max_substring_len {
                max_substring_len = substring_len;
            }
        } else {
            substring_len = 1;
        }
        prev_char = chr;
    });
    print!("{}", max_substring_len);
}

use itertools::Itertools;
use std::fs;

const BUFF: usize = 14;

fn main() {
    let input: String = fs::read_to_string("./test.txt").expect("File could not be read");

    let marker = input
        .chars()
        .collect_vec()
        .windows(BUFF)
        .enumerate()
        .filter(|(_, w)| w.iter().all_unique())
        .map(|(i, _)| i + BUFF )
        .next().unwrap();

    println!("{}", marker);
}

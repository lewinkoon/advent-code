use std::fs;

fn main() {
    let input = fs::read_to_string("./input.txt").expect("File could not be read");

    let vec: Vec<&str> = input.split("\n").collect();

    fn priority(c: char) -> i32 {
        match c {
            'a'..='z' => c as i32 - 96,
            'A'..='Z' => c as i32 - 64 + 26,
            _ => 0,
        }
    }

    let mut sum_one: i32 = 0;
    for rucksack in &vec {
        let (a, b) = rucksack.split_at(rucksack.len() / 2);
        let letter = a.chars().find(|c| b.contains(*c)).unwrap();
        sum_one += priority(letter)
    }

    let mut sum_two = 0;
    for i in (0..vec.len()).step_by(3) {
        let (a, b, c) = (&vec[i], &vec[i + 1], &vec[i + 2]);
        let letter = c
            .chars()
            .find(|c| a.contains(*c) && b.contains(*c))
            .unwrap();
        sum_two += priority(letter);
    }

    // answers
    let ans_one = sum_one;
    let ans_two = sum_two;

    println!("\nAnswers:\n");
    println!("a) {} priorities\n", ans_one);
    println!("b) {} priorities\n", ans_two);
}

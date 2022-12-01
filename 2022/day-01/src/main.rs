use std::fs;

fn main() {
    let input = fs::read_to_string("./src/input.txt").expect("File could not be read");

    let mut list = vec![];

    for elf in input.split("\n\n") {
        let mut total = 0;
        for calories in elf.lines() {
            total += calories.parse::<i32>().unwrap();
        }
        list.push(total);
    }

    println!("{:?}", list.iter().max().unwrap());
}
use std::fs;

fn main() {
    let input = fs::read_to_string("./src/input.txt").expect("File could not be read");

    // total calories for each elf
    let mut list = vec![];
    for elf in input.split("\n\n") {
        let mut total = 0;
        for calories in elf.lines() {
            total += calories.parse::<i32>().unwrap();
        }
        list.push(total);
    }

    // sort in reverse order
    list.sort();
    list.reverse();


    // answers
    let ans_one: i32 = list[0];
    let ans_two: i32 = list[..3].iter().sum();

    println!("\nAnswers:\n");
    println!("a) {:?} calories\n", ans_one);
    println!("b) {:?} calories\n", ans_two);
}
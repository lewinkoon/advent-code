use std::fs;

fn main() {
    let input = fs::read_to_string(r#"./input.txt"#).expect("File could not be read");

    let mut score_a = 0;
    let mut score_b = 0;
    for round in input.split("\n") {
        for shape in round.split("\n") {
            match shape {
                "B X" => {score_a += 1; score_b += 1},
                "C Y" => {score_a += 2; score_b += 6},
                "A Z" => {score_a += 3; score_b += 8},
                "A X" => {score_a += 4; score_b += 3},
                "B Y" => {score_a += 5; score_b += 5},
                "C Z" => {score_a += 6; score_b += 7},
                "C X" => {score_a += 7; score_b += 2},
                "A Y" => {score_a += 8; score_b += 4},
                "B Z" => {score_a += 9; score_b += 9},
                _ => println!("Error")
            }
        }
    }

    let ans_one = score_a;
    let ans_two = score_b;

    println!("\nAnswers:\n");
    println!("a) {} points\n", ans_one);
    println!("b) {} points\n", ans_two);
}

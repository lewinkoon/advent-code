use std::fs;

fn main() {
    let input: String = fs::read_to_string("./input.txt").expect("File could not be read");

    let mut sum_one: i32 = 0;
    let mut sum_two: i32 = 0;
    for line in input.lines() {
        let section: Vec<u32> = line
            .split(&[',', '-'])
            .map(|x| x.parse::<u32>().unwrap())
            .collect();

        // println!("{:?}", section);

        if (section[0] <= section[2] && section[1] >= section[3])
            || (section[2] <= section[0] && section[3] >= section[1])
        {
            sum_one += 1;
        }

        if (section[1] >= section[2]) && (section[0] <= section[3])
        {
            sum_two += 1;
        }
    }

    println!("\nAnswers:\n");
    println!("a) {} pairs\n", sum_one);
    println!("b) {} overlaps\n", sum_two);
}

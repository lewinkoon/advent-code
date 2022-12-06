use itertools::Itertools;
use std::{fs, usize};

const STACKS: usize = 9;

pub fn main() {
    let input = fs::read_to_string("./input.txt").expect("File not read");
    let (boxes, moves) = input.split_once("\n\n").unwrap();
    let mut stack_one: [Vec<char>; STACKS] = Default::default();
    let (mut stack_two, mut swp): ([Vec<char>; STACKS], [char; 64]) =
        (Default::default(), ['0'; 64]);

    boxes.lines().rev().skip(1).for_each(|l| {
        l.chars()
            .skip(1)
            .step_by(4)
            .enumerate()
            .filter(|(_, c)| !c.is_whitespace())
            .for_each(|(i, c)| {
                stack_one[i].push(c);
                stack_two[i].push(c)
            })
    });

    moves.lines().for_each(|l| {
        let (n, a, b) = l
            .split_whitespace()
            .skip(1)
            .step_by(2)
            .map(|c| c.parse().unwrap())
            .collect_tuple()
            .unwrap();

        for _ in 0..n {
            let tmp = stack_one[a as usize - 1].pop().unwrap();
            stack_one[b as usize - 1].push(tmp);
        }

        let len = stack_two[a as usize - 1].len();
        let swp = &mut swp[..n as usize];

        swp.copy_from_slice(&stack_two[a as usize - 1][len - n as usize..len]);
        stack_two[a as usize - 1].truncate(len - n as usize);
        stack_two[b as usize - 1].extend(swp.iter());
    });

    stack_one
        .iter()
        .for_each(|s| print!("{}", *s.last().unwrap() as char));
    println!();

    stack_two
        .iter()
        .for_each(|s| print!("{}", *s.last().unwrap() as char));
    println!();
}

use rand::Rng;
use std::io;

fn main() {
    println!("Guess a number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    println!("Please input your guess. {secret_number}");

    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("Faild to read line");

    let guess: u32 = guess
        .trim()
        .parse()
        .expect("Could not parse guess input to number");

    println!("You guessed: {guess}");
}

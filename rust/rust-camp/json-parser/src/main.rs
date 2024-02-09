use std::{fs::File, path::PathBuf, process::exit};

use clap::Parser;
use serde_json::Value;

/// Simple program to greet a person
#[derive(Parser, Debug)]
#[command(author, version, about, long_about = None)]
struct Args {
    #[arg(short, long)]
    json: PathBuf,
}

fn main() {
    let args = Args::parse();

    println!("Path: {:#?}", args);

    if !args.json.exists() {
        eprintln!("file does not exist!");
        exit(1);
    }

    let file: File = File::open(args.json).unwrap();
    let res: Result<Value, _> = serde_json::from_reader(file);

    match res {
        Ok(value) => println!("It's valid json: {:?}", value),
        Err(error) => eprintln!("Failed to validate: {error}"),
    }
}

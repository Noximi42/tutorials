pub use crate::math::add;

mod math {
    pub fn add(a: i32, b: i32) -> i32 {
        a + b
    }
}

pub fn foo() {
    let mut name: String = String::new();

    enter_name(&mut name);

    println!("This is me: {name}");
}

fn enter_name(name: &mut String) {
    name.push_str("Mattes");
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn should_work() {
        assert_eq!(add(1, 2,), 3);
    }
}

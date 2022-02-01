use std::fmt;

#[derive(Debug)]
struct Person {
    name: String,
    age: u8
}
// Essentially implementing 'to string' for this object.
impl fmt::Display for Person {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}:{}", self.name, self.age)
    }
}
fn main(){
    let age = 27;
    println!("{} {}", "Format Test", 31i32);
    println!("{} {name}", "My Name Is", name="Warren");
    println!("I am {age:b} years old({age} in Decimal)", age=age);
    #[derive(Debug)]
    struct Structure(i32);
    println!("Let's take a look at this Structure: \t {:?}", Structure(28)); // We Need the '?' for debugging custom object types (structs)
    let warren = Person{name: "Warren".to_string(), age: 27};
    println!("{}", warren)
}

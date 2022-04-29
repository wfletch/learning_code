use std::collections::HashMap;
//Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

//You may assume that each input would have exactly one solution, and you may not use the same element twice.

//You can return the answer in any order.
//
fn main(){
    let mut num_to_index: HashMap<i32, i32> = HashMap::new(); 
    let nums: [i32; 4] = [2,7,11,15];
    let target = 9;
    let mut cur_index = 0;
    let mut other_index = 0;
    let mut found = 0;
    // Linear Time Solution. Run through array and hash each entry to it's index.
    // Check if the corresponding vaue we want is in the hash map at each iteration
    for num in nums.iter(){
        //Same Element cannot be used twice!
        // 1. Check if reciprocol value exists
        // 2. If it does. Great, We are done
        let recip = target - num;
        if num_to_index.contains_key(&recip) {
            other_index = num_to_index[&recip];
            found = 1;
            break;
        } else {
            num_to_index.insert(*num, cur_index);
            cur_index+=1;
        }
    }
    if found == 1{
        println!("{},{}", cur_index, other_index);
    } else {
        println!("{}", "Not Found");
    }
}

// Coding Problems are a great way to learn a new language. However... python is just fucking great
// when it comes to coding problems.

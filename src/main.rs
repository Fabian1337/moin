fn day29() {
    let mut moin = String::from("МойнМойн");
    moin.retain(|s| s != 'й');
    moin.push('i');
    moin.push('n');
    let (mo, mut __in) = moin.split_at(2);
    let (_, mut _in) = __in.split_at(6);
    let mut ___in = String::from(_in);
    let mut _mo = String::from(mo);
    ___in.retain(|s| s != 'н');
    _mo.insert(0, 'm');
    _mo.retain(|s| s != 'М');
    println!("{}{}", _mo.to_lowercase(), ___in);
}

fn main() {
    day29()
}

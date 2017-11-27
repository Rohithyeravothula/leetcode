function weeblyInt(input){
	if(input == "" || input.indexOf(".") != -1){
		return NaN;
	}
	i=0;
	var sign = 1;
	if(input[i] == "-")
		{
			sign=-1;
			i+=1;
		}
	var n = 0;
	var l=input.length;
	var code;
	while(i<l){
		code = input[i].charCodeAt() - '0'.charCodeAt();
		if (code > 9 || code < 0)
			return NaN;
		n=n*10+code;
		i+=1;
	}
	return sign*n;
}

function weeblyFloat(input){
	var left_split = input.split(".")[0];
	var right_split = input.split(".")[1];
	var sign = 1;
	if(left_split[0] == "-")
		{
			sign = -1;
			left_split = left_split.substr(1);
		}

	var left = weeblyInt(left_split);
	var right = weeblyInt(right_split);
	var right_lenth = right_split.length;

	if(left_split == "")
		left = 0;

	if(right == NaN || left == NaN)
		return NaN;
	var right_decimal = right / Math.pow(10, right_lenth);
	console.log();
	if(left < 0)
		return left - right_decimal;
	return sign*(left + right_decimal);
}	

// test cases
console.log(weeblyFloat("-32.78"));
console.log(weeblyFloat("-32.78a"));
console.log(weeblyFloat("-32a.78"));
console.log(weeblyFloat(".78"));
console.log(weeblyFloat("-0.78"));
console.log(weeblyFloat("-32."));
console.log(weeblyFloat("32.001"));
console.log(weeblyFloat("32.001000"));
console.log(weeblyFloat("-32.1234"));
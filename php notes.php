<?php
/*

*/


// Array Notes

$x = [1,2,3,];
$y = [1,$x];
print_r($y);
$y[1][0] = 0;
print_r($x);
$x = [1,2,3];
print_r($y);
implode($glue, $pieces)
join($glue, $pieces)
lcfirst($str)	Converts the first character of a string to lowercase

ltrim($str [, $character_mask])	Removes whitespace or other characters from the left side of a string

str_repeat($input, $mult)	Repeats a string a specified number of times
str_replace($search, $replace, $subject [, &$replace_count])	Replaces some characters in a string (case-sensitive)

strlen($str)	Returns the length of a string

ucfirst($str)	Converts the first character of a string to uppercase
ucwords($str [, $delimiters])s	Converts the first character of each word in a string to uppercase

explode($separator, $str [, $limit])	Breaks a string into an array
str_split($str [, $split_length]) Splits a string into an array
strpos($haystack, $needle [, $offset])	Returns the position of the first occurrence of a string inside another string (case-sensitive)
strrchr($haystack, $needle)	Finds the last occurrence of a string inside another string
strrev($str)	Reverses a string
strripos($haystack, $needle [, $offset])	Finds the position of the last occurrence of a string inside another string (case-insensitive)
strrpos($haystack, $needle [, $offset])	Finds the position of the last occurrence of a string inside another string (case-sensitive)
strspn($str, $mask [, $start, $len])	Returns the number of characters found in a string that contains only characters from a specified charlist
strstr($haystack, $needle [, $part])	Finds the first occurrence of a string inside another string (case-sensitive)
strrev($str)	Reverses a string
echo str_replace("world","Peter","Hello world!");

parse_str("name=Peter&age=43",$myArray);
substr($str, $start [, $length])	Returns a part of a string

array_chunk($arg, $size [, $preserve_keys])	Splits an array into chunks of arrays
array_combine($keys, $values)	Creates an array by using the elements from one "keys" array and one "values" array
array_combine($keys, $values)	Creates an array by using the elements from one "keys" array and one "values" array
array_count_values($arg)	Counts all the values of an array
array_diff($arr1, $arrays...)	Compare arrays, and returns the differences (compare values only)
array_diff_assoc($arr1, $arrays...)	Compare arrays, and returns the differences (compare keys and values)
array_diff_key($arr1, $arrays...)	Compare arrays, and returns the differences (compare keys only)


array_intersect($arr1, $arrays...)	Compare arrays, and returns the matches (compare values only)
array_intersect_assoc($arr1, $arrays...)	Compare arrays and returns the matches (compare keys and values)
array_map($callback, $arrays...)	Sends each value of an array to a user-made function, which returns new values

array_merge($arr1 [, $arrays...])	Merges one or more arrays into one array
array_merge_recursive($arr1 [, $arrays...])	Merges one or more arrays into one array recursively
$a1=array("a"=>"red","b"=>"green");
$a2=array("c"=>"blue","b"=>"yellow");
print_r(array_merge_recursive($a1,$a2)); Array ( [a] => red [b] => Array ( [0] => green [1] => yellow ) [c] => blue )
print_r(array_merge($a1,$a2)); Array ( [a] => red [b] => yellow [c] => blue )

array_pop(&$stack)	Deletes the last element of an array
array_product($arg)	Calculates the product of the values in an array
array_push(&$stack, $vars...)	Inserts one or more elements to the end of an array
array_rand($arg [, $num_req])	Returns one or more random keys from an array

array_reduce($arg, $callback [, $initial])	Returns an array as a string, using a user-defined function
array_replace($arr1 [, $arrays...])	Replaces the values of the first array with the values from following arrays
array_replace_recursive($arr1 [, $arrays...])	Replaces the values of the first array with the values from following arrays recursively
array_reverse($input [, $preserve_keys])	Returns an array in the reverse order
array_search($needle, $haystack [, $strict])	Searches an array for a given value and returns the key
array_shift(&$stack)	Removes the first element from an array, and returns the value of the removed element
array_slice($arg, $offset [, $length, $preserve_keys])	Returns selected parts of an array
array_splice(&$arg, $offset [, $length, $replacement])	Removes and replaces specified elements of an array
array_sum($arg)	Returns the sum of the values in an array
 unset($arr[$index]);
array_unique($arg [, $flags])	Removes duplicate values from an array
array_unshift(&$stack, $vars...)	Adds one or more elements to the beginning of an array
array_values($arg)	Returns all the values of an array

count($var [, $mode])	Returns the number of elements in an array

arsort(&$arg [, $sort_flags])	Sorts an associative array in descending order, according to the value
asort(&$arg [, $sort_flags])	Sorts an associative array in ascending order, according to the value
in_array($needle, $haystack [, $strict])	Checks if a specified value exists in an array
sizeof($var [, $mode])	Alias of count
sort(&$arg [, $sort_flags])	Sorts an indexed array in ascending order
uasort(&$arg, $cmp_function)	Sorts an array by values using a user-defined comparison function
uksort(&$arg, $cmp_function)	Sorts an array by keys using a user-defined comparison function
usort(&$arg, $cmp_function)	Sorts an array using a user-defined comparison function
shuffle(&$arg)	Shuffles an array

range($low, $high [, $step])	Creates an array containing a range of elements
Syntax
array_fill(index, number, value)
Parameter Values
Parameter	Description
index	Required. The first index of the returned array
number	Required. Specifies the number of elements to insert
value	Required. Specifies the value to use for filling the array

function test_odd($var)
  {
  return($var & 1);
  }

$a1=array(1,3,2,3,4);
print_r(array_filter($a1,"test_odd"));
$a1=array("a"=>"red","b"=>"green","c"=>"blue","d"=>"yellow");

$result=array_flip($a1);
Array ( [red] => a [green] => b [blue] => c [yellow] => d )

$x = " hlloe world";
echo $x;
print_r(str_split($x));
foreach (str_split($x) as $index => $char) {
  // code...
  if($index == 0 || $x[$index-1] == ' '){
    $x[$index] = ucfirst($x[$index]);
  }
}
echo $x;

json_encode($value [, $options, $depth])
json_decode($json [, $assoc, $depth, $options])

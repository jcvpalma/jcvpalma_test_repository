<?php

//We have an array with values like [1,2,3,4,5]

//When we perform d=4 left rotations, the array undergoes the following sequence of changes:
//[1,2,3,4,5] -> [2,3,4,5,1] -> [3,4,5,1,2] -> [4,5,1,2,3] -> [5,1,2,3,4]
//so, we have the parameter d that is the last

$vetor = [1,2,3,4,5];

$d = 4;

for($i=0;$i<$d;$i++){
    //for each iterator I should left to the next position array
    $v = [];
    //for($j=0;$j<sizeof($vetor);$j++){
    $vetor = dequeue_array($vetor);
    print_r($vetor);
    //}
    echo "<br>";
}

function dequeue_array($arr_in){
    //get first and remove it
    $s_first = $arr_in[0];
    array_shift($arr_in);
    array_push($arr_in, $s_first);
    return $arr_in;

}

?>
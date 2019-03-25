<?php
$vetor = array(1, array(3,5), array(7,6,9));
$reorder = array();

foreach($vetor as $key => $val){
    if(gettype($val) == "array"){
        foreach($val  as $k => $v){
            array_push($reorder, $v);
        }
    } else {
        array_push($reorder, $val);
    }
}

array_multisort($reorder, SORT_ASC, SORT_NUMERIC);

var_dump($reorder);

?>
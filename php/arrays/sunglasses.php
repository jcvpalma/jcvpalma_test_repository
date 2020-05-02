<?php


function sunglasses_test($arr){

	for($i=0;$i<sizeof($arr);$i++){
		//echo $i . " - " . ($i+(sizeof($vetor)/2)) . "<br>";
		for($j=0;$j<sizeof($arr[$i]);$j++){
	
			if(($i+(sizeof($arr)/2)) <7 ){
	
				if (($j+(sizeof($vetor[$i])/2))<7){
	
					$i_start = $i;
					$i_finish = ($i+(sizeof($arr)/2));
					$j_start = $j;
					$j_finish = ($j+(sizeof($arr[$i])/2));
	
					extract_sunglasses($i_start, $i_finish, $j_start, $j_finish, $arr);
				}
				echo "<br>";	
			}
		}
	}
}

function extract_sunglasses($i_start, $i_finish, $j_start, $j_finish, $vetor){
	$v = [];
	$total = 0;
	for($i=$i_start;$i<$i_finish;$i++){
		for($j=$j_start;$j<$j_finish;$j++){
			$v[$i][] = $vetor[$i][$j];
		}
	}

	for($i=0;$i<sizeof($v);$i++){
		for($j=0;$j<sizeof($v[$i]);$j++){
			if(($i == 1 && $j == 0) || ($i == 1 && $j == 2)) {
				$v[$i][$j] = 0;	
			}
			echo $v[$i][$j] . "\t";
			$total += $v[$i][$j];

		}
		echo "<br>";
	}
	echo "Total: $total<br>";
	
}


$vetor = [
	[1,3,1,0,4,1],
	[0,2,0,0,1,0],
	[1,1,1,1,0,1],
	[2,1,0,0,1,0],
	[0,1,0,0,1,0],
	[2,8,9,6,2,3],
];


sunglasses_test($vetor);

?>
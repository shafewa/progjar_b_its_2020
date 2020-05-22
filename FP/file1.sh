read n
temp=$(($number+n))
echo $temp

moref= `cp http.py http${temp}.py`
echo $moref

 
number=$temp



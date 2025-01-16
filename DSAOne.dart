//Moving the zeros to the end of the array
import 'dart:ffi';
class DSAOne{
  var array=[1,2,3,4,0,9,8,0];
  

}
void MoveZeros(var array){
  int j=0;
    for(int i=0;i<array.length();i++){
       if(array[i]!=0){
        array[j]=array[i];
        j++;
       }
    }
    while(j<array.length())
    {
      array[j]=0;
      j++;
    }
    
}
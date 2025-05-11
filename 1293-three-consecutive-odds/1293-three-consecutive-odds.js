/**
 * @param {number[]} arr
 * @return {boolean}
 */
var threeConsecutiveOdds = function(arr) {
    // sliding window
    if (arr.length < 3){
        return false
    }
    for(let i=0;i<arr.length-2;i++){
        if (arr[i]%2==1 && arr[i+1]%2==1 && arr[i+2]%2==1)
            return true
    }
    return false
};
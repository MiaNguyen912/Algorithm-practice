/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    // M1: Traverse the entire prototype chain until we find a match or else return False. O(n)
    while(obj!=null){
        if(obj.constructor === classFunction)
            return true;
        obj = Object.getPrototypeOf(obj); // inheritance is achieved with the prototype chain
    }
    return false;

    // M2: use Object wrapper to make obj object-like 
    // If it’s a primitive (e.g. string, number), it’s wrapped in an object wrapper (e.g., "hi" becomes new String("hi")).
    if (obj == null || typeof classFunction !== 'function' ) return false;
    return Object(obj) instanceof classFunction;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */
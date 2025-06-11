// 'use strict';

// const a = 'строка';
// const b = 42;  // число 
// const c = true;
// const d = null;
// let e;
// const f = {x: 1};
// const g = [1, 2, 3];
// console.log(a)
// console.log(typeof a)
// console.log('')
// console.log(b)
// console.log(typeof b)
// console.log('')
// console.log(c)
// console.log(typeof c)
// console.log('')
// console.log(d)
// console.log(typeof d)
// console.log('')
// console.log(e)
// console.log(typeof e)
// console.log('')
// console.log(f['x'])
// console.log(f.x)
// console.log(typeof f)
// console.log('')
// console.log(g[1])
// console.log(typeof g)



// a = new Boolean('false');
// console.log(a == '');  //  true
// console.log(a);
// console.log(typeof a);
// console.log(a.valueOf());
// console.log(a.toString());
// console.log('end')

// let x;  
// console.log([] == 0);  // true
// console.log([] == false);  // true
// console.log([] == x);  // false
// console.log('');
// console.log(0 == false);  // true
// console.log(0 == x);  // false
// console.log('');
// console.log(x == false);  // false
// console.log(null == x);  // true
// console.log([] == null);  // false
// console.log(0 == null);  // false
// console.log(null == false);  // false
// console.log([] === []);
// console.log([1] === [1]);
// console.log({} === {});
// console.log(NaN === NaN);
// console.log(null === undefined);  
// console.log([[]] < [[]])   // false
// console.log([[]] == [[]])  // false
// console.log([] > 0);                                                       // false                   false                                                                                                                                                                                   
// console.log([0] < 1);                                                      // true                    true                                                                                         
// console.log([1] < 2);                                                      // true                    true                                                                                         
// console.log([1,2] < '1,2');                                                // false                   false                                                                                                
// console.log([1,2] <= '1,2');                                               // true                    true                                                                                               
// console.log([1,2] < '1.2');                                                // ??                      true                                                                                             
// console.log([1,2] < true);                            // nan < 1           // false                   false                                                                                               
// console.log([1,2] > true);                            // nan > 1           // false                   false                                                                                               
// console.log([null] < 1);                                                   // true                    true                                                                                            
// console.log([undefined] < 1);                                              // true                    true                                                                                                 
// console.log([[]] < 1);                                                     // true                    true                                                                                          
// console.log([''] < 1);                                                     // true                    true                                                                                          
// console.log([' '] < 1);                                                    // true                    true                                                                                           
// console.log(['\n'] < 1);                                                   // true                    true                                                                                            
// console.log(['0'] < 1);                                                    // true                    true                                                                                           
// console.log(['false'] < 1);                                                // false                   false                                                                                                
// console.log({} < 1);                                                       // false                   false                                                                                         
// console.log({ toString: () => '2' } < 3);                                  // true                    true                                                                                                             
// console.log({ valueOf: () => 2 } < 3);                                     // true                    true                                                                                                          
// console.log({ toString: () => '2', valueOf: () => '1' } < 2);              // true                    true                                                                                                                                 

// console.log('0' == 0)	 // true	true	✅                                                                                                
// console.log(false == 'false')	 // false	false	✅                                                           
// console.log([null] == '')	 // false	false	                                        true                   
// console.log(undefined == null)	 // true	true	✅                                                           
// console.log([] == [])	 // false	false	✅                                                           
// console.log([0] == false)	 // true	true	✅                                                           
// console.log(' \n\t ' == 0)	 // true	true	✅                                                           
// console.log('42' == true)	 //false	false	✅                                                           
// console.log('' == false)   //true	true	✅                                                           
// console.log([''] == 0)	 // true	true	✅                                                           
// console.log([undefined] == 0)	 // true	true	✅                                                           
// console.log([undefined] == '')	 // true	true	✅                                                           
// console.log([null] == 0)	 // false	false	✅                                      true                     
// console.log([null] == '')	 // false	false	✅                                      true                     
// console.log(['0'] == false)	 // true	true	✅                                                           
// console.log([[]] == '')	 // true	true	✅                                                           
// console.log(['\n'] == 0)	 // true	true	✅                                                           
// console.log(new Boolean(false) == false)	 // false	false	✅                                                           
// console.log(new String('') == '')	// true	false	❌                                                           
// console.log(NaN == NaN)  // false                                                           
// console.log([] == 0);                   // 1     true      true                                              
// console.log([1] == true);              // 2      true      true                                          
// console.log([2] == '2');               // 3      True      true                                  
// console.log([null] == null);          // 4       False     false                                  
// console.log([undefined] == undefined); // 5      False     false                                   
// console.log([[]] == false);           // 6       True      true                                 
// console.log(['false'] == false);      // 7       False     false                                  
// console.log([null] == false);         // 8       True      true                                 
// console.log([undefined] == false);    // 9       True      true                                 
// console.log(Boolean('false') == false); // 10    False     false                                     
// console.log([1,2] == '1,2');           // 11     True      true                                   
// console.log([1,2] == true);           // 12      False     false                                   
// console.log([1] == '1');              // 13      True      true                                  
// console.log(['1'] == 1);              // 14      True      true                                  
// console.log(['1'] == true);           // 15      True      true                                  
// console.log(['0'] == 0);              // 16      True      true                                  
// console.log([0,0] == '0,0');           // 17     True      true                                   
// console.log([0,0] == 0);              // 18      False     false                                   
// console.log([1,2,3] == '1,2,3');       // 19     True      true                                   
// console.log([] + {} == {} + []);          // True        

// console.log("1" + 1);       // "11"                                                   11                                                                    
// console.log(1 + "1");       // "11"                                                   11                          
// console.log("1" + true);    // "1true"                                                1true                             
// console.log("1" + null);    // "1null"                                                1null                             
// console.log("1" + undefined); // "1undefined"                                         1undefined                                    
// console.log("1" + {});      // "1[object Object]"                                     1[object Object]                                        
// console.log("1" + [2, 3]);  // "12,3"                                                 12,3                            
// console.log(1 + 1);         // 2                                                      2                       
// console.log(1 + true);      // 2                                                      2                       
// console.log(1 + null);      // 1                                                      1                       
// console.log(1 + undefined); // NaN                                                    NaN                         
// console.log(1 + {});        // "1[object Object]"                                     1[object Object]                                        
// console.log(1 + [2, 3]);    // "12,3"                                                 12,3                            
// console.log(true + true);   // 2                                                      2                       
// console.log(null + false);  // 0                                                      0                       
// console.log(undefined + 1); // NaN                                                    NaN                         
// console.log({} + {});       // "[object Object][object Object]"                       [object Object][object Object]                                                      
// console.log([] + []);       // ""                                                                             

                                       







// b = [] - []
// console.log(b);          // True                                                                                                                                                                                                                                          
                                                                                                                          
                                                                                                                          
                                                                                                                          
// let secret = Symbol.for('secret');                                                                                                                          
                                                                                                                          
// let user = {                                                                                                                          
//   name: 'Neo',                                                                                                                          
//   secret: 'trinity',                                                                                                                          
//   secret2: 'trinity',                                                                                                                          
//   [1]: 'ty pidor',                                                                                                                          
//   [1, 2]: 'ty pidor',                                                                                                                          
// };                                                                                                                          
                                                                                                                          
// secret = Symbol('secret');                                                                                                                          
// user[secret] = 'trinity_abab';                                                                                                                          
// console.log(user[Symbol.for('secret')]);                                                                                                                          
// console.log();                                                                                                                          
// console.log(user);                                                                                                                          
                                                                                                                          
                                                                                                                          


























// function createUser(name) {                                                                                                                          
//   return {                                                                                                                          
//     sayHi() {                                                                                                                          
//       console.log("Привет, " + name);                                                                                                                          
//     }                                                                                                                          
//   };                                                                                                                          
// }                                                                                                                          
                                                                                                                          
// let us = createUser("Катя");                                                                                                                          
// us.sayHi();                                                                                                                          
// console.log(typeof createUser);                                                                                                                                                                                        
// console.log(typeof createUser());                                                                                                                                                                         
// console.log(typeof createUser().sayHi);                                                                                                                                                                         
// console.log(typeof createUser().sayHi());                                                                                                                                                                         





let obj = {
  a: 12,
  b: 'hui',
  value: function() {
    console.log(this.b, 'длинной', this.a, 'см')
  }
};

Object.defineProperty(obj, 'c2', {
  value: function() {
    console.log(this.b, 'длинной', this.a, 'см')
  } 
});

console.log(obj.c);                                                                                                                                                                         
// console.dir(obj.c);                                                                                                                                                                         
console.log(obj.c2);                                                                                                                                                                         
// console.dir(obj.c2);                                                                                                                                                                         


// const user = Object.create(obj, {
//   name: {
//     value: "Neo",
//     writable: true,  // Может ли значение быть перезаписано?
// 		enumerable: false,  // Будет ли видно в for...in, Object.keys() и т.д.
// 		configurable: true  
// 		// Можно ли: удалить delete obj.key и
// 		// перенастроить свойство через defineProperty ещё раз
// 	},
//   greet: {
//     value: function() {
//       console.log("I'm " + this.name);
//     },
//     writable: true,  
//     enumerable: false,
//     configurable: true  
//   }
// });                                                                                                
                                                                                                                          

// console.log(user.greet())

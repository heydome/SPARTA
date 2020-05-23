class Food{
    constructor(name){
        this.name = name;
        this.list = [];
    }
    addList(name){
        this.list.push(name);
    }
    print(){
        for(let i=0; i<this.list.length;i++){
            console.log(this.list[i]);
        }
    }
}

const fruits = new Food();
fruits.addList('사과');
fruits.addList('딸기');
fruits.addList('바나나');
fruits.print();

// class Fruits{
//     constructor(name, color, price){
//         this.name = name;
//         this.color = color;
//         this.price = price;
//     }

//     view(){
//         console.log(this.color);
//     }
// }

// class Apple extends Fruits{
//     constructor(color,price){
//         super('사과',color,price);
//     }
// }

// const greenApple = new Apple('green', 1000);
// const redApple = new Apple('red', 32000);

// greenApple.view();
// redApple.view();

// class Apple extends Fruits{
//     constructor(color, price){
//         super('사과',color,price)
//     }
// }

// console.log(this.color);

// const apple = new Fruits('사과','Red',2000);
// apple.view();


// var a = new Object();
// console.log(a);

// function A() {};
// var A = new A();
// console.log(A);

// function Number(a, b) {
//     this.a = a;
//     this.b = b;
//   }
  
//   var one = new Number(1, 2);
//   var two = new Number(3, 4);
  
//   console.log(two);
//   console.log(two.a);
//   // 프로토타입에 속성 추가
//   Number.prototype.sum = function() {
//     console.log(this.a + this.b);
//   }
  
//   one.sum(); // 결과: 3
//   two.sum(); // 결과: 7
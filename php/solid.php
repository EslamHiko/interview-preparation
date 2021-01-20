<?php
/*
S: Single-responsibility principle
O: Open-closed principle
L: Liskov substitution principle
I: Interface segregation principle
D: Dependency Inversion Principle
*/

// S: Single-responsibility principle
 class User {

     private $email;

     // Getter and setter...

     public function store() {
         // Store attributes into a database...
     }
 }
// result
 class User {

    private $email;

    // Getter and setter...
}

class UserDB {

    public function store(User $user) {
        // Store the user into a database...
    }
}

// O: Open-closed principle

class Rectangle {

    public $width;
    public $height;

    public function __construct($width, $height) {
        $this->width = $width;
        $this->height = $height;
    }
}

class Square {

    public $length;

    public function __construct($length) {
        $this->length = $length;
    }
}


class AreaCalculator {

    protected $shapes;

    public function __construct($shapes = array()) {
        $this->shapes = $shapes;
    }

    public function sum() {
        $area = [];

        foreach($this->shapes as $shape) {
            if($shape instanceof Square) {
                $area[] = pow($shape->length, 2);
            } else if($shape instanceof Rectangle) {
                $area[] = $shape->width * $shape->height;
            }
        }

        return array_sum($area);
    }
}

 // result

interface Shape {
    public function area();
}

class Rectangle implements Shape {

    private $width;
    private $height;

    public function __construct($width, $height) {
        $this->width = $width;
        $this->height = $height;
    }

    public function area() {
        return $this->width * $this->height;
    }
}

class Square implements Shape {

    private $length;

    public function __construct($length) {
        $this->length = $length;
    }

    public function area() {
        return pow($this->length, 2);
    }
}


class AreaCalculator {

    protected $shapes;

    public function __construct($shapes = array()) {
        $this->shapes = $shapes;
    }

    public function sum() {
        $area = [];

        foreach($this->shapes as $shape) {
            $area[] = $shape->area();
        }

        return array_sum($area);
    }
}

// L: Liskov Substitution Principle
// The principle says that objects must be replaceable by instances of their subtypes without altering the correct functioning of our system.


class BasicCoffeeMachine implements CoffeeMachineInterface {

    public function brewCoffee($selection) {
        switch ($selection) {
            case 'ESPRESSO':
                return $this->brewEspresso();
            default:
                throw new CoffeeException('Selection not supported');
        }
    }

    protected function brewEspresso() {
        // Brew an espresso...
    }
}


class PremiumCoffeeMachine extends BasicCoffeeMachine {

    public function brewCoffee($selection) {
        switch ($selection) {
            case 'ESPRESSO':
                return $this->brewEspresso();
            case 'VANILLA':
                return $this->brewVanillaCoffee();
            default:
                throw new CoffeeException('Selection not supported');
        }
    }

    protected function brewVanillaCoffee() {
        // Brew a vanilla coffee...
    }
}


function getCoffeeMachine(User $user) {
    switch ($user->getPlan()) {
        case 'PREMIUM':
            return new PremiumCoffeeMachine();
        case 'BASIC':
        default:
            return new BasicCoffeeMachine();
    }
}


function prepareCoffee(User $user, $selection) {
    $coffeeMachine = getCoffeeMachine($user);
    return $coffeeMachine->brewCoffee($selection);
}

// Interface Segregation Principle
/*
This principle defines that a class should never implement an interface that does not go to use. In that case, means that in our implementations we will have methods that don’t need.
The solution is to develop specific interfaces instead of general-purpose interfaces.
 */

 interface VehicleInterface {
     public function drive();
     public function fly();
 }

 class FutureCar implements VehicleInterface {

     public function drive() {
         echo 'Driving a future car!';
     }

     public function fly() {
         echo 'Flying a future car!';
     }
 }

 class Car implements VehicleInterface {

     public function drive() {
         echo 'Driving a car!';
     }

     public function fly() {
         throw new Exception('Not implemented method');
     }
 }

 class Airplane implements VehicleInterface {

     public function drive() {
         throw new Exception('Not implemented method');
     }

     public function fly() {
         echo 'Flying an airplane!';
     }
 }

 // result

interface CarInterface {
    public function drive();
}

interface AirplaneInterface {
    public function fly();
}

class FutureCar implements CarInterface, AirplaneInterface {

    public function drive() {
        echo 'Driving a future car!';
    }

    public function fly() {
        echo 'Flying a future car!';
    }
}

class Car implements CarInterface {

    public function drive() {
        echo 'Driving a car!';
    }
}

class Airplane implements AirplaneInterface {

    public function fly() {
        echo 'Flying an airplane!';
    }
}

// D: Dependency Inversion Principle
/*
This principle means that a particular class should not depend directly on another class but on an abstraction of this class.
This principle allows for decoupling and more code reusability.
 */

 class UserDB {

     private $dbConnection;

     public function __construct(MySQLConnection $dbConnection) {
         $this->$dbConnection = $dbConnection;
     }

     public function store(User $user) {
         // Store the user into a database...
     }
 }

 // result

interface DBConnectionInterface {
    public function connect();
}

class MySQLConnection implements DBConnectionInterface {

    public function connect() {
        // Return the MySQL connection...
    }
}

class UserDB {

    private $dbConnection;

    public function __construct(DBConnectionInterface $dbConnection) {
        $this->$dbConnection = $dbConnection;
    }

    public function store(User $user) {
        // Store the user into a database...
    }
}

 ?>

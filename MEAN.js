MEAN stack
- MongoDB
- express.js
- Angular
- Node

SCOPE
// At a base level, JavaScript has function scoping. This means that when we declare variables inside of a function, 
// they are only accessible to that function. Function calls create new scope. 

// ES6 gives us the ability to create variable with const and let in addition to var. While var is function scoped, 
// let and const are also block scoped. For example, if a let or const variable is defined inside an if-block or a loop, 
// then it will not  be defined outside of that block. Referring to that variable outside of the block will produce a 
// ReferenceError since it is not defined.

Variable Hoisting with var
    console.log(magicalUnicorns);
var magicalUnicorns = "awesome";
// In JavaScript, variable declarations are hoisted to the top of their scope. Here's how the interpreter actually 
// reads the previous example:
var magicalUnicorns; // the declaration gets hoisted to the top of the scope by itself
console.log(magicalUnicorns); // we log it as undefined
magicalUnicorns = "awesome"; // the assignment stays exactly where it was

// On the flip side, let and const do not allow us to do this.
console.log(magicalUnicorns);
let magicalUnicorns = "awesome!";
// In the above example, let will produce ReferenceErrors if we try to call the variable this way.

Key Rules of Hoisting
// • Variable declarations (var) rise to the top of their scope like hot air balloons.

// • Functions create their own scope and act like cages, preventing declarations from rising out.

// • Assignments, or = signs, act like anchors. They stay put, no matter how the code is rearranged.

// • let and const do not get hoisted,  and will throw an error if called before they are declared. 
// const will even throw a syntax error if it is called before it is assigned.
var - is used when we want to define the scope, and this will be scoped within functions only.
    let - is used when we want to define the scope, within blocks { }, this includes loops, a variable
declared as a let within an if block, or for loop block, will not be defined outside of the if block, or the for loop block.
    const - is similar to let, in that it's scoped within blocks, but we are unable to change its type, or value once set. 
Note: if an object is const, we can't change the object's structure(such as adding, or replacing keys),
    but we can change the object's values.

Scope and this
'this' is about context
// A strong understanding of the this keyword will help you write bug free code, and detect bugs faster when you create them. 
// Let's look a bit closer. Try running the below code in your browser:


ES6 vs ES5
// ES5 way
function Dot(x, y) {
    this.x = x;
    this.y = y;
}
Dot.prototype.showLocation = function () {
    console.log("This Dot is at x " + this.x + " and y " + this.y);
}
var dot1 = new Dot(55, 20);
dot1.showLocation();
// ES6 way
class Dot {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
    showLocation() {
        // ES6 String Interpolation! Note that the string is enclosed in backticks, not quotes.
        console.log(`This Dot is at x ${this.x} and y ${this.y}`);
    }
}
const dot2 = new Dot(5, 13);
dot2.showLocation();

Class Methods vs Instance Methods
// In ES6, class methods are called 'static methods' while instance methods are called 'prototype methods'. 
// We've already seen prototype methods, now let's look at a static method. Let's say we want to add a new function 
// to the class Dot, not an instance of a Dot:
class Dot {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
    // prototype method
    showLocation() {
        console.log(`This Dot is at x ${this.x} and y ${this.y}`);
    }
    // static method
    static getHelp() {
        console.log("This is a Dot class, for created Dots! A Dot takes x and y coordinates, type 'new Dot' to create one!");
    }
}
const dot3 = new Dot(4, 2);
// we can see showLocation from our instance...
console.log(dot3.showLocation);
// but we can't see getHelp
console.log(dot3.getHelp);
// however we can call getHelp this way:
Dot.getHelp();


Inheritance and Super
// Inheritance is much easier with the ES6 class syntax. Using the extends keyword, we can define new classes that inherit 
// from existing classes. Inheritance is a common aspect of OOP, and it's important to see how JavaScript does it a little 
// differently. Let's see inheritance in action:
// parent Dot class
class Dot {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
    showLocation() {
        console.log(`This Dot is at x ${this.x} and y ${this.y}`);
    }
}
// child Circle class
class Circle extends Dot {
    constructor(x, y, radius) {
        super(x, y);
        this.radius = radius;
    }
}
// we can now create Circles
const circle1 = new Circle(33, 33, 33);
// same attributes as a Dot, plus a radius
console.log(circle1);
// and Circles can access Dot methods
circle1.showLocation();

// If you look closely, you will notice the super() function. Super is a special function that allows us to call the 
// constructor of the parent class. Just like how Dot needs an x and y value, the super() of our Circle class requires 
// that exact same thing.

// Super Continued
// Another important property of super is we can call Parent methods with it. Consider this example:
// parent Dot class
class Dot {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
    showLocation() {
        console.log(`This ${this.constructor.name} is at x ${this.x} and y ${this.y}`);
    }
    // simple method in the parent class
    parentFunction() {
        return "This is coming from the parent!";
    }
}
// child Circle class
class Circle extends Dot {
    constructor(x, y, radius) {
        super(x, y);
        this.radius = radius;
    }
    // simple function in the child class
    childFunction() {
        // by using super, we can call the parent method
        const message = super.parentFunction();
        console.log(message);
    }
}
const circle = new Circle(1, 2, 3);
circle.childFunction();


// If we did not differentiate the attribute name from the getter and setter names, the above code would have put us 
// into an infinite loop, and we would have gotten a RangeError: Maximum call stack size exceeded. It does not matter 
// how you differentiate the names of the attributes from the Getters and Setters, but preceding the attribute with an 
// underscore is convention.


// Any file written in plain text will be served with utf-8 encoding.  Images won't be served with utf-8; 
// omit that argument in the fs.readFile() method when serving images.
// Use the following table to figure out which headers to send with your server's responses:

File type: Headers:
HTML	        { 'Content-Type': 'text/html' }
CSS	            { 'Content-Type': 'text/css' }
Javascript	    { 'Content-Type': 'text/javascript' }
png / jpeg / gif	{ 'Content-Type': 'image/*' } (* is the image format, ie png or jpeg etc)




// Start Node Server
// Full Web Server
const http = require('http');
const fs = require('fs');
const server = http.createServer((request, response) => {
    if (request.url === '/') {
        fs.readFile('./views/index.html', 'utf8', (errors, contents) => {
            response.writeHead(200, { 'Content-Type': 'text/html' });
            response.write(contents);
            response.end();
        });
    }
    // Serving CSS and Images
    else if (request.url === '/stylesheets/style.css') {
        fs.readFile('./stylesheets/style.css', 'utf8', (errors, contents) => {
            response.writeHead(200, { 'Content-type': 'text/css' });
            response.write(contents);
            response.end();
        });
    }
    else if (request.url === '/images/pizza.jpg') {
        // notice we won't include the utf8 encoding
        fs.readFile('./images/pizza.jpg', (errors, contents) => {
            response.writeHead(200, { 'Content-type': 'image/jpg' });
            response.write(contents);
            response.end();
        });
    }
    else if (request.url === "/ninjas") {
        fs.readFile('./views/ninjas.html', 'utf8', (errors, contents) => {
            response.writeHead(200, { 'Content-type': 'text/html' });
            response.write(contents);
            response.end();
        });
    }
    else if (request.url === "/dojos/new") {
        fs.readFile('./views/dojos.html', 'utf8', (errors, contents) => {
            response.writeHead(200, { 'Content-type': 'text/html' });
            response.write(contents);
            response.end();
        });
    }
    else {
        response.end('File not found!!!');
    }
});
server.listen(6789);
console.log("listening on port 6789");



// Link CSS
<link rel="stylesheet" type="text/css" href="/stylesheets/style.css"></link>







// Start Express Server
//  1. Navigate to project folder in terminal
npm init - y
npm install express  or  npm i express
npm install ejs
npm install body - parser
npm install path
npm install mongoose
npm install express - session
npm install express - flash

npm install express ejs body - parser path mongoose express - session express - flash


touch server.js

//  In server.js
const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const path = require('path');

const flash = require('express-flash');
app.use(flash());

const session = require('express-session');
app.use(session({
    secret: 'keyboardkitteh',
    resave: false,
    saveUninitialized: true,
    cookie: { maxAge: 60000 }
}))
// Static and Views
app.use(express.static(path.join(__dirname, '/static')));
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './views'));
// Post Data
app.use(express.urlencoded({ extended: true }));
// Mongoose
const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/name_of_your_DB', { useNewUrlParser: true });
const QuoteSchema = new mongoose.Schema({
    name: { type: String, required: true, minlength: 1 },
    quote: { type: String, required: true, maxlength: 60 },
}, { timestamps: true })
// create an object that contains methods for mongoose to interface with MongoDB
const Quote = mongoose.model('Quote', QuoteSchema);
// Server Port
app.listen(8000, () => console.log("listening on port 8000"));

// Routes
app.get('/', (request, response) => {
    response.send("Hello Express");
});

// 2. Create Static and Views Folder in project folder





// Route and Render EJS
app.get("/users", (req, res) => {
    // hard-coded user data
    var users_array = [
        { name: "Michael", email: "michael@codingdojo.com" },
        { name: "Jay", email: "jay@codingdojo.com" },
        { name: "Brendan", email: "brendan@codingdojo.com" },
        { name: "Andrew", email: "andrew@codingdojo.com" }
    ];
    res.render('users', { users: users_array });
})

    // EJS - embedded JavaScript
    // Notice the <% %> tags allow us to enter JavaScript code, and the <%=  %> tags actually print the JavaScript 
    // code to the document. 
    < html >
    <body>
        <h2>Here are all the users:</h2>
        <% for (var user of users) { %>
            <h3>Name: <%= user.name %></h3>
            <h4>Email: <%= user.email %></h4>
            <hr>
                <% } %>
</body>
</html>

// POST Data - Forms
app.post('/users', (req, res) => {
    console.log(req.body)
    res.redirect('/')
});

// Route Parameters
app.get('/users/:id', (req, res) => {
    console.log(req.params.id);
    // ...
}); //or
app.get("/users/:id", (req, res) => {
    const { id } = req.params;
    console.log("The user id requested is:", id);
    // ...
});

// Ajax
npm install axios

// Sockets.IO
npm install--save express
npm install--save socket.io
nodemon server.js


//  Mongoose (order of below is important!)
const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/name_of_your_DB', { useNewUrlParser: true });
const UserSchema = new mongoose.Schema({
    name: String,
    age: Number
})
// create an object that contains methods for mongoose to interface with MongoDB
const User = mongoose.model('User', UserSchema);

app.post('/users', (req, res) => {
    const user = new User();
    user.name = req.body.name;
    user.age = req.body.age;
    user.save()
        .then(newUserData => console.log('user created: ', newUserData))
        .catch(err => console.log(err));

    res.redirect('/');
})
// The last thing we need is to query our database for our users that we create with our form.  Modify your root route accordingly:
app.get('/', (req, res) => {
    User.find()
        .then(data => res.render("index", { users: data }))
        .catch(err => res.json(err));
});









Starting Angular
// inside directory you want the angular app to start
// Most likely in the express project on server.js level
ng new public
// nagivate into public folder
ng g s http
// in vscode, navigate to app.module.ts and import HttpService in array of providers

// back in app.module.ts
import { HttpClientModule } from '@angular/common/http';
// add HttpClientModule to imports array

// dependecy injection - navigate to http.service.ts
import { HttpClient } from '@angular/common/http';
export class HttpService {
    constructor(private _http: HttpClient) { }
}
// Convention states that this attribute should be preceded by an underscore. (ie _http)
// navigate to app.components.ts
import { HttpService } from './http.service';
import { setFlagsFromString } from 'v8';
export class AppComponent {
    title = 'app';
    constructor(private _httpService: HttpService) { }
}



Angular Forms
// /app/app.module.ts
import { FormsModule } from '@angular/forms'; // <-- import FormsModule.
@NgModule({
    ...
    imports: [
        BrowserModule,
        FormsModule, // <-- register FormsModule with our app.
	],
    ...
})

// .../app/app.component.html
<form (submit) = "onSubmit()" >
    < !--use the json pipe to see how newTask changes in real time-- >
    <p> {{ newTask | json}} </p>
    <input type="text" name="title" [(ngModel)] = "newTask.title" />
        <input type="text" name="description" [(ngModel)] = "newTask.description" />
            <input type="submit" value="Create Task" />
</form >
// .../app/app.component.ts
import { Component, OnInit } from '@angular/core';
@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
    newTask: any;
    constructor() { }

    ngOnInit() {
        this.newTask = { title: "", description: "" }
    }

    onSubmit() {

        // Code to send off the form data (this.newTask) to the Service
        // ...
        // Reset this.newTask to a new, clean object.
        this.newTask = { title: "", description: "" }
    }
}




















Starting FULL MEAN - Boiler Plate
    - npm init - y
        - npm install express body - parser path mongoose
            // Nagivate into project folder. Most likely in the express project on server.js level
            - mkdir server
                - ng new public
                    // Nagivate into server folder
                    - mkdir config
                        - mkdir controllers
                            - mkdir models
                                // Navigate into config folder
                                - touch moongoose.js
                                    - touch routes.js
                                        // Navigate into controllers folder
                                        - touch models.js
                                            // Navigate into models folder
                                            - touch model.js

// In server.js file
const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();

// Angular Source Code
app.use(express.static(path.join(__dirname, '.public/dist/public')));

// Incoming Ajax requests or Post
app.use(bodyParser.json());
app.use(express.urlencoded({ extended: true }));

// Server Port
app.listen(8000, () => {
    console.log("server up on localhost:8000");
})


// In models/models.js file
let mongoose = require('mongoose');

let ModelSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    desc: {
        type: String
    },
    complete: {
        type: Boolean,
        default: false
    }
}, { timestamps: true });

mongoose.model('Model', ModelSchema);
// let Model = mongoose.model('Model')


//  In config/routes.js
let models = require('./../controllers/models');
// Import controller/models.js
module.exports = function (app) {


    app.get('/models', models.index);
    app.get('/models/:_id', models.model);
    app.post('/models', models.create);
    app.delete('/models/:_id', models.delete);
    app.put('/models/:_id', models.update);

}


//  In config/mongoose.js
let mongoose = require('mongoose');

const options = {
    useNewUrlParser: true,
    useUnifiedTopology: true
}

mongoose.connect('mongodb://localhost/PROJECT_NAME', options);
mongoose.Promise = global.Promise;
// Connect to Models files
require('./../models/Model');


//  In server.js file. Import routes/mongoose from config
require('./server/config/mongoose');
require('./server/config/routes')(app);


// In controllers/models.js
let mongoose = require('mongoose');
let Model = mongoose.model('Model');

module.exports = {
    index: function (req, res) {
        Model.find()
            .catch(err => res.json(err))
            .then(models => res.json(models));
    },
    model: function (req, res) {
        Model.findOne({ _id: req.params._id })
            .catch(err => res.json(err))
            .then(model => res.json(model));
    },
    create: function (req, res) {
        Model.create(req.body)
            .catch(err => res.json(err))
            .then(newModel => res.json(newModel));
    },
    delete: function (req, res) {
        Model.delete({ _id: req.params._id }, { returnDeleted: true })
            .catch(err => res.json(err))
            .then(deleted => res.json(deleted));
    },
    update: function (req, res) {
        Model.update({ _id: req.params._id }, req.body, { runValidators: true })
            .catch(err => res.json(err))
            .then(updated => res.json(updated));
    }
}



    // Nagivate into public folder (angular folder)
    - ng g s http
        // in vscode, navigate to app.module.ts and import HttpService in array of providers

        // back in app.module.ts
        - import { HttpClientModule } from '@angular/common/http';
// add HttpClientModule to imports array

// dependecy injection - navigate to http.service.ts
- import { HttpClient } from '@angular/common/http';
- export class HttpService {
    constructor(private _http: HttpClient) { }
}
// Convention states that this attribute should be preceded by an underscore. (ie _http)
// navigate to app.components.ts
import { HttpService } from './http.service';
import { setFlagsFromString } from 'v8';
export class AppComponent {
    title = 'app';
    constructor(private _httpService: HttpService) { }
}

// ADD Angular Forms
// ...src/app/app.module.ts
import { FormsModule } from '@angular/forms'; // <-- import FormsModule.
@NgModule({
    ...
    imports: [
        BrowserModule,
        FormsModule, // <-- register FormsModule with our app.
    ],
    ...
})

// ...src/app/app.component.html
<form (submit) = "onSubmit()" >
    < !--use the json pipe to see how newTask changes in real time-- >
    <p> {{ newTask | json}} </p>
    <input type="text" name="title" [(ngModel)] = "newTask.title" />
        <input type="text" name="description" [(ngModel)] = "newTask.description" />
            <input type="submit" value="Create Task" />
</form >
// ...src/app/app.component.ts
import { Component, OnInit } from '@angular/core';
import { fileLoader } from 'ejs';
@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
    newTask: any;
    constructor() { }

    ngOnInit() {
        this.newTask = { title: "", description: "" }
    }

    onSubmit() {

        // Code to send off the form data (this.newTask) to the Service
        // ...
        // Reset this.newTask to a new, clean object.
        this.newTask = { title: "", description: "" }
    }
}

New Component Generate new component
// in angular project folder
ng g c "component_name"

Nested Component


Angular Routing
//      .../app/app.component.html - Redirecting via links
<button [routerLink]="['/alpha']">Load Alpha</button>
<button [routerLink]="['/beta']">Load Beta</button>
<router-outlet></router-outlet> 

// .../app/app-routing.module.ts
import { AlphaComponent } from './alpha/alpha.component';
import { BetaComponent } from './beta/beta.component';
import { GammaComponent } from './gamma/gamma.component';
import { PageNotFoundComponent } from './pagenotfound/pagenotfound.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
const routes: Routes = [
  { path: 'alpha',component: AlphaComponent },
  { path: 'beta',component: BetaComponent },
  // use a colon and parameter name to include a parameter in the url
  { path: 'gamma/:id', component: GammaComponent },
  // redirect to /alpha if there is nothing in the url
  { path: '', pathMatch: 'full', redirectTo: '/alpha' },
  // the ** will catch anything that did not match any of the above routes
  { path: '**', component: PageNotFoundComponent }
];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

// .../app/app.module.ts
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { AlphaComponent } from './alpha/alpha.component';
import { BetaComponent } from './beta/beta.component';
import { GammaComponent } from './gamma/gamma.component';
@NgModule({
  declarations: [AppComponent, AlphaComponent, BetaComponent, GammaComponent],
  imports: [BrowserModule, AppRoutingModule],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

// .../server.js, this route will be triggered if any of the routes above did not match
app.all("*", (req,res,next) => {
  res.sendFile(path.resolve("./public/dist/public/index.html"))
});


// .../gamma/gamma.component.ts
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';
@Component({
  selector: 'app-gamma',
  templateUrl: './gamma.component.html',
  styleUrls: ['./gamma.component.css']
})
export class GammaComponent implements OnInit {
  constructor(
    private _route: ActivatedRoute,
    private _router: Router
  ) {}
  ngOnInit() {
    this._route.params.subscribe((params: Params) => {
        console.log(params['id'])
    });
  }
  goHome() {
    this._router.navigate(['/home']);
  }
 
}


Nested Routes


















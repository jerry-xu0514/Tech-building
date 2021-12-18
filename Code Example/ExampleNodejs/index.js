const express = require('express');
var session = require('express-session');
const path = require('path');
const settings = require('./Settings');
var bodyParser = require('body-parser');

const app = express();

// Setup form posting
app.use(session({
	secret: 'secret123123235321',
	resave: true,
	saveUninitialized: true
}));
app.use(bodyParser.urlencoded({extended : true}));
app.use(bodyParser.json());
    
// Setup Handlebars
var handlebars = require('express-handlebars').create({ defaultLayout: 'main'});
app.engine('handlebars', handlebars.engine);
app.set('view engine', 'handlebars');

//handlebar homepage
app.get('/', (req, res) => {
    res.render('index', {
        title: 'Main Page'
    });
})


//login mysql - need to install and run mysql server in order to work
const mysql = require('mysql');
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'loginSys'
});
connection.connect((err) => {
  if (err) throw err;
  console.log('Connected!');
});


// all the paths to blogs (http://localhost:5000/blog)
app.use('/blog/', require('./routes/blog.js'));

// all the login logic goes here (http://localhost:5000/auth)
app.use('/auth/', require('./routes/auth.js'));

// set a static folder 
app.use(express.static(path.join(__dirname, 'public')));


const PORT = process.env.PORT || settings.PORT;
app.listen(PORT, () => console.log(`Server started:: port:(${PORT})`));
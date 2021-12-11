const express = require('express');
const path = require('path');
const settings = require('./Settings');

const app = express();

    
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

// all the paths to blogs (http://localhost/blog)
app.use('/blog/', require('./routes/blog.js'));

// set a static folder 
app.use(express.static(path.join(__dirname, 'public')));


const PORT = process.env.PORT || settings.PORT;
app.listen(PORT, () => console.log(`Server started:: port:(${PORT})`));
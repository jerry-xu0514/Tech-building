const express = require('express');
const uuid = require('uuid');

const router = express.Router();


router.get('/', (req, res) => {
    res.redirect('/auth/login');
})
router.get('/login', (req, res) => {
    res.render('login', {});
})

router.post('/loginAction', (request, response) => {
	var username = request.body.username;
	var password = request.body.pwd;
	if (username && password) {
		connection.query('SELECT * FROM users WHERE username = ? AND pwd = ?', [username, password], function(error, results, fields) {
			if (results.length > 0) {
				request.session.loggedin = true;
				request.session.username = username;
				// request.session.id = username;
				response.redirect('/');
			} else {
				response.send('Incorrect Username and/or Password!');
			}			
			response.end();
		});
	} else {
		response.send('Please enter Username and Password!');
		response.end();
	}
});


module.exports = router;
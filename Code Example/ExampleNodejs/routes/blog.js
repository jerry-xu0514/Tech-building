const express = require('express');
const uuid = require('uuid');

const router = express.Router();

router.get('/:paramName', (req, res) => {
    let param = req.params.paramName;
    res.send("success");
    res.status(400).json({ status: 'success' });
})

router.get('/', (req, res) => {
    res.json({asdf: "asdf"});
})

router.post('/create', (req, res) => {
    let newId = uuid.v4();
    let name = req.body.name;
    res.json({status: "success"});
})

module.exports = router;
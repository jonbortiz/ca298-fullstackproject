var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index');
});

router.get('/login', function(req, res, next){
  res.render('login')
});

router.get('/productindividual', function(req, res, next){
  res.render('productindividual')
});

router.get('/basket', function(req, res, next){
  res.render('basket')
});

router.get('/footer', function(req, res, next) {
  res.render('footer')
});

router.get('/header', function(req, res, next) {
  res.render('header')
});

module.exports = router;
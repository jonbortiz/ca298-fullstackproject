var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index');
});

router.get('/login', function(req, res, next){
  res.render('login')
});

router.get('/products', function(req, res, next){
  res.render('products')
});

router.get('/productindividual', function(req, res, next){
  res.render('productindividual')
});

router.get('/register', function(req, res, next){
  res.render('register')
});

router.get('/basket', function(req, res, next){
  res.render('basket')
});

router.get('/orders', function(req, res, next){
  res.render('orders')
});

router.get('/footer', function(req, res, next) {
  res.render('footer')
});

router.get('/header', function(req, res, next) {
  res.render('header')
});

module.exports = router;
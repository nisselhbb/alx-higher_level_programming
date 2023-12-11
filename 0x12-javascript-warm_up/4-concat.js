#!/usr/bin/node
const { argv } = require('process');
const first = argv[2];
const second = argv[3];
const isString = ' is ';
console.log(first + isString + second);

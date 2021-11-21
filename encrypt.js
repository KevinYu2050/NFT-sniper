const QS = require('querystring');

let obj = { 
    email: 'ky97@duke.edu',
    fullName: 'Kai Yang',
    yourEmailVer: '323274',
    password: '12345678',
}

console.log(QS.stringify(obj));

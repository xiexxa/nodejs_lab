const port = 3000;

const mysql = require('mysql');

const con = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'testdb'
});

// 
con.connect(function(err) {
    let sql;
    if (err) throw err;
    console.log('conected')

    // SQL文を発行する
    sql = 'insert into users(name, email) values("kevin", "kevin@test.com")';
    con.query(sql, function(err, result) {
        if (err) throw err;
        console.log(result);
    });

    // SQL文中に変数を代入して発行する
    sql = "insert into users(name, email) values(?, ?)";
    con.query(sql, ['Jack', 'jack@example.co.jp'], function(err, result, fields) {
        if (err) throw err;
        console.log(result);
    })

    // select文
    sql = "select * from users";
    con.query(sql, function (err, result, fields) {
        if (err) throw err;
        console.log(result);
        console.log('特定の値を抽出する');
        console.log('email: '+result[0].email);
    });
});
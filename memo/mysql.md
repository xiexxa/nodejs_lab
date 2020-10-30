## SQLファイルをMySQLに適用する
`$ mysql -u [user_name] -p [db_name] < [sql_file_path]`
- 例  
`$ mysql -u root -p testdb < sql/init.sql`

## ユーザ一覧を確認する
`select User from mysql.user;'`

## ユーザを追加する
`create user user_name identified by 'password';`

## 現在のユーザ名を確認する
`select user(), current_user();`

## ユーザの権限を確認する
`show grants for user_name;`
* USAGE権限の場合、何も権限がない。ユーザ作成時はUSAGE。

## ユーザにすべての権限を付与する
`grant all on *.* to user_name;`
-- Project Name : noname
-- Date/Time    : 2020/07/23 1:09:22
-- Author       : tokazaki13
-- RDBMS Type   : Oracle Database
-- Application  : A5:SQL Mk-2

-- 【一時保存用】ショッピングカートテーブル
drop table if exists 【一時保存用】ショッピングカートテーブル;

create table 【一時保存用】ショッピングカートテーブル (
  itemcode varchar(8) not null
  , name varchar(32) not null
  , author varchar(32) not null
  , price varchar(8) not null
  , discounted varchar(8) not null
  , price_tax varchar(8) not null
  , num int not null
  , total varchar(8) not null
  , total_tax varchar(8) not null
  , item_category varchar(32) not null
  , login_id varchar(8) not null
) ;

-- 受注テーブル
drop table if exists 【編集禁止】受注テーブル（一覧表示用）;

create table 【編集禁止】受注テーブル（一覧表示用） (
  id int auto_increment not null
  , login_id varchar(8) not null
  , name varchar(16) not null
  , order_date datetime default CURRENT_TIMESTAMP not null
  , billing_amount varchar(8) default '0' not null
  , shipping_fee int default 0 not null
  , received int default 0 not null
  , returned int default 0 not null
  , printed int default 0 not null
  , delivered int default 0 not null
  , canceled_id int default 0 not null
  , tel varchar(11) default '0' not null
  , mail_address varchar(128) default '0' not null
  , bikou varchar(255)
  , change_date datetime default CURRENT_TIMESTAMP not null
  , constraint 【編集禁止】受注テーブル（一覧表示用）_PKC primary key (id)
) ;

-- 受注明細テーブル
drop table if exists 【編集禁止】受注明細テーブル（一覧表示用）;

create table 【編集禁止】受注明細テーブル（一覧表示用） (
  id int auto_increment not null
  , order_id int not null
  , itemcode varchar(8) not null
  , name varchar(32) not null
  , ordernum int not null
  , price varchar(8) not null
  , price_with_tax varchar(8) not null
  , total varchar(8) not null
  , total_with_tax varchar(8) not null
  , bikou varchar(255)
  , constraint 【編集禁止】受注明細テーブル（一覧表示用）_PKC primary key (id)
) ;

-- 入出庫履歴テーブル
drop table if exists 入出庫履歴テーブル;

create table 入出庫履歴テーブル (
  id int auto_increment not null
  , itemcode varchar(8) not null
  , stock_date date not null
  , in_num int default 0 not null
  , out_num int default 0 not null
  , bikou varchar(255)
  , change_date datetime default CURRENT_TIMESTAMP not null
  , constraint 入出庫履歴テーブル_PKC primary key (id)
) ;

-- 商品分類テーブル
drop table if exists 商品分類テーブル;

create table 商品分類テーブル (
  id int auto_increment not null
  , name varchar(32) not null
  , discount_rate float default 1 not null
  , flat_price varchar(8) not null
  , sale_flag varchar(8) default '0' not null
  , tax varchar(8) not null
  , delete_flag varchar(4) default '0' not null
  , change_date datetime default CURRENT_TIMESTAMP not null
  , constraint 商品分類テーブル_PKC primary key (id)
) ;

-- 商品履歴テーブル
drop table if exists 商品履歴テーブル;

create table 商品履歴テーブル (
  id int auto_increment not null
  , itemcode varchar(8) not null
  , name varchar(32) not null
  , author varchar(32) not null
  , sale_status varchar(8) not null
  , price varchar(8) not null
  , sale_price varchar(8) not null
  , flat_price varchar(8) not null
  , item_category_id varchar(4) not null
  , 分類名 varchar(32) not null
  , 割引率 float not null
  , 税率 varchar(8) not null
  , sale_flag int default 0 not null
  , delete_flag int default 0 not null
  , bikou varchar(255)
  , change_date datetime default CURRENT_TIMESTAMP not null
  , constraint 商品履歴テーブル_PKC primary key (id)
) ;

-- 配送テーブル
drop table if exists 配送テーブル;

create table 配送テーブル (
  id int auto_increment not null
  , fee int not null
  , areas varchar(8) not null
  , tax float not null
  , delete_flag varchar(4) default '0' not null
  , bikou varchar(255)
  , change_date datetime default CURRENT_TIMESTAMP not null
  , constraint 配送テーブル_PKC primary key (id)
) ;

-- 顧客履歴テーブル
drop table if exists 顧客履歴テーブル;

create table 顧客履歴テーブル (
  id int auto_increment not null
  , login_id varchar(8) not null
  , name varchar(16) not null
  , tel varchar(11) not null
  , mail_address varchar(128) not null
  , zipcode varchar(7) not null
  , address varchar(64) not null
  , deliver_id varchar(2) not null
  , customer_discount varchar(8) default '1' not null
  , bikou varchar(255)
  , registered_date datetime not null
  , change_date datetime default CURRENT_TIMESTAMP not null
  , password varchar(16) not null
  , constraint 顧客履歴テーブル_PKC primary key (id)
) ;

-- 表示用受注テーブル
drop view if exists 表示用受注テーブル;

create view 表示用受注テーブル as 
SELECT
  【編集禁止】受注テーブル（一覧表示用）.id AS 受注ID
  , 【編集禁止】受注テーブル（一覧表示用）.login_id AS ログインID
  , 【編集禁止】受注テーブル（一覧表示用）.name AS 顧客名
  , 【編集禁止】受注テーブル（一覧表示用）.order_date AS 受注日
  , 【編集禁止】受注テーブル（一覧表示用）.billing_amount AS 請求額
  , 【編集禁止】受注テーブル（一覧表示用）.shipping_fee AS 配送料
  , 【編集禁止】受注テーブル（一覧表示用）.received AS 入金状況
  , 【編集禁止】受注テーブル（一覧表示用）.returned AS キャンセル状況
  , 【編集禁止】受注テーブル（一覧表示用）.printed AS 出力状況
  , 【編集禁止】受注テーブル（一覧表示用）.delivered AS 配送状況
  , 【編集禁止】受注テーブル（一覧表示用）.canceled_id AS キャンセル対応受注ID
  , 【編集禁止】受注テーブル（一覧表示用）.tel AS 電話番号
  , 【編集禁止】受注テーブル（一覧表示用）.mail_address AS メールアドレス
  , 【編集禁止】受注テーブル（一覧表示用）.bikou AS 備考
  , 【編集禁止】受注テーブル（一覧表示用）.change_date AS 更新日 
FROM
  【編集禁止】受注テーブル（一覧表示用）

;

-- 表示用受注明細テーブル
drop view if exists 表示用受注明細テーブル;

create view 表示用受注明細テーブル as 
SELECT
  【編集禁止】受注明細テーブル（一覧表示用）.id AS 受注明細ID
  , 【編集禁止】受注明細テーブル（一覧表示用）.order_id AS 受注ID
  , 【編集禁止】受注明細テーブル（一覧表示用）.itemcode AS 商品コード
  , 【編集禁止】受注明細テーブル（一覧表示用）.name AS 商品名
  , 【編集禁止】受注明細テーブル（一覧表示用）.ordernum AS 数量
  , 【編集禁止】受注明細テーブル（一覧表示用）.price AS 税抜価格
  , 【編集禁止】受注明細テーブル（一覧表示用）.price_with_tax AS 税込価格
  , 【編集禁止】受注明細テーブル（一覧表示用）.total AS 税抜小計
  , 【編集禁止】受注明細テーブル（一覧表示用）.total_with_tax AS 税込小計
  , 【編集禁止】受注明細テーブル（一覧表示用）.bikou AS 備考 
FROM
  【編集禁止】受注明細テーブル（一覧表示用）

;

-- 出庫待ちリスト
drop view if exists 出庫待ちリスト;

create view 出庫待ちリスト as 
SELECT
  【編集禁止】受注テーブル（一覧表示用）.id AS 受注ID
  , 【編集禁止】受注テーブル（一覧表示用）.name AS 顧客名
  , 【編集禁止】受注テーブル（一覧表示用）.order_date AS 受注日
  , 【編集禁止】受注テーブル（一覧表示用）.billing_amount AS 請求額
  , 【編集禁止】受注テーブル（一覧表示用）.shipping_fee AS 配送料
  , 【編集禁止】受注明細テーブル（一覧表示用）.itemcode AS 商品コード
  , 【編集禁止】受注明細テーブル（一覧表示用）.name AS 商品名
  , 【編集禁止】受注明細テーブル（一覧表示用）.ordernum AS 数量
  , 【編集禁止】受注明細テーブル（一覧表示用）.price AS 税抜価格
  , 【編集禁止】受注明細テーブル（一覧表示用）.price_with_tax AS 税込価格
  , 【編集禁止】受注明細テーブル（一覧表示用）.total AS 税抜小計
  , 【編集禁止】受注明細テーブル（一覧表示用）.total_with_tax AS 税込小計
  , 【編集禁止】受注テーブル（一覧表示用）.received AS 入金状況
  , 【編集禁止】受注テーブル（一覧表示用）.returned AS キャンセル状況
  , 【編集禁止】受注テーブル（一覧表示用）.delivered AS 配送状況 
FROM
  【編集禁止】受注テーブル（一覧表示用） 
  INNER JOIN 【編集禁止】受注明細テーブル（一覧表示用） 
    ON 【編集禁止】受注テーブル（一覧表示用）.id = 【編集禁止】受注明細テーブル（一覧表示用）.order_id 
WHERE
  【編集禁止】受注テーブル（一覧表示用）.received = 1 
  AND 【編集禁止】受注テーブル（一覧表示用）.returned = 0 
  AND 【編集禁止】受注テーブル（一覧表示用）.delivered = 0

;

-- 受注・受注明細一覧テーブル
drop view if exists 受注・受注明細一覧テーブル;

create view 受注・受注明細一覧テーブル as 
SELECT
  【編集禁止】受注テーブル（一覧表示用）.id AS 受注ID
  , 【編集禁止】受注テーブル（一覧表示用）.name AS 顧客名
  , 【編集禁止】受注テーブル（一覧表示用）.order_date AS 受注日
  , 【編集禁止】受注テーブル（一覧表示用）.billing_amount AS 請求額
  , 【編集禁止】受注テーブル（一覧表示用）.shipping_fee AS 配送料
  , 【編集禁止】受注明細テーブル（一覧表示用）.itemcode AS 商品コード
  , 【編集禁止】受注明細テーブル（一覧表示用）.name AS 商品名
  , 【編集禁止】受注明細テーブル（一覧表示用）.ordernum AS 数量
  , 【編集禁止】受注明細テーブル（一覧表示用）.price AS 税抜価格
  , 【編集禁止】受注明細テーブル（一覧表示用）.price_with_tax AS 税込価格
  , 【編集禁止】受注明細テーブル（一覧表示用）.total AS 税抜小計
  , 【編集禁止】受注明細テーブル（一覧表示用）.total_with_tax AS 税込小計
  , 【編集禁止】受注テーブル（一覧表示用）.received AS 入金状況
  , 【編集禁止】受注テーブル（一覧表示用）.returned AS キャンセル状況
  , 【編集禁止】受注テーブル（一覧表示用）.delivered AS 配送状況
  , 【編集禁止】受注テーブル（一覧表示用）.printed AS 出力状況
  , 【編集禁止】受注テーブル（一覧表示用）.canceled_id AS キャンセル対応受注ID
  , 【編集禁止】受注テーブル（一覧表示用）.tel AS 電話番号
  , 【編集禁止】受注テーブル（一覧表示用）.mail_address AS メールアドレス
  , 【編集禁止】受注テーブル（一覧表示用）.bikou AS 備考
  , 【編集禁止】受注テーブル（一覧表示用）.change_date AS 更新日
FROM
  【編集禁止】受注テーブル（一覧表示用） 
  INNER JOIN 【編集禁止】受注明細テーブル（一覧表示用） 
    ON 【編集禁止】受注テーブル（一覧表示用）.id = 【編集禁止】受注明細テーブル（一覧表示用）.order_id

;

-- 表示用商品履歴テーブル
drop view if exists 表示用商品履歴テーブル;

create view 表示用商品履歴テーブル as 
SELECT
  商品履歴テーブル.id AS 更新履歴ID
  , 商品履歴テーブル.itemcode AS 商品コード
  , 商品履歴テーブル.name AS 商品名
  , 商品履歴テーブル.author AS 商品詳細
  , 商品履歴テーブル.sale_status AS セール状況
  , ( 
    CASE 
      WHEN (商品履歴テーブル.sale_flag = 1) 
        THEN 商品履歴テーブル.sale_price 
      WHEN (商品履歴テーブル.sale_flag = 2) 
        THEN 商品履歴テーブル.flat_price 
      ELSE 商品履歴テーブル.price 
      END
  ) AS 現在価格
  , 商品履歴テーブル.price AS 定価
  , 商品履歴テーブル.sale_price AS セール価格
  , 商品履歴テーブル.flat_price AS 一律価格
  , 商品履歴テーブル.item_category_id AS 商品分類ID
  , 商品履歴テーブル.分類名 AS 分類名
  , 商品履歴テーブル.割引率 AS 割引率
  , 商品履歴テーブル.税率 AS 税率
  , 商品履歴テーブル.sale_flag AS セールフラグ
  , 商品履歴テーブル.delete_flag AS 取扱状況
  , 商品履歴テーブル.bikou AS 備考
FROM
  商品履歴テーブル

;

-- 商品情報一覧テーブル
drop view if exists 商品情報一覧テーブル;

create view 商品情報一覧テーブル as 
SELECT
  i1.更新履歴ID
  , i1.商品コード
  , i1.商品名
  , i1.商品詳細
  , i1.セール状況
  , i1.現在価格
  , i1.定価
  , i1.セール価格
  , i1.一律価格
  , i1.商品分類ID
  , i1.分類名
  , i1.割引率
  , i1.税率
  , i1.セールフラグ
  , i1.取扱状況
  , i1.備考
FROM
  表示用商品履歴テーブル as i1 
  INNER JOIN ( 
    SELECT
      表示用商品履歴テーブル.商品コード AS F1
      , max(表示用商品履歴テーブル.更新履歴ID) AS F2 
    FROM
      表示用商品履歴テーブル 
    GROUP BY
      表示用商品履歴テーブル.商品コード
  ) i2 
    ON i2.F1 = i1.商品コード
    AND i2.F2 = i1.更新履歴ID
;

-- 在庫テーブル
drop view if exists 在庫テーブル;

create view 在庫テーブル as 
SELECT
  商品情報一覧テーブル.商品コード AS 商品コード
  , 商品情報一覧テーブル.商品名
  , (sum(入出庫履歴テーブル.in_num) - sum(入出庫履歴テーブル.out_num)) AS 在庫数 
FROM
  入出庫履歴テーブル 
  RIGHT OUTER JOIN 商品情報一覧テーブル 
    ON 入出庫履歴テーブル.itemcode = 商品情報一覧テーブル.商品コード 
GROUP BY
  商品情報一覧テーブル.商品コード

;

-- 発送チェックシート
drop view if exists 発送チェックシート;

create view 発送チェックシート as 
SELECT
  【編集禁止】受注テーブル（一覧表示用）.id AS 受注ID
  , 【編集禁止】受注テーブル（一覧表示用）.name AS 顧客名
  , 【編集禁止】受注テーブル（一覧表示用）.order_date AS 受注日
  , 【編集禁止】受注テーブル（一覧表示用）.billing_amount AS 請求額
  , 【編集禁止】受注テーブル（一覧表示用）.shipping_fee AS 配送料
  , 【編集禁止】受注明細テーブル（一覧表示用）.itemcode AS 商品コード
  , 【編集禁止】受注明細テーブル（一覧表示用）.name AS 商品名
  , 【編集禁止】受注明細テーブル（一覧表示用）.ordernum AS 数量
  , 【編集禁止】受注明細テーブル（一覧表示用）.price AS 税抜価格
  , 【編集禁止】受注明細テーブル（一覧表示用）.price_with_tax AS 税込価格
  , 【編集禁止】受注明細テーブル（一覧表示用）.total AS 税抜小計
  , 【編集禁止】受注明細テーブル（一覧表示用）.total_with_tax AS 税込小計
  , 【編集禁止】受注テーブル（一覧表示用）.received AS 入金状況
  , 【編集禁止】受注テーブル（一覧表示用）.returned AS キャンセル状況
  , 【編集禁止】受注テーブル（一覧表示用）.delivered AS 配送状況
FROM
  【編集禁止】受注テーブル（一覧表示用） 
  INNER JOIN 【編集禁止】受注明細テーブル（一覧表示用） 
    ON 【編集禁止】受注テーブル（一覧表示用）.id = 【編集禁止】受注明細テーブル（一覧表示用）.order_id 
WHERE
  【編集禁止】受注テーブル（一覧表示用）.received = 1 
  AND 【編集禁止】受注テーブル（一覧表示用）.returned = 0 
  AND 【編集禁止】受注テーブル（一覧表示用）.delivered = 0 
  AND 【編集禁止】受注テーブル（一覧表示用）.printed = 1

;

-- 表示用入出庫履歴テーブル
drop view if exists 表示用入出庫履歴テーブル;

create view 表示用入出庫履歴テーブル as 
SELECT
  入出庫履歴テーブル.id AS 入出庫履歴ID
  , 入出庫履歴テーブル.itemcode AS 商品コード
  , 入出庫履歴テーブル.stock_date AS 入出庫日
  , 入出庫履歴テーブル.in_num AS 入庫数
  , 入出庫履歴テーブル.out_num AS 出庫数
  , 入出庫履歴テーブル.bikou AS 備考
  , 入出庫履歴テーブル.change_date AS 更新日
FROM
  入出庫履歴テーブル

;

-- 表示用商品分類テーブル
drop view if exists 表示用商品分類テーブル;

create view 表示用商品分類テーブル as 
SELECT
  商品分類テーブル.id AS 商品分類ID
  , 商品分類テーブル.name AS 分類名
  , 商品分類テーブル.discount_rate AS 割引率
  , 商品分類テーブル.flat_price AS 一律価格
  , 商品分類テーブル.sale_flag AS セール状況
  , 商品分類テーブル.tax AS 税率
  , 商品分類テーブル.delete_flag AS 削除フラグ
  , 商品分類テーブル.change_date AS 更新日 
FROM
  商品分類テーブル

;



-- 表示用顧客履歴テーブル
drop view if exists 表示用顧客履歴テーブル;

create view 表示用顧客履歴テーブル as 
SELECT
  顧客履歴テーブル.id AS 更新履歴ID
  , 顧客履歴テーブル.login_id AS ログインID
  , 顧客履歴テーブル.name AS 顧客名
  , 顧客履歴テーブル.tel AS 電話番号
  , 顧客履歴テーブル.mail_address AS メールアドレス
  , 顧客履歴テーブル.zipcode AS 郵便番号
  , 顧客履歴テーブル.address AS 住所
  , 顧客履歴テーブル.deliver_id AS 配送ID
  , 配送テーブル.areas AS 配送地域
  , 顧客履歴テーブル.customer_discount AS 顧客分類
  , 顧客履歴テーブル.bikou as 備考
  , 顧客履歴テーブル.registered_date as 登録日
  , 顧客履歴テーブル.change_date as 更新日
FROM
  顧客履歴テーブル 
  INNER JOIN 配送テーブル 
    ON 顧客履歴テーブル.deliver_id = 配送テーブル.id

;

-- 顧客情報一覧テーブル
drop view if exists 顧客情報一覧テーブル;

create view 顧客情報一覧テーブル as 
SELECT
  c1.更新履歴ID
  , c1.ログインID
  , c1.顧客名
  , c1.電話番号
  , c1.メールアドレス
  , c1.郵便番号
  , c1.住所
  , c1.配送ID
  , c1.配送地域
  , c1.顧客分類
  , c1.登録日
  , c1.備考
FROM
  表示用顧客履歴テーブル as c1 
  INNER JOIN ( 
    SELECT
      表示用顧客履歴テーブル.ログインID AS F1
      , max(表示用顧客履歴テーブル.更新履歴ID) AS F2 
    FROM
      表示用顧客履歴テーブル 
    GROUP BY
      表示用顧客履歴テーブル.ログインID
  ) as c2 
    ON c2.F1 = c1.ログインID 
    AND c2.F2 = c1.更新履歴ID

;


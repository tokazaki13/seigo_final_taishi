-- Project Name : noname
-- Date/Time    : 2020/07/23 1:09:22
-- Author       : tokazaki13
-- RDBMS Type   : Oracle Database
-- Application  : A5:SQL Mk-2

-- yêÛ¶pzVbsOJ[ge[u
drop table if exists yêÛ¶pzVbsOJ[ge[u;

create table yêÛ¶pzVbsOJ[ge[u (
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

-- óe[u
drop table if exists yÒWÖ~zóe[uiê\¦pj;

create table yÒWÖ~zóe[uiê\¦pj (
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
  , constraint yÒWÖ~zóe[uiê\¦pj_PKC primary key (id)
) ;

-- ó¾×e[u
drop table if exists yÒWÖ~zó¾×e[uiê\¦pj;

create table yÒWÖ~zó¾×e[uiê\¦pj (
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
  , constraint yÒWÖ~zó¾×e[uiê\¦pj_PKC primary key (id)
) ;

-- üoÉðe[u
drop table if exists üoÉðe[u;

create table üoÉðe[u (
  id int auto_increment not null
  , itemcode varchar(8) not null
  , stock_date date not null
  , in_num int default 0 not null
  , out_num int default 0 not null
  , bikou varchar(255)
  , change_date datetime default CURRENT_TIMESTAMP not null
  , constraint üoÉðe[u_PKC primary key (id)
) ;

-- ¤iªÞe[u
drop table if exists ¤iªÞe[u;

create table ¤iªÞe[u (
  id int auto_increment not null
  , name varchar(32) not null
  , discount_rate float default 1 not null
  , flat_price varchar(8) not null
  , sale_flag varchar(8) default '0' not null
  , tax varchar(8) not null
  , delete_flag varchar(4) default '0' not null
  , change_date datetime default CURRENT_TIMESTAMP not null
  , constraint ¤iªÞe[u_PKC primary key (id)
) ;

-- ¤iðe[u
drop table if exists ¤iðe[u;

create table ¤iðe[u (
  id int auto_increment not null
  , itemcode varchar(8) not null
  , name varchar(32) not null
  , author varchar(32) not null
  , sale_status varchar(8) not null
  , price varchar(8) not null
  , sale_price varchar(8) not null
  , flat_price varchar(8) not null
  , item_category_id varchar(4) not null
  , ªÞ¼ varchar(32) not null
  , ø¦ float not null
  , Å¦ varchar(8) not null
  , sale_flag int default 0 not null
  , delete_flag int default 0 not null
  , bikou varchar(255)
  , change_date datetime default CURRENT_TIMESTAMP not null
  , constraint ¤iðe[u_PKC primary key (id)
) ;

-- ze[u
drop table if exists ze[u;

create table ze[u (
  id int auto_increment not null
  , fee int not null
  , areas varchar(8) not null
  , tax float not null
  , delete_flag varchar(4) default '0' not null
  , bikou varchar(255)
  , change_date datetime default CURRENT_TIMESTAMP not null
  , constraint ze[u_PKC primary key (id)
) ;

-- Úqðe[u
drop table if exists Úqðe[u;

create table Úqðe[u (
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
  , constraint Úqðe[u_PKC primary key (id)
) ;

-- \¦póe[u
drop view if exists \¦póe[u;

create view \¦póe[u as 
SELECT
  yÒWÖ~zóe[uiê\¦pj.id AS óID
  , yÒWÖ~zóe[uiê\¦pj.login_id AS OCID
  , yÒWÖ~zóe[uiê\¦pj.name AS Úq¼
  , yÒWÖ~zóe[uiê\¦pj.order_date AS óú
  , yÒWÖ~zóe[uiê\¦pj.billing_amount AS ¿z
  , yÒWÖ~zóe[uiê\¦pj.shipping_fee AS z¿
  , yÒWÖ~zóe[uiê\¦pj.received AS üàóµ
  , yÒWÖ~zóe[uiê\¦pj.returned AS LZóµ
  , yÒWÖ~zóe[uiê\¦pj.printed AS oÍóµ
  , yÒWÖ~zóe[uiê\¦pj.delivered AS zóµ
  , yÒWÖ~zóe[uiê\¦pj.canceled_id AS LZÎóID
  , yÒWÖ~zóe[uiê\¦pj.tel AS dbÔ
  , yÒWÖ~zóe[uiê\¦pj.mail_address AS [AhX
  , yÒWÖ~zóe[uiê\¦pj.bikou AS õl
  , yÒWÖ~zóe[uiê\¦pj.change_date AS XVú 
FROM
  yÒWÖ~zóe[uiê\¦pj

;

-- \¦pó¾×e[u
drop view if exists \¦pó¾×e[u;

create view \¦pó¾×e[u as 
SELECT
  yÒWÖ~zó¾×e[uiê\¦pj.id AS ó¾×ID
  , yÒWÖ~zó¾×e[uiê\¦pj.order_id AS óID
  , yÒWÖ~zó¾×e[uiê\¦pj.itemcode AS ¤iR[h
  , yÒWÖ~zó¾×e[uiê\¦pj.name AS ¤i¼
  , yÒWÖ~zó¾×e[uiê\¦pj.ordernum AS Ê
  , yÒWÖ~zó¾×e[uiê\¦pj.price AS Å²¿i
  , yÒWÖ~zó¾×e[uiê\¦pj.price_with_tax AS Å¿i
  , yÒWÖ~zó¾×e[uiê\¦pj.total AS Å²¬v
  , yÒWÖ~zó¾×e[uiê\¦pj.total_with_tax AS Å¬v
  , yÒWÖ~zó¾×e[uiê\¦pj.bikou AS õl 
FROM
  yÒWÖ~zó¾×e[uiê\¦pj

;

-- oÉÒ¿Xg
drop view if exists oÉÒ¿Xg;

create view oÉÒ¿Xg as 
SELECT
  yÒWÖ~zóe[uiê\¦pj.id AS óID
  , yÒWÖ~zóe[uiê\¦pj.name AS Úq¼
  , yÒWÖ~zóe[uiê\¦pj.order_date AS óú
  , yÒWÖ~zóe[uiê\¦pj.billing_amount AS ¿z
  , yÒWÖ~zóe[uiê\¦pj.shipping_fee AS z¿
  , yÒWÖ~zó¾×e[uiê\¦pj.itemcode AS ¤iR[h
  , yÒWÖ~zó¾×e[uiê\¦pj.name AS ¤i¼
  , yÒWÖ~zó¾×e[uiê\¦pj.ordernum AS Ê
  , yÒWÖ~zó¾×e[uiê\¦pj.price AS Å²¿i
  , yÒWÖ~zó¾×e[uiê\¦pj.price_with_tax AS Å¿i
  , yÒWÖ~zó¾×e[uiê\¦pj.total AS Å²¬v
  , yÒWÖ~zó¾×e[uiê\¦pj.total_with_tax AS Å¬v
  , yÒWÖ~zóe[uiê\¦pj.received AS üàóµ
  , yÒWÖ~zóe[uiê\¦pj.returned AS LZóµ
  , yÒWÖ~zóe[uiê\¦pj.delivered AS zóµ 
FROM
  yÒWÖ~zóe[uiê\¦pj 
  INNER JOIN yÒWÖ~zó¾×e[uiê\¦pj 
    ON yÒWÖ~zóe[uiê\¦pj.id = yÒWÖ~zó¾×e[uiê\¦pj.order_id 
WHERE
  yÒWÖ~zóe[uiê\¦pj.received = 1 
  AND yÒWÖ~zóe[uiê\¦pj.returned = 0 
  AND yÒWÖ~zóe[uiê\¦pj.delivered = 0

;

-- óEó¾×êe[u
drop view if exists óEó¾×êe[u;

create view óEó¾×êe[u as 
SELECT
  yÒWÖ~zóe[uiê\¦pj.id AS óID
  , yÒWÖ~zóe[uiê\¦pj.name AS Úq¼
  , yÒWÖ~zóe[uiê\¦pj.order_date AS óú
  , yÒWÖ~zóe[uiê\¦pj.billing_amount AS ¿z
  , yÒWÖ~zóe[uiê\¦pj.shipping_fee AS z¿
  , yÒWÖ~zó¾×e[uiê\¦pj.itemcode AS ¤iR[h
  , yÒWÖ~zó¾×e[uiê\¦pj.name AS ¤i¼
  , yÒWÖ~zó¾×e[uiê\¦pj.ordernum AS Ê
  , yÒWÖ~zó¾×e[uiê\¦pj.price AS Å²¿i
  , yÒWÖ~zó¾×e[uiê\¦pj.price_with_tax AS Å¿i
  , yÒWÖ~zó¾×e[uiê\¦pj.total AS Å²¬v
  , yÒWÖ~zó¾×e[uiê\¦pj.total_with_tax AS Å¬v
  , yÒWÖ~zóe[uiê\¦pj.received AS üàóµ
  , yÒWÖ~zóe[uiê\¦pj.returned AS LZóµ
  , yÒWÖ~zóe[uiê\¦pj.delivered AS zóµ
  , yÒWÖ~zóe[uiê\¦pj.printed AS oÍóµ
  , yÒWÖ~zóe[uiê\¦pj.canceled_id AS LZÎóID
  , yÒWÖ~zóe[uiê\¦pj.tel AS dbÔ
  , yÒWÖ~zóe[uiê\¦pj.mail_address AS [AhX
  , yÒWÖ~zóe[uiê\¦pj.bikou AS õl
  , yÒWÖ~zóe[uiê\¦pj.change_date AS XVú
FROM
  yÒWÖ~zóe[uiê\¦pj 
  INNER JOIN yÒWÖ~zó¾×e[uiê\¦pj 
    ON yÒWÖ~zóe[uiê\¦pj.id = yÒWÖ~zó¾×e[uiê\¦pj.order_id

;

-- \¦p¤iðe[u
drop view if exists \¦p¤iðe[u;

create view \¦p¤iðe[u as 
SELECT
  ¤iðe[u.id AS XVðID
  , ¤iðe[u.itemcode AS ¤iR[h
  , ¤iðe[u.name AS ¤i¼
  , ¤iðe[u.author AS ¤iÚ×
  , ¤iðe[u.sale_status AS Z[óµ
  , ( 
    CASE 
      WHEN (¤iðe[u.sale_flag = 1) 
        THEN ¤iðe[u.sale_price 
      WHEN (¤iðe[u.sale_flag = 2) 
        THEN ¤iðe[u.flat_price 
      ELSE ¤iðe[u.price 
      END
  ) AS »Ý¿i
  , ¤iðe[u.price AS è¿
  , ¤iðe[u.sale_price AS Z[¿i
  , ¤iðe[u.flat_price AS ê¥¿i
  , ¤iðe[u.item_category_id AS ¤iªÞID
  , ¤iðe[u.ªÞ¼ AS ªÞ¼
  , ¤iðe[u.ø¦ AS ø¦
  , ¤iðe[u.Å¦ AS Å¦
  , ¤iðe[u.sale_flag AS Z[tO
  , ¤iðe[u.delete_flag AS æµóµ
  , ¤iðe[u.bikou AS õl
FROM
  ¤iðe[u

;

-- ¤iîñêe[u
drop view if exists ¤iîñêe[u;

create view ¤iîñêe[u as 
SELECT
  i1.XVðID
  , i1.¤iR[h
  , i1.¤i¼
  , i1.¤iÚ×
  , i1.Z[óµ
  , i1.»Ý¿i
  , i1.è¿
  , i1.Z[¿i
  , i1.ê¥¿i
  , i1.¤iªÞID
  , i1.ªÞ¼
  , i1.ø¦
  , i1.Å¦
  , i1.Z[tO
  , i1.æµóµ
  , i1.õl
FROM
  \¦p¤iðe[u as i1 
  INNER JOIN ( 
    SELECT
      \¦p¤iðe[u.¤iR[h AS F1
      , max(\¦p¤iðe[u.XVðID) AS F2 
    FROM
      \¦p¤iðe[u 
    GROUP BY
      \¦p¤iðe[u.¤iR[h
  ) i2 
    ON i2.F1 = i1.¤iR[h
    AND i2.F2 = i1.XVðID
;

-- ÝÉe[u
drop view if exists ÝÉe[u;

create view ÝÉe[u as 
SELECT
  ¤iîñêe[u.¤iR[h AS ¤iR[h
  , ¤iîñêe[u.¤i¼
  , (sum(üoÉðe[u.in_num) - sum(üoÉðe[u.out_num)) AS ÝÉ 
FROM
  üoÉðe[u 
  RIGHT OUTER JOIN ¤iîñêe[u 
    ON üoÉðe[u.itemcode = ¤iîñêe[u.¤iR[h 
GROUP BY
  ¤iîñêe[u.¤iR[h

;

-- ­`FbNV[g
drop view if exists ­`FbNV[g;

create view ­`FbNV[g as 
SELECT
  yÒWÖ~zóe[uiê\¦pj.id AS óID
  , yÒWÖ~zóe[uiê\¦pj.name AS Úq¼
  , yÒWÖ~zóe[uiê\¦pj.order_date AS óú
  , yÒWÖ~zóe[uiê\¦pj.billing_amount AS ¿z
  , yÒWÖ~zóe[uiê\¦pj.shipping_fee AS z¿
  , yÒWÖ~zó¾×e[uiê\¦pj.itemcode AS ¤iR[h
  , yÒWÖ~zó¾×e[uiê\¦pj.name AS ¤i¼
  , yÒWÖ~zó¾×e[uiê\¦pj.ordernum AS Ê
  , yÒWÖ~zó¾×e[uiê\¦pj.price AS Å²¿i
  , yÒWÖ~zó¾×e[uiê\¦pj.price_with_tax AS Å¿i
  , yÒWÖ~zó¾×e[uiê\¦pj.total AS Å²¬v
  , yÒWÖ~zó¾×e[uiê\¦pj.total_with_tax AS Å¬v
  , yÒWÖ~zóe[uiê\¦pj.received AS üàóµ
  , yÒWÖ~zóe[uiê\¦pj.returned AS LZóµ
  , yÒWÖ~zóe[uiê\¦pj.delivered AS zóµ
FROM
  yÒWÖ~zóe[uiê\¦pj 
  INNER JOIN yÒWÖ~zó¾×e[uiê\¦pj 
    ON yÒWÖ~zóe[uiê\¦pj.id = yÒWÖ~zó¾×e[uiê\¦pj.order_id 
WHERE
  yÒWÖ~zóe[uiê\¦pj.received = 1 
  AND yÒWÖ~zóe[uiê\¦pj.returned = 0 
  AND yÒWÖ~zóe[uiê\¦pj.delivered = 0 
  AND yÒWÖ~zóe[uiê\¦pj.printed = 1

;

-- \¦püoÉðe[u
drop view if exists \¦püoÉðe[u;

create view \¦püoÉðe[u as 
SELECT
  üoÉðe[u.id AS üoÉðID
  , üoÉðe[u.itemcode AS ¤iR[h
  , üoÉðe[u.stock_date AS üoÉú
  , üoÉðe[u.in_num AS üÉ
  , üoÉðe[u.out_num AS oÉ
  , üoÉðe[u.bikou AS õl
  , üoÉðe[u.change_date AS XVú
FROM
  üoÉðe[u

;

-- \¦p¤iªÞe[u
drop view if exists \¦p¤iªÞe[u;

create view \¦p¤iªÞe[u as 
SELECT
  ¤iªÞe[u.id AS ¤iªÞID
  , ¤iªÞe[u.name AS ªÞ¼
  , ¤iªÞe[u.discount_rate AS ø¦
  , ¤iªÞe[u.flat_price AS ê¥¿i
  , ¤iªÞe[u.sale_flag AS Z[óµ
  , ¤iªÞe[u.tax AS Å¦
  , ¤iªÞe[u.delete_flag AS ítO
  , ¤iªÞe[u.change_date AS XVú 
FROM
  ¤iªÞe[u

;



-- \¦pÚqðe[u
drop view if exists \¦pÚqðe[u;

create view \¦pÚqðe[u as 
SELECT
  Úqðe[u.id AS XVðID
  , Úqðe[u.login_id AS OCID
  , Úqðe[u.name AS Úq¼
  , Úqðe[u.tel AS dbÔ
  , Úqðe[u.mail_address AS [AhX
  , Úqðe[u.zipcode AS XÖÔ
  , Úqðe[u.address AS Z
  , Úqðe[u.deliver_id AS zID
  , ze[u.areas AS znæ
  , Úqðe[u.customer_discount AS ÚqªÞ
  , Úqðe[u.bikou as õl
  , Úqðe[u.registered_date as o^ú
  , Úqðe[u.change_date as XVú
FROM
  Úqðe[u 
  INNER JOIN ze[u 
    ON Úqðe[u.deliver_id = ze[u.id

;

-- Úqîñêe[u
drop view if exists Úqîñêe[u;

create view Úqîñêe[u as 
SELECT
  c1.XVðID
  , c1.OCID
  , c1.Úq¼
  , c1.dbÔ
  , c1.[AhX
  , c1.XÖÔ
  , c1.Z
  , c1.zID
  , c1.znæ
  , c1.ÚqªÞ
  , c1.o^ú
  , c1.õl
FROM
  \¦pÚqðe[u as c1 
  INNER JOIN ( 
    SELECT
      \¦pÚqðe[u.OCID AS F1
      , max(\¦pÚqðe[u.XVðID) AS F2 
    FROM
      \¦pÚqðe[u 
    GROUP BY
      \¦pÚqðe[u.OCID
  ) as c2 
    ON c2.F1 = c1.OCID 
    AND c2.F2 = c1.XVðID

;


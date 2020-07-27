-- Project Name : noname
-- Date/Time    : 2020/07/23 1:09:22
-- Author       : tokazaki13
-- RDBMS Type   : Oracle Database
-- Application  : A5:SQL Mk-2

-- �y�ꎞ�ۑ��p�z�V���b�s���O�J�[�g�e�[�u��
drop table if exists �y�ꎞ�ۑ��p�z�V���b�s���O�J�[�g�e�[�u��;

create table �y�ꎞ�ۑ��p�z�V���b�s���O�J�[�g�e�[�u�� (
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

-- �󒍃e�[�u��
drop table if exists �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j;

create table �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j (
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
  , constraint �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j_PKC primary key (id)
) ;

-- �󒍖��׃e�[�u��
drop table if exists �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j;

create table �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j (
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
  , constraint �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j_PKC primary key (id)
) ;

-- ���o�ɗ����e�[�u��
drop table if exists ���o�ɗ����e�[�u��;

create table ���o�ɗ����e�[�u�� (
  id int auto_increment not null
  , itemcode varchar(8) not null
  , stock_date date not null
  , in_num int default 0 not null
  , out_num int default 0 not null
  , bikou varchar(255)
  , change_date datetime default CURRENT_TIMESTAMP not null
  , constraint ���o�ɗ����e�[�u��_PKC primary key (id)
) ;

-- ���i���ރe�[�u��
drop table if exists ���i���ރe�[�u��;

create table ���i���ރe�[�u�� (
  id int auto_increment not null
  , name varchar(32) not null
  , discount_rate float default 1 not null
  , flat_price varchar(8) not null
  , sale_flag varchar(8) default '0' not null
  , tax varchar(8) not null
  , delete_flag varchar(4) default '0' not null
  , change_date datetime default CURRENT_TIMESTAMP not null
  , constraint ���i���ރe�[�u��_PKC primary key (id)
) ;

-- ���i�����e�[�u��
drop table if exists ���i�����e�[�u��;

create table ���i�����e�[�u�� (
  id int auto_increment not null
  , itemcode varchar(8) not null
  , name varchar(32) not null
  , author varchar(32) not null
  , sale_status varchar(8) not null
  , price varchar(8) not null
  , sale_price varchar(8) not null
  , flat_price varchar(8) not null
  , item_category_id varchar(4) not null
  , ���ޖ� varchar(32) not null
  , ������ float not null
  , �ŗ� varchar(8) not null
  , sale_flag int default 0 not null
  , delete_flag int default 0 not null
  , bikou varchar(255)
  , change_date datetime default CURRENT_TIMESTAMP not null
  , constraint ���i�����e�[�u��_PKC primary key (id)
) ;

-- �z���e�[�u��
drop table if exists �z���e�[�u��;

create table �z���e�[�u�� (
  id int auto_increment not null
  , fee int not null
  , areas varchar(8) not null
  , tax float not null
  , delete_flag varchar(4) default '0' not null
  , bikou varchar(255)
  , change_date datetime default CURRENT_TIMESTAMP not null
  , constraint �z���e�[�u��_PKC primary key (id)
) ;

-- �ڋq�����e�[�u��
drop table if exists �ڋq�����e�[�u��;

create table �ڋq�����e�[�u�� (
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
  , constraint �ڋq�����e�[�u��_PKC primary key (id)
) ;

-- �\���p�󒍃e�[�u��
drop view if exists �\���p�󒍃e�[�u��;

create view �\���p�󒍃e�[�u�� as 
SELECT
  �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.id AS ��ID
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.login_id AS ���O�C��ID
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.name AS �ڋq��
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.order_date AS �󒍓�
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.billing_amount AS �����z
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.shipping_fee AS �z����
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.received AS ������
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.returned AS �L�����Z����
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.printed AS �o�͏�
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.delivered AS �z����
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.canceled_id AS �L�����Z���Ή���ID
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.tel AS �d�b�ԍ�
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.mail_address AS ���[���A�h���X
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.bikou AS ���l
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.change_date AS �X�V�� 
FROM
  �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j

;

-- �\���p�󒍖��׃e�[�u��
drop view if exists �\���p�󒍖��׃e�[�u��;

create view �\���p�󒍖��׃e�[�u�� as 
SELECT
  �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.id AS �󒍖���ID
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.order_id AS ��ID
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.itemcode AS ���i�R�[�h
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.name AS ���i��
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.ordernum AS ����
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.price AS �Ŕ����i
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.price_with_tax AS �ō����i
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.total AS �Ŕ����v
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.total_with_tax AS �ō����v
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.bikou AS ���l 
FROM
  �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j

;

-- �o�ɑ҂����X�g
drop view if exists �o�ɑ҂����X�g;

create view �o�ɑ҂����X�g as 
SELECT
  �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.id AS ��ID
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.name AS �ڋq��
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.order_date AS �󒍓�
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.billing_amount AS �����z
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.shipping_fee AS �z����
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.itemcode AS ���i�R�[�h
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.name AS ���i��
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.ordernum AS ����
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.price AS �Ŕ����i
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.price_with_tax AS �ō����i
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.total AS �Ŕ����v
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.total_with_tax AS �ō����v
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.received AS ������
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.returned AS �L�����Z����
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.delivered AS �z���� 
FROM
  �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j 
  INNER JOIN �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j 
    ON �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.id = �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.order_id 
WHERE
  �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.received = 1 
  AND �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.returned = 0 
  AND �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.delivered = 0

;

-- �󒍁E�󒍖��׈ꗗ�e�[�u��
drop view if exists �󒍁E�󒍖��׈ꗗ�e�[�u��;

create view �󒍁E�󒍖��׈ꗗ�e�[�u�� as 
SELECT
  �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.id AS ��ID
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.name AS �ڋq��
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.order_date AS �󒍓�
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.billing_amount AS �����z
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.shipping_fee AS �z����
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.itemcode AS ���i�R�[�h
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.name AS ���i��
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.ordernum AS ����
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.price AS �Ŕ����i
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.price_with_tax AS �ō����i
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.total AS �Ŕ����v
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.total_with_tax AS �ō����v
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.received AS ������
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.returned AS �L�����Z����
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.delivered AS �z����
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.printed AS �o�͏�
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.canceled_id AS �L�����Z���Ή���ID
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.tel AS �d�b�ԍ�
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.mail_address AS ���[���A�h���X
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.bikou AS ���l
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.change_date AS �X�V��
FROM
  �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j 
  INNER JOIN �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j 
    ON �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.id = �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.order_id

;

-- �\���p���i�����e�[�u��
drop view if exists �\���p���i�����e�[�u��;

create view �\���p���i�����e�[�u�� as 
SELECT
  ���i�����e�[�u��.id AS �X�V����ID
  , ���i�����e�[�u��.itemcode AS ���i�R�[�h
  , ���i�����e�[�u��.name AS ���i��
  , ���i�����e�[�u��.author AS ���i�ڍ�
  , ���i�����e�[�u��.sale_status AS �Z�[����
  , ( 
    CASE 
      WHEN (���i�����e�[�u��.sale_flag = 1) 
        THEN ���i�����e�[�u��.sale_price 
      WHEN (���i�����e�[�u��.sale_flag = 2) 
        THEN ���i�����e�[�u��.flat_price 
      ELSE ���i�����e�[�u��.price 
      END
  ) AS ���݉��i
  , ���i�����e�[�u��.price AS �艿
  , ���i�����e�[�u��.sale_price AS �Z�[�����i
  , ���i�����e�[�u��.flat_price AS �ꗥ���i
  , ���i�����e�[�u��.item_category_id AS ���i����ID
  , ���i�����e�[�u��.���ޖ� AS ���ޖ�
  , ���i�����e�[�u��.������ AS ������
  , ���i�����e�[�u��.�ŗ� AS �ŗ�
  , ���i�����e�[�u��.sale_flag AS �Z�[���t���O
  , ���i�����e�[�u��.delete_flag AS �戵��
  , ���i�����e�[�u��.bikou AS ���l
FROM
  ���i�����e�[�u��

;

-- ���i���ꗗ�e�[�u��
drop view if exists ���i���ꗗ�e�[�u��;

create view ���i���ꗗ�e�[�u�� as 
SELECT
  i1.�X�V����ID
  , i1.���i�R�[�h
  , i1.���i��
  , i1.���i�ڍ�
  , i1.�Z�[����
  , i1.���݉��i
  , i1.�艿
  , i1.�Z�[�����i
  , i1.�ꗥ���i
  , i1.���i����ID
  , i1.���ޖ�
  , i1.������
  , i1.�ŗ�
  , i1.�Z�[���t���O
  , i1.�戵��
  , i1.���l
FROM
  �\���p���i�����e�[�u�� as i1 
  INNER JOIN ( 
    SELECT
      �\���p���i�����e�[�u��.���i�R�[�h AS F1
      , max(�\���p���i�����e�[�u��.�X�V����ID) AS F2 
    FROM
      �\���p���i�����e�[�u�� 
    GROUP BY
      �\���p���i�����e�[�u��.���i�R�[�h
  ) i2 
    ON i2.F1 = i1.���i�R�[�h
    AND i2.F2 = i1.�X�V����ID
;

-- �݌Ƀe�[�u��
drop view if exists �݌Ƀe�[�u��;

create view �݌Ƀe�[�u�� as 
SELECT
  ���i���ꗗ�e�[�u��.���i�R�[�h AS ���i�R�[�h
  , ���i���ꗗ�e�[�u��.���i��
  , (sum(���o�ɗ����e�[�u��.in_num) - sum(���o�ɗ����e�[�u��.out_num)) AS �݌ɐ� 
FROM
  ���o�ɗ����e�[�u�� 
  RIGHT OUTER JOIN ���i���ꗗ�e�[�u�� 
    ON ���o�ɗ����e�[�u��.itemcode = ���i���ꗗ�e�[�u��.���i�R�[�h 
GROUP BY
  ���i���ꗗ�e�[�u��.���i�R�[�h

;

-- �����`�F�b�N�V�[�g
drop view if exists �����`�F�b�N�V�[�g;

create view �����`�F�b�N�V�[�g as 
SELECT
  �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.id AS ��ID
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.name AS �ڋq��
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.order_date AS �󒍓�
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.billing_amount AS �����z
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.shipping_fee AS �z����
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.itemcode AS ���i�R�[�h
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.name AS ���i��
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.ordernum AS ����
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.price AS �Ŕ����i
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.price_with_tax AS �ō����i
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.total AS �Ŕ����v
  , �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.total_with_tax AS �ō����v
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.received AS ������
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.returned AS �L�����Z����
  , �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.delivered AS �z����
FROM
  �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j 
  INNER JOIN �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j 
    ON �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.id = �y�ҏW�֎~�z�󒍖��׃e�[�u���i�ꗗ�\���p�j.order_id 
WHERE
  �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.received = 1 
  AND �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.returned = 0 
  AND �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.delivered = 0 
  AND �y�ҏW�֎~�z�󒍃e�[�u���i�ꗗ�\���p�j.printed = 1

;

-- �\���p���o�ɗ����e�[�u��
drop view if exists �\���p���o�ɗ����e�[�u��;

create view �\���p���o�ɗ����e�[�u�� as 
SELECT
  ���o�ɗ����e�[�u��.id AS ���o�ɗ���ID
  , ���o�ɗ����e�[�u��.itemcode AS ���i�R�[�h
  , ���o�ɗ����e�[�u��.stock_date AS ���o�ɓ�
  , ���o�ɗ����e�[�u��.in_num AS ���ɐ�
  , ���o�ɗ����e�[�u��.out_num AS �o�ɐ�
  , ���o�ɗ����e�[�u��.bikou AS ���l
  , ���o�ɗ����e�[�u��.change_date AS �X�V��
FROM
  ���o�ɗ����e�[�u��

;

-- �\���p���i���ރe�[�u��
drop view if exists �\���p���i���ރe�[�u��;

create view �\���p���i���ރe�[�u�� as 
SELECT
  ���i���ރe�[�u��.id AS ���i����ID
  , ���i���ރe�[�u��.name AS ���ޖ�
  , ���i���ރe�[�u��.discount_rate AS ������
  , ���i���ރe�[�u��.flat_price AS �ꗥ���i
  , ���i���ރe�[�u��.sale_flag AS �Z�[����
  , ���i���ރe�[�u��.tax AS �ŗ�
  , ���i���ރe�[�u��.delete_flag AS �폜�t���O
  , ���i���ރe�[�u��.change_date AS �X�V�� 
FROM
  ���i���ރe�[�u��

;



-- �\���p�ڋq�����e�[�u��
drop view if exists �\���p�ڋq�����e�[�u��;

create view �\���p�ڋq�����e�[�u�� as 
SELECT
  �ڋq�����e�[�u��.id AS �X�V����ID
  , �ڋq�����e�[�u��.login_id AS ���O�C��ID
  , �ڋq�����e�[�u��.name AS �ڋq��
  , �ڋq�����e�[�u��.tel AS �d�b�ԍ�
  , �ڋq�����e�[�u��.mail_address AS ���[���A�h���X
  , �ڋq�����e�[�u��.zipcode AS �X�֔ԍ�
  , �ڋq�����e�[�u��.address AS �Z��
  , �ڋq�����e�[�u��.deliver_id AS �z��ID
  , �z���e�[�u��.areas AS �z���n��
  , �ڋq�����e�[�u��.customer_discount AS �ڋq����
  , �ڋq�����e�[�u��.bikou as ���l
  , �ڋq�����e�[�u��.registered_date as �o�^��
  , �ڋq�����e�[�u��.change_date as �X�V��
FROM
  �ڋq�����e�[�u�� 
  INNER JOIN �z���e�[�u�� 
    ON �ڋq�����e�[�u��.deliver_id = �z���e�[�u��.id

;

-- �ڋq���ꗗ�e�[�u��
drop view if exists �ڋq���ꗗ�e�[�u��;

create view �ڋq���ꗗ�e�[�u�� as 
SELECT
  c1.�X�V����ID
  , c1.���O�C��ID
  , c1.�ڋq��
  , c1.�d�b�ԍ�
  , c1.���[���A�h���X
  , c1.�X�֔ԍ�
  , c1.�Z��
  , c1.�z��ID
  , c1.�z���n��
  , c1.�ڋq����
  , c1.�o�^��
  , c1.���l
FROM
  �\���p�ڋq�����e�[�u�� as c1 
  INNER JOIN ( 
    SELECT
      �\���p�ڋq�����e�[�u��.���O�C��ID AS F1
      , max(�\���p�ڋq�����e�[�u��.�X�V����ID) AS F2 
    FROM
      �\���p�ڋq�����e�[�u�� 
    GROUP BY
      �\���p�ڋq�����e�[�u��.���O�C��ID
  ) as c2 
    ON c2.F1 = c1.���O�C��ID 
    AND c2.F2 = c1.�X�V����ID

;


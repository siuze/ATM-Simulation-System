-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        8.0.26 - MySQL Community Server - GPL
-- 服务器操作系统:                      Win64
-- HeidiSQL 版本:                  11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- 导出 atm 的数据库结构
CREATE DATABASE IF NOT EXISTS `atm` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `atm`;

-- 导出  表 atm.临时会话 结构
CREATE TABLE IF NOT EXISTS `临时会话` (
  `会话号` bigint NOT NULL,
  `卡号` bigint NOT NULL,
  `会话过期时间` timestamp NOT NULL,
  `会话建立时间` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`会话号`) USING BTREE,
  KEY `FK_session_users` (`卡号`) USING BTREE,
  CONSTRAINT `FK_临时会话_银行卡密` FOREIGN KEY (`卡号`) REFERENCES `银行卡密` (`卡号`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='会话记录表';

-- 正在导出表  atm.临时会话 的数据：~0 rows (大约)
DELETE FROM `临时会话`;
/*!40000 ALTER TABLE `临时会话` DISABLE KEYS */;
INSERT INTO `临时会话` (`会话号`, `卡号`, `会话过期时间`, `会话建立时间`) VALUES
	(648914137858, 1043, '2022-06-22 16:14:06', '2022-06-22 16:12:06');
/*!40000 ALTER TABLE `临时会话` ENABLE KEYS */;

-- 导出  表 atm.卡内账户 结构
CREATE TABLE IF NOT EXISTS `卡内账户` (
  `账户号` varchar(50) NOT NULL DEFAULT '',
  `卡号` bigint NOT NULL DEFAULT '0',
  `账户类型` varchar(2) NOT NULL,
  PRIMARY KEY (`账户号`),
  KEY `卡号` (`卡号`),
  CONSTRAINT `FK_卡内账户_银行卡密` FOREIGN KEY (`卡号`) REFERENCES `银行卡密` (`卡号`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 正在导出表  atm.卡内账户 的数据：~55 rows (大约)
DELETE FROM `卡内账户`;
/*!40000 ALTER TABLE `卡内账户` DISABLE KEYS */;
INSERT INTO `卡内账户` (`账户号`, `卡号`, `账户类型`) VALUES
	('1-1043', 1043, '活期'),
	('2-1043', 1043, '定期'),
	('3-1043', 1043, '信用'),
	('ATM', 0, '系统');
/*!40000 ALTER TABLE `卡内账户` ENABLE KEYS */;

-- 导出  表 atm.定期存款 结构
CREATE TABLE IF NOT EXISTS `定期存款` (
  `交易编号` bigint NOT NULL AUTO_INCREMENT,
  `交易时间` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `账户号` varchar(50) NOT NULL DEFAULT '0',
  `存入金额` decimal(20,2) NOT NULL DEFAULT '0.00',
  `到期时间` timestamp NOT NULL,
  `日利率` decimal(20,6) NOT NULL DEFAULT '0.000000',
  `存款状态` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`交易编号`) USING BTREE,
  KEY `FK_定期存款_卡内账户` (`账户号`),
  CONSTRAINT `FK_定期存款_卡内账户` FOREIGN KEY (`账户号`) REFERENCES `卡内账户` (`账户号`),
  CONSTRAINT `FK_定期存款_账户流水` FOREIGN KEY (`交易编号`) REFERENCES `账户流水` (`交易编号`)
) ENGINE=InnoDB AUTO_INCREMENT=160 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 正在导出表  atm.定期存款 的数据：~4 rows (大约)
DELETE FROM `定期存款`;
/*!40000 ALTER TABLE `定期存款` DISABLE KEYS */;
/*!40000 ALTER TABLE `定期存款` ENABLE KEYS */;

-- 导出  表 atm.客户信息 结构
CREATE TABLE IF NOT EXISTS `客户信息` (
  `客户名` tinytext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `身份证号` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `客户状态` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`身份证号`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- 正在导出表  atm.客户信息 的数据：~18 rows (大约)
DELETE FROM `客户信息`;
/*!40000 ALTER TABLE `客户信息` DISABLE KEYS */;
INSERT INTO `客户信息` (`客户名`, `身份证号`, `客户状态`) VALUES
	('TEST', '121212', 0),
	('系统账户', 'ATMsystem', 0);
/*!40000 ALTER TABLE `客户信息` ENABLE KEYS */;

-- 导出  表 atm.账户流水 结构
CREATE TABLE IF NOT EXISTS `账户流水` (
  `交易编号` bigint NOT NULL AUTO_INCREMENT,
  `交易时间` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `账户号` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `交易类型` tinytext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `映射账户` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `映射交易号` bigint DEFAULT NULL,
  `变动金额` decimal(20,2) NOT NULL DEFAULT '0.00',
  `余额` decimal(20,2) NOT NULL DEFAULT '0.00',
  `包含手续费` decimal(20,2) NOT NULL DEFAULT '0.00',
  `交易备注` tinytext,
  PRIMARY KEY (`交易编号`),
  KEY `FK_活期_users` (`账户号`) USING BTREE,
  KEY `FK_活期_users_2` (`映射账户`) USING BTREE,
  KEY `操作时间` (`交易时间`) USING BTREE,
  KEY `FK_账户流水_账户流水` (`映射交易号`),
  CONSTRAINT `FK_账户流水_卡内账户` FOREIGN KEY (`账户号`) REFERENCES `卡内账户` (`账户号`),
  CONSTRAINT `FK_账户流水_卡内账户_2` FOREIGN KEY (`映射账户`) REFERENCES `卡内账户` (`账户号`),
  CONSTRAINT `FK_账户流水_账户流水` FOREIGN KEY (`映射交易号`) REFERENCES `账户流水` (`交易编号`)
) ENGINE=InnoDB AUTO_INCREMENT=224 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 正在导出表  atm.账户流水 的数据：~113 rows (大约)
DELETE FROM `账户流水`;
/*!40000 ALTER TABLE `账户流水` DISABLE KEYS */;
INSERT INTO `账户流水` (`交易编号`, `交易时间`, `账户号`, `交易类型`, `映射账户`, `映射交易号`, `变动金额`, `余额`, `包含手续费`, `交易备注`) VALUES
	(221, '2022-06-22 16:07:42', '1-1043', '开户', 'ATM', NULL, 0.00, 0.00, 0.00, NULL),
	(222, '2022-06-22 16:07:42', '2-1043', '开户', 'ATM', NULL, 0.00, 0.00, 0.00, NULL),
	(223, '2022-06-22 16:07:42', '3-1043', '开户', 'ATM', NULL, 0.00, 0.00, 0.00, NULL);
/*!40000 ALTER TABLE `账户流水` ENABLE KEYS */;

-- 导出  表 atm.银行卡密 结构
CREATE TABLE IF NOT EXISTS `银行卡密` (
  `卡号` bigint NOT NULL AUTO_INCREMENT,
  `密码` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `身份证号` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`卡号`),
  KEY `FK_银行卡密_客户信息` (`身份证号`),
  CONSTRAINT `FK_银行卡密_客户信息` FOREIGN KEY (`身份证号`) REFERENCES `客户信息` (`身份证号`)
) ENGINE=InnoDB AUTO_INCREMENT=1044 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 正在导出表  atm.银行卡密 的数据：~0 rows (大约)
DELETE FROM `银行卡密`;
/*!40000 ALTER TABLE `银行卡密` DISABLE KEYS */;
INSERT INTO `银行卡密` (`卡号`, `密码`, `身份证号`) VALUES
	(0, 'HNUdb', 'ATMsystem'),
	(1043, '111111', '121212');
/*!40000 ALTER TABLE `银行卡密` ENABLE KEYS */;

-- 导出  存储过程 atm.history 结构
DELIMITER //
CREATE PROCEDURE `history`(
	IN `cookie` BIGINT,
	IN `ctype` VARCHAR(2),
	IN `cfrom` TIMESTAMP,
	IN `cto` TIMESTAMP,
	IN `corder` INT,
	IN `sc` int
)
BEGIN
	DECLARE id BIGINT;
	DECLARE acc VARCHAR(50);
	SELECT 卡号 INTO id FROM 临时会话 WHERE 会话号=cookie;
	if id IS NOT NULL then 
		UPDATE 临时会话 SET 会话过期时间 =TIMESTAMPADD(minute,2,now()) WHERE 会话号=cookie;
		SELECT 账户号 into acc FROM 卡内账户 WHERE 卡号=id AND 账户类型=ctype;
		if corder > 0 then 
			if sc =1 then
				SELECT 交易时间,交易类型,卡内账户.`卡号` 发起人或接收方,卡内账户.`账户类型` 发起人或接收方类型,变动金额 , 余额,交易备注 FROM 账户流水,卡内账户 WHERE 账户流水.`账户号` = acc and 卡内账户.`账户号`=账户流水.`映射账户` order BY 交易时间 DESC LIMIT corder;
			ELSE 
				SELECT 交易时间,交易类型,卡内账户.`卡号` 发起人或接收方,卡内账户.`账户类型` 发起人或接收方类型,变动金额 , 余额 ,交易备注 FROM 账户流水,卡内账户 WHERE 账户流水.`账户号` = acc and 卡内账户.`账户号`=账户流水.`映射账户` order BY 交易时间 ASC LIMIT corder;
			END if;
		else
			if sc=1 then 
				SELECT 交易时间,交易类型,卡内账户.`卡号` 发起人或接收方,卡内账户.`账户类型` 发起人或接收方类型,变动金额 , 余额,交易备注  FROM 账户流水,卡内账户 WHERE 账户流水.`账户号` = acc and 卡内账户.`账户号`=账户流水.`映射账户` and (交易时间 BETWEEN cfrom AND cto ) order BY 交易时间 DESC;
			ELSE 
				SELECT 交易时间,交易类型,卡内账户.`卡号` 发起人或接收方,卡内账户.`账户类型` 发起人或接收方类型,变动金额 , 余额,交易备注  FROM 账户流水,卡内账户 WHERE 账户流水.`账户号` = acc and 卡内账户.`账户号`=账户流水.`映射账户` and (交易时间 BETWEEN cfrom AND cto ) order BY 交易时间 ASC;
			END if;
		END if;
	END if;
END//
DELIMITER ;

-- 导出  存储过程 atm.inquiry 结构
DELIMITER //
CREATE PROCEDURE `inquiry`(
	IN `cookie` BIGINT,
	IN `ctype` VARCHAR(2),
	OUT `name` TEXT,
	OUT `balance` DECIMAL(20,2),
	OUT `flex_balance` DECIMAL(20,2)
)
BEGIN
	DECLARE id BIGINT;
	DECLARE day_money DECIMAL(20,2) DEFAULT 0;
	DECLARE acc VARCHAR(50);
	UPDATE 临时会话 SET 会话过期时间 =TIMESTAMPADD(minute,2,now()) WHERE 会话号=cookie;
	SELECT 卡号 INTO id FROM 临时会话 WHERE 会话号=cookie;
	if id IS NOT NULL then 
		SELECT 身份证号 INTO @pid FROM 银行卡密 WHERE 卡号=id;
		SELECT 客户名 INTO name FROM 客户信息 WHERE 身份证号 = @pid;
		SELECT 账户号 INTO acc FROM 卡内账户 WHERE 卡号 = id AND 账户类型 = ctype;
		SELECT 余额 INTO balance FROM 账户流水 WHERE 账户号 =acc ORDER BY 交易时间 DESC LIMIT 1;
		select SUM(变动金额) into day_money FROM 账户流水 WHERE TO_DAYS(交易时间) = TO_DAYS(NOW()) AND 账户号=acc AND 交易类型='取款';
		if day_money IS NULL then
			set day_money = 0;
		END if;
		set flex_balance=5000+day_money ;
		if flex_balance > balance then
			SET flex_balance = balance;
		END IF;
	END if;
END//
DELIMITER ;

-- 导出  存储过程 atm.login 结构
DELIMITER //
CREATE PROCEDURE `login`(
	IN `id` BIGINT,
	IN `pwd` VARCHAR(50),
	OUT `state` INT,
	OUT `cookie` BIGINT
)
BEGIN
  DECLARE sessionid BIGINT DEFAULT (NOW()-20220000000000)*id;
  start transaction; 
  SELECT COUNT(*) INTO state FROM 银行卡密 WHERE 卡号=id AND 密码= AES_DECRYPT(FROM_BASE64(pwd), 'HNUdatabase');
  if state = 1 then
  	INSERT INTO atm.临时会话(卡号,会话号,会话过期时间) VALUES (id,sessionid, TIMESTAMPADD(MINUTE,2,now()));
  	SET cookie := sessionid;
  ELSE 
   SET cookie := 0;
  END if;
  if state IS NULL then 
  	SET state=0;
	END if;
	COMMIT;
END//
DELIMITER ;

-- 导出  存储过程 atm.modify 结构
DELIMITER //
CREATE PROCEDURE `modify`(
	IN `cookie` BIGINT,
	IN `oldpwd` VARCHAR(50),
	IN `newpwd` VARCHAR(50),
	OUT `state` int,
	OUT `info` TEXT
)
BEGIN
	DECLARE id BIGINT;
	start transaction; 
	SELECT 卡号 INTO id FROM 临时会话 WHERE 会话号=cookie;
	if id IS NOT NULL then 
	UPDATE 临时会话 SET 会话过期时间 = TIMESTAMPADD(MINUTE,2,now()) WHERE 会话号=cookie;
		SELECT COUNT(*) INTO state FROM 银行卡密 WHERE 卡号=id AND 密码= AES_DECRYPT(FROM_BASE64(oldpwd), 'HNUdatabase');
		if state = 1 then
		 UPDATE 银行卡密 SET 密码= AES_DECRYPT(FROM_BASE64(newpwd), 'HNUdatabase') WHERE 卡号=id;
		 SET info = '修改成功';
		ELSE 
			SET info = '旧密码错误';
			SET state =0;
		END if;
	END if;
	COMMIT;
END//
DELIMITER ;

-- 导出  存储过程 atm.save 结构
DELIMITER //
CREATE PROCEDURE `save`(
	IN `cookie` BIGINT,
	IN `ctype` VARCHAR(2),
	IN `money` DECIMAL(20,2),
	OUT `state` INT,
	OUT `info` TEXT,
	OUT `balance` DECIMAL(20,2)
)
BEGIN
	DECLARE id BIGINT;
	DECLARE acc VARCHAR(50);
	start transaction; 
	SELECT 卡号 INTO id FROM 临时会话 WHERE 会话号=cookie;
	if id IS NOT NULL then 
	UPDATE 临时会话 SET 会话过期时间 = TIMESTAMPADD(minute,2,now()) WHERE 会话号=cookie;
	SELECT 账户号 INTO acc FROM 卡内账户 WHERE 卡号 = id AND 账户类型 = ctype;
	if ctype = '活期' or ctype = '信用' then 
		SELECT 余额 INTO balance FROM 账户流水 WHERE 账户号 = acc  ORDER BY 交易时间 DESC LIMIT 1;
		SET balance = balance+money;
		INSERT INTO 账户流水(账户号,交易类型,映射账户,变动金额,余额)VALUES	(acc,'存款',acc,money,balance);
		SET state = 1;
		SET info = concat('存款成功！本次存入金额为：¥',money);
	ELSEIF ctype = '定期' then 
		SELECT 余额 INTO balance FROM 账户流水 WHERE 账户号 = acc  ORDER BY 交易时间 DESC LIMIT 1;
		SET balance = balance+money;
		INSERT INTO 账户流水(账户号,交易类型,映射账户,变动金额,余额)VALUES	(acc,'存款',acc,money,balance);
		select 交易编号,交易时间 into @opid,@optime from 账户流水 where 账户号=acc and 交易类型='存款' order by 交易时间 DESC LIMIT 1;
		INSERT INTO 定期存款(交易编号,交易时间,账户号,存入金额,到期时间,日利率)VALUES	(@opid,@optime,acc,money,TIMESTAMPADD(day,30,@optime),0.0001);
		SET state = 1;
		SET info = concat('存款成功！本次存入金额为：¥',money,',定期存款存期1个月(30个自然日)，月利率为0.3%，仅支持整存整取（含利息）');
	END if;
	END if;
	COMMIT;
END//
DELIMITER ;

-- 导出  存储过程 atm.signup 结构
DELIMITER //
CREATE PROCEDURE `signup`(
	IN `name` TINYTEXT,
	IN `pwd` VARCHAR(50),
	IN `pid` BIGINT,
	OUT `id` INT,
	OUT `info` TEXT
)
BEGIN
	DECLARE num INT ;
	DECLARE acc TEXT;
	DECLARE ACCOUNT VARCHAR(50); 
	start transaction; 
	SELECT COUNT(*) INTO num FROM 客户信息 WHERE 身份证号=pid;
	if num > 2 then
		SET id = -1;
		SET info = '开户失败，一位客户最多拥有三张银行卡';
	ELSE 
		if num IS NULL OR num = 0 then
				INSERT INTO 客户信息(客户名,身份证号) VALUES (NAME,pid);
		END if;
		SELECT 客户名 INTO @kehuname FROM 客户信息 WHERE 身份证号=pid;
		if @kehuname = NAME then 	
			insert into 银行卡密(密码,身份证号) values(AES_DECRYPT(FROM_BASE64(pwd), 'HNUdatabase'),pid);
		  	select max(卡号) into id from 银行卡密 WHERE 身份证号=pid;
		  	SET acc = id+'';
	  		INSERT INTO 卡内账户(账户号,卡号,账户类型)VALUES(CONCAT('1-',acc),id,'活期');
		  	INSERT INTO 卡内账户(账户号,卡号,账户类型)VALUES(CONCAT('2-',acc),id,'定期');
		  	INSERT INTO 卡内账户(账户号,卡号,账户类型)VALUES(CONCAT('3-',acc),id,'信用');
		  	SELECT 账户号 INTO ACCOUNT FROM 卡内账户 WHERE 卡号=id AND 账户类型='活期';
		  	INSERT INTO 账户流水(账户号,交易类型,映射账户,变动金额,余额)VALUES(ACCOUNT,'开户','ATM',0,0);
		  	SELECT 账户号 INTO ACCOUNT FROM 卡内账户 WHERE 卡号=id AND 账户类型='定期';
		  	INSERT INTO 账户流水(账户号,交易类型,映射账户,变动金额,余额)VALUES(ACCOUNT,'开户','ATM',0,0);
		  	SELECT 账户号 INTO ACCOUNT FROM 卡内账户 WHERE 卡号=id AND 账户类型='信用';
		  	INSERT INTO 账户流水(账户号,交易类型,映射账户,变动金额,余额)VALUES(ACCOUNT,'开户','ATM',0,0);
	  		SET info = '开户成功，请妥善保管您的卡号和密码，此卡为定活信用一卡通类型，同时带有三个子账户';
  		ELSE 
  			SET id = -1;
  			SET info = '您输入的客户名与身份证信息不匹配，请重新输入。';
  		END if;
  	END if;
  	COMMIT;
END//
DELIMITER ;

-- 导出  存储过程 atm.transfer 结构
DELIMITER //
CREATE PROCEDURE `transfer`(
	IN `cookie` BIGINT,
	IN `to_id` BIGINT,
	IN `stype` VARCHAR(2),
	IN `rtype` VARCHAR(2),
	IN `money` DECIMAL(20,2),
	OUT `state` INT,
	OUT `info` TEXT,
	OUT `balance` DECIMAL(20,2)
)
BEGIN
	DECLARE id BIGINT;
	DECLARE acc varchar(50);
	declare to_acc varchar(50);
	DECLARE rbalance DECIMAL(20,2);
	start transaction; 
	SELECT 卡号 INTO id FROM 临时会话 WHERE 会话号=cookie;
	if id IS NOT NULL then 
	UPDATE 临时会话 SET 会话过期时间 =TIMESTAMPADD(minute,2,now()) WHERE 会话号=cookie;
		if money >10000 then
			set state = -1;
			SET info = '单次转账金额不得超过10000元';
		ELSE 
			SELECT COUNT(*) INTO @ob FROM 银行卡密 WHERE 卡号=to_id;
			if @ob = 0 or @ob is null then
				set state = -2;
				SET info = '转账对方不存在';
			ELSE 
				SELECT 账户号 into acc FROM 卡内账户 WHERE 卡号=id AND 账户类型=stype;
				SELECT 账户号 into to_acc FROM 卡内账户 WHERE 卡号=to_id AND 账户类型=rtype;
				SELECT 余额 INTO balance FROM 账户流水 WHERE 账户号 = acc  ORDER BY 交易时间 DESC LIMIT 1;
				if stype = '活期' or stype = '信用'then
					if balance-(money*1.01) <0 and stype = '活期' then
						set state = -2;
						SET info = '余额不足以扣除转账金额与手续费，手续费率1%';
					elseif balance-(money*1.01) <-2000 and stype = '信用' then
						set state = -2;
						SET info = '透支额度不足以扣除转账金额与手续费，手续费率1%';
					else
						INSERT INTO 账户流水(账户号,交易类型,映射账户,变动金额,余额,包含手续费)VALUES
										(acc,'转出',to_acc,-money*1.01,balance-money*1.01,money*0.01);
						select max(交易编号) into @opid from 账户流水 where 账户号=acc and 交易类型='转出';
						SELECT 余额 INTO @to_balance FROM 账户流水 WHERE 账户号 = to_acc  ORDER BY 交易时间 DESC LIMIT 1;
						INSERT INTO 账户流水(账户号,交易类型,映射账户,映射交易号,变动金额,余额)VALUES
										(to_acc,'转入',acc,@opid,money,@to_balance+money);
						select max(交易编号) into @lastid from 账户流水 where 账户号=to_acc and 交易类型='转入';
						UPDATE 账户流水 SET 映射交易号=@lastid WHERE 交易编号 = @opid;
						if rtype = '定期' then 
							select 交易编号,交易时间 into @opid,@optime from 账户流水 where 账户号=to_acc and 交易类型='转入' order by 交易时间 DESC LIMIT 1;
							INSERT INTO 定期存款(交易编号,交易时间,账户号,存入金额,到期时间,日利率)VALUES	(@opid,@optime,to_acc,money,TIMESTAMPADD(day,30,@optime),0.0001);
						end if;
						set state= 1;
						SET info = '转账成功';
					END if;
				elseif stype ='定期' then
					SELECT 账户号 into @huoqiacc FROM 卡内账户 WHERE 卡号=id AND 账户类型='活期';
					SELECT 余额 INTO @huoqi_balance FROM 账户流水 WHERE 账户号 = @huoqiacc  ORDER BY 交易时间 DESC LIMIT 1;
					if balance-money<0 then
						set state = -2;
						SET info = '余额不足以扣除转账金额';
					elseif money*0.01 > @huoqi_balance then
						set state = -2;
						SET info = '活期账户余额（未结算定期利息）不足以扣除手续费，手续费率1%';
					else
						SELECT COUNT(*) into @match_op from 定期存款 WHERE 存款状态=0 AND 存入金额=money AND 账户号=acc;
						if @match_op is null or @match_op = 0 then
							set state = -2;
							SET info = '您的账户中没有与转账金额匹配的历史存款';
						else 
							SELECT COUNT(*) into @match_op from 定期存款 WHERE 存款状态=0 AND 存入金额=money and 到期时间<now() AND 账户号=acc;
							if @match_op is null or @match_op = 0 then
								select 交易编号 into @match_op from 定期存款 WHERE 存款状态=0 AND 存入金额=money  AND 账户号=acc order by 到期时间 desc limit 1;
								if @huoqi_balance <10 then
										set state = -2;
										SET info = '活期账户余额不足！您的该笔定期存款尚未到期，转出存款需要从活期账户扣除10元手续费';
								else
									UPDATE 定期存款 set 存款状态 = 2 where 交易编号=@match_op;
									insert into 账户流水(账户号,交易类型,映射账户,变动金额,余额,交易备注)VALUES (acc,'转出',to_acc,0-money,balance-money,"转出未到期存款，于活期账户扣除手续费10元");
									select max(交易编号) into @src_opid from 账户流水 where 账户号=acc and 交易类型='转出';
									insert into 账户流水(账户号,交易类型,映射账户,映射交易号,变动金额,余额,包含手续费,交易备注)VALUES (@huoqiacc,'代扣',acc,@src_opid,-10,@huoqi_balance-10,-10,"定期账户转出未到期存款，扣除手续费10元");
									select 余额 INTO @to_balance from 账户流水 where 账户号=to_acc  ORDER BY 交易时间 DESC LIMIT 1;
									INSERT INTO 账户流水(账户号,交易类型,映射账户,映射交易号,变动金额,余额)VALUES (to_acc,'转入',acc,@src_opid,money,@to_balance+money);
									select max(交易编号) into @lastid from 账户流水 where 账户号=to_acc and 交易类型='转入';
									UPDATE 账户流水 SET 映射交易号=@lastid WHERE 交易编号 =@src_opid;
									if rtype = '定期' then 
										select 交易编号,交易时间 into @opid,@optime from 账户流水 where 账户号=to_acc and 交易类型='转入' order by 交易时间 DESC LIMIT 1;
										INSERT INTO 定期存款(交易编号,交易时间,账户号,存入金额,到期时间,日利率)VALUES	(@opid,@optime,to_acc,money,TIMESTAMPADD(day,30,@optime),0.0001);
									end if;
									set state= 1;
									SET info = '转账成功';
								end if;
							else
								SELECT 余额 INTO @dingqi_balance FROM 账户流水 WHERE 账户号 = acc ORDER BY 交易时间 DESC LIMIT 1;
								SELECT 余额 INTO @huoqi_balance FROM 账户流水 WHERE 账户号 = @huoqiacc  ORDER BY 交易时间 DESC LIMIT 1;
								select 交易编号,日利率 into @match_op,@lilv from 定期存款 WHERE 存款状态=0 AND 存入金额=money order by 到期时间 asc limit 1;
								UPDATE 定期存款 set 存款状态 = 1 where 交易编号=@match_op;
								insert into 账户流水(账户号,交易类型,映射账户,变动金额,余额,交易备注)VALUES (acc,'转出',to_acc,-money,@dingqi_balance-money,"转出到期存款，利息另转至活期账户");
								select max(交易编号) into @src_opid from 账户流水 where 账户号=acc and 交易类型='转出';
								insert into 账户流水(账户号,交易类型,映射账户,映射交易号,变动金额,余额,包含手续费,交易备注)VALUES (@huoqiacc,'代扣',@huoqiacc,@src_opid,-money*0.01,@huoqi_balance-money*0.01,-money*0.01,'定期账户转出到期存款，扣除手续费');
								SELECT 余额 INTO @huoqi_balance FROM 账户流水 WHERE 账户号 = @huoqiacc  ORDER BY 交易时间 DESC LIMIT 1;
								insert into 账户流水(账户号,交易类型,映射账户,映射交易号,变动金额,余额)VALUES (@huoqiacc,'定期利息',acc,@src_opid,@lilv*30*money, @huoqi_balance+@lilv*30*money);
								SELECT 余额 INTO @to_balance FROM 账户流水 WHERE 账户号 = to_acc  ORDER BY 交易时间 DESC LIMIT 1;
								INSERT INTO 账户流水(账户号,交易类型,映射账户,映射交易号,变动金额,余额)VALUES (to_acc,'转入',acc,@src_opid,money,@to_balance+money);
								select max(交易编号) into @lastid from 账户流水 where 账户号=to_acc and 交易类型='转入';
								UPDATE 账户流水 SET 映射交易号=@lastid WHERE 交易编号 =@src_opid;
								if rtype = '定期' then 
										select 交易编号,交易时间 into @opid,@optime from 账户流水 where 账户号=to_acc and 交易类型='转入' order by 交易时间 DESC LIMIT 1;
										INSERT INTO 定期存款(交易编号,交易时间,账户号,存入金额,到期时间,日利率)VALUES	(@opid,@optime,to_acc,money,TIMESTAMPADD(day,30,@optime),0.0001);
								end if;
								set state= 1;
								SET info = '转账成功';
							end if;
						end if;
					END if;
					END if;
			END if;
		END if;
	END if;
SELECT 余额 INTO balance FROM 账户流水 WHERE 账户号 = acc  ORDER BY 交易时间 DESC LIMIT 1;
commit; 
END//
DELIMITER ;

-- 导出  存储过程 atm.withdraw 结构
DELIMITER //
CREATE PROCEDURE `withdraw`(
	IN `cookie` BIGINT,
	IN `ctype` VARCHAR(2),
	IN `money` DECIMAL(20,2),
	OUT `state` INT,
	OUT `info` TEXT,
	OUT `balance` DECIMAL(20,2)
)
BEGIN
	DECLARE id BIGINT;
	DECLARE acc VARCHAR(50);
	declare day_money DECIMAL(20,2);
	DECLARE month_times INT;
	start transaction; 
	SELECT 卡号 INTO id FROM 临时会话 WHERE 会话号=cookie;
	if id IS NOT NULL then 
	UPDATE 临时会话 SET 会话过期时间 = TIMESTAMPADD(minute,2,now()) WHERE 会话号=cookie;
	SELECT 账户号 into acc FROM 卡内账户 WHERE 卡号=id AND 账户类型=ctype;
		if money >2000 then
			set state = -1;
			SET info = '单次取款金额不得超过2000元';
		ELSE 
			SELECT SUM(变动金额) into day_money FROM 账户流水 WHERE TO_DAYS(交易时间) = TO_DAYS(NOW()) AND 账户号 = acc AND  交易类型='取款';
			if day_money IS NULL then 
				SET day_money = 0;
			END if;
			if day_money-money<-5000 then
				set state = -2;
				SET info = '单日累计取款金额不得超过5000元';
			else
				SELECT 余额 INTO balance FROM 账户流水 WHERE 账户号 = acc ORDER BY 交易时间 DESC LIMIT 1;
				if ctype = '活期' then
						SELECT COUNT(*) into month_times FROM 账户流水 WHERE DATE_FORMAT(交易时间, '%Y%m') = DATE_FORMAT(NOW(), '%Y%m') AND 账户号 = acc AND  交易类型='取款';														
						if month_times >= 5 then
							if balance-money-2>0 then
								INSERT INTO 账户流水(账户号,交易类型,映射账户,变动金额,余额,包含手续费)VALUES
									(acc,'取款',acc,0-money-2,balance-money-2,-2);
								set state = 2;
								SET info = '取款成功，本月累计取款金额超过5次，收取手续费2元';
							ELSE 
								set state = -2;
								SET info = '您的余额不足以扣除取款金额与手续费之和';
							END if;
						ELSE 
							if balance -money > 0 then
								INSERT INTO 账户流水(账户号,交易类型,映射账户,变动金额,余额)VALUES
									(acc,'取款',acc,0-money,balance-money);
								set state = 1;
								SET info = '取款成功';
							ELSE 
								set state = -2;
								SET info = '您的余额不足以扣除取款金额';
							END if;
						END if;
				ELSEif ctype = '定期' then
					SELECT COUNT(*) into @match_op from 定期存款 WHERE 存款状态=0 AND 存入金额=money AND 账户号=acc;
					if @match_op is null or @match_op = 0 then
						set state = -2;
						SET info = '您的账户中没有与取款金额匹配的未取出历史存款';
					else 
						SELECT COUNT(*) into @match_op from 定期存款 WHERE 存款状态=0 AND 存入金额=money and 到期时间<NOW() AND 账户号=acc;
						if @match_op is null or @match_op = 0 then
							select 交易编号 into @match_op from 定期存款 WHERE 存款状态=0 AND 存入金额=money AND 账户号=acc order by 到期时间 desc limit 1;
							select 账户号 into @huoqi_id from 卡内账户 where 卡号=id and 账户类型='活期';
							SET @dingqib = balance;
							SELECT 余额 INTO balance FROM 账户流水 WHERE 账户号 = @huoqi_id ORDER BY 交易时间 DESC LIMIT 1;
							if balance <10 then
									set state = -2;
									SET info = '活期账户余额不足！您的该笔存款尚未到期，取出存款需要从活期账户扣除10元手续费';
							else
								UPDATE 定期存款 set 存款状态 = 2 where 交易编号=@match_op;
								insert into 账户流水(账户号,交易类型,映射账户,变动金额,余额,交易备注)VALUES (acc,'取款',acc,0-money,@dingqib-money,"取出未到期存款，于活期账户扣除手续费10元");
								select max(交易编号) into @src_opid from 账户流水 where 账户号=acc and 交易类型='取款';
								insert into 账户流水(账户号,交易类型,映射账户,映射交易号,变动金额,余额,包含手续费,交易备注)VALUES (@huoqi_id,'代扣',acc,@src_opid,-10,balance-10,-10,"定期账户取出未到期存款，扣除手续费10元");
								set state = 1;
								SET info = '取款成功，该笔存款尚未到期，已从活期账户中代扣10元手续费。';
							end if;
						else
							SELECT 余额 INTO @dingqib FROM 账户流水 WHERE 账户号 = acc ORDER BY 交易时间 DESC LIMIT 1;
							SELECT 余额 INTO balance FROM 账户流水 WHERE 账户号 = @huoqi_id ORDER BY 交易时间 DESC LIMIT 1;
							select 交易编号,日利率 into @match_op,@lilv from 定期存款 WHERE 存款状态=0 AND 存入金额=money AND 账户号=acc order by 到期时间 asc limit 1;
							UPDATE 定期存款 set 存款状态 = 1 where 交易编号=@match_op;
							insert into 账户流水(账户号,交易类型,映射账户,变动金额,余额,交易备注)VALUES (acc,'取款',acc,0-money,@dingqib-money,"取出到期存款，利息另转至活期账户");
							select 账户号 into @huoqi_id from 卡内账户 where 卡号=id and 账户类型='活期';
							select max(交易编号) into @src_opid from 账户流水 where 账户号=acc and 交易类型='取款';
							insert into 账户流水(账户号,交易类型,映射账户,映射交易号,变动金额,余额)VALUES (@huoqi_id,'定期利息',acc,@src_opid,@lilv*30*money,balance+@lilv*30*money);
							set state = 1;
							SET info = '取款成功,存款利息已取出至活期账户。';
						end if;
					end if;
				ELSEif ctype = '信用' then
					if balance -money< -2000 then
						set state = -2;
						SET info = '取出金额超出可透支额度';
					else
						INSERT INTO 账户流水(账户号,交易类型,映射账户,变动金额,余额)VALUES
									(acc,'取款',acc,0-money,balance-money);
						set state = 1;
						SET info = '取款成功';
					END if;
					END if;
				END if;
			END if;
		END if;
		SELECT 余额 INTO balance FROM 账户流水 WHERE 账户号 = acc ORDER BY 交易时间 DESC LIMIT 1;
		commit; 
END//
DELIMITER ;

-- 导出  事件 atm.clean_session 结构
DELIMITER //
CREATE EVENT `clean_session` ON SCHEDULE EVERY 1 MINUTE STARTS '2022-05-15 10:27:32' ON COMPLETION PRESERVE ENABLE DO DELETE FROM 临时会话 WHERE 会话过期时间 < NOW()//
DELIMITER ;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

-- all properties
SELECT pid, zip, address, bed, bath, square, bdate, bid, water, bus, subway, start, listprice, evalprice, taxde, maintenancefee, aid FROM properties_all P WHERE P.sale = true

-- featured properties
SELECT pid, zip, address, bed, bath, square, bdate, bid, water, bus, subway, start, listprice, evalprice, taxde, maintenancefee, aid FROM (SELECT * FROM properties_all P WHERE P.sale = true) P WHERE P.pid = 'prpt23' OR P.pid = 'prpt723' OR P.pid = 'prpt230' OR P.pid = 'prpt323'





INSERT INTO Properties VALUES('prpt1','10457','4354 PARK AVENUE','2','1','2316','1899','blk1');
INSERT INTO Lists VALUES('agnt1','prpt1');
INSERT INTO Owners VALUES('325-01-5646','Daniel','Franklin');
INSERT INTO Blongs VALUES('237-72-7053','prpt493');
INSERT INTO States(st_start,prpt_id) VALUES(to_date('12/04/2016', 'MM/DD/YYYY'),'prpt23');
INSERT INTO Prices VALUES('590200',NULL,'766100','FALSE','310','prpt23');

DELETE FROM prices p WHERE prpt_id = 'prpt731' OR prpt_id = 'prpt732' OR prpt_id = 'prpt733' OR prpt_id = 'prpt734';
DELETE FROM States s WHERE prpt_id = 'prpt731' OR prpt_id = 'prpt732' OR prpt_id = 'prpt733' OR prpt_id = 'prpt734';
DELETE FROM blongs B WHERE prpt_id = 'prpt731' OR prpt_id = 'prpt732' OR prpt_id = 'prpt733' OR prpt_id = 'prpt734';
DELETE FROM lists L WHERE prpt_id = 'prpt731' OR prpt_id = 'prpt732' OR prpt_id = 'prpt733' OR prpt_id = 'prpt734';
DELETE FROM properties P WHERE P.prpt_id = 'prpt731' OR prpt_id = 'prpt732' OR prpt_id = 'prpt733' OR prpt_id = 'prpt734';
DELETE FROM owners O WHERE O.onr_ssn = '111-11-1111' OR onr_ssn ='111-11-1111(1)';
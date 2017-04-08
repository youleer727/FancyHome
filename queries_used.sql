DROP VIEW agents_all, agents_t, agents_f, agents_tf, properties_all;

-- create view of all_properties infomation
CREATE VIEW properties_all AS
SELECT P.prpt_id AS pid,
P.prpt_zip AS zip,
P.prpt_address AS address,
P.prpt_bed AS bed,
P.prpt_bath AS bath,
CAST(P.prpt_square AS INT) AS square,
P.prpt_bdate AS	bdate,
P.blk_id AS bid,
B.blk_water	AS water,
B.blk_bus AS bus,
B.blk_subway AS subway,
T.st_start AS start,
T.st_end AS closed,
T.st_sale AS sale,
R.pr_list AS listprice,
R.pr_sold AS soldprice,
R.pr_eval AS evalprice,
R.pr_taxde AS taxde,
R.pr_maint AS maintenancefee,
L.agnt_id AS aid,
A.agnt_tel AS atel,
A.agnt_email AS aemail,
A.agnt_fname AS afname,
A.agnt_lname AS alname,
N.onr_ssn AS ossn,
O.onr_fname AS ofname,
O.onr_lname AS olname
FROM properties P, blocks B, states T, prices R, lists L, agents A, blongs N, owners O
WHERE P.prpt_id = R.prpt_id AND 
R.prpt_id = T.prpt_id AND 
P.blk_id = B.blk_id AND 
P.prpt_id = L.prpt_id AND 
A.agnt_id = L.agnt_id AND 
P.prpt_id = N.prpt_id AND 
N.onr_ssn = O.onr_ssn;

CREATE VIEW agents_tf AS
SELECT A.agnt_id, 
A.agnt_fname ||' '|| A.agnt_lname AS fullname,
A.agnt_tel AS tel,
A.agnt_email AS email,
COUNT(pid) AS pall,
MAX(listprice) AS maxlpr,
MIN(listprice) AS minlpr,
AVG(listprice) AS avglpr,
MAX(soldprice) AS maxspr,
MIN(soldprice) AS minspr,
AVG(soldprice) AS avgspr,
MAX(evalprice) AS maxepr,
MIN(evalprice) AS minepr,
AVG(evalprice) AS avgepr
FROM agents A LEFT JOIN properties_all P ON A.agnt_id = P.aid
GROUP BY A.agnt_id, A.agnt_fname, A.agnt_lname, A.agnt_email
ORDER BY pall DESC;

CREATE VIEW agents_t AS
SELECT A.agnt_id, 
COUNT(pid) AS psale
FROM agents A LEFT JOIN (SELECT * FROM properties_all P WHERE P.sale = true) P ON A.agnt_id = P.aid
GROUP BY A.agnt_id, A.agnt_fname, A.agnt_lname, A.agnt_email
ORDER BY psale DESC;

CREATE VIEW agents_f AS
SELECT A.agnt_id, 
COUNT(pid) AS psold
FROM agents A LEFT JOIN (SELECT * FROM properties_all P WHERE P.sale = false) P ON A.agnt_id = P.aid
GROUP BY A.agnt_id, A.agnt_fname, A.agnt_lname, A.agnt_email
ORDER BY psold DESC;

-- CREATE VIEW agents_all AS
-- SELECT 
-- A.agnt_id, 
-- A.fullname,
-- A.tel,
-- A.email,
-- A.pall,
-- A1.psale,
-- A2.psold,
-- A.maxlpr,
-- A.minlpr,
-- A.avglpr,
-- A.maxspr,
-- A.minspr,
-- A.avgspr,
-- A.maxepr,
-- A.minepr,
-- A.avgepr
-- FROM agents_tf AS A, agents_t AS A1, agents_f AS A2
-- WHERE A.agnt_id = A1.agnt_id and A.agnt_id = A2.agnt_id;

CREATE VIEW agents_all AS
SELECT 
A.agnt_id, 
A.fullname,
A.tel,
A.email,
A.pall,
A1.psale,
A2.psold,
A.maxlpr,
A.minlpr,
ROUND(A.avglpr) AS avglpr,
A.maxspr,
A.minspr,
ROUND(A.avgspr) AS avgspr,
A.maxepr,
A.minepr,
ROUND(A.avgepr) AS avgepr
FROM agents_tf AS A, agents_t AS A1, agents_f AS A2
WHERE A.agnt_id = A1.agnt_id and A.agnt_id = A2.agnt_id;

P.ossn, P.ofname ||' '|| P.olname AS fullname



-- Update Some Data
UPDATE lists
SET agnt_id = 'agnt1'
WHERE prpt_id = 'prpt40';

UPDATE lists
SET agnt_id = 'agnt2'
WHERE prpt_id = 'prpt84';

DELETE FROM prices p WHERE prpt_id = 'prpt731' OR prpt_id = 'prpt732' OR prpt_id = 'prpt733' OR prpt_id = 'prpt734';
DELETE FROM States s WHERE prpt_id = 'prpt731' OR prpt_id = 'prpt732' OR prpt_id = 'prpt733' OR prpt_id = 'prpt734';
DELETE FROM blongs B WHERE prpt_id = 'prpt731' OR prpt_id = 'prpt732' OR prpt_id = 'prpt733' OR prpt_id = 'prpt734';
DELETE FROM lists L WHERE prpt_id = 'prpt731' OR prpt_id = 'prpt732' OR prpt_id = 'prpt733' OR prpt_id = 'prpt734';
DELETE FROM properties P WHERE P.prpt_id = 'prpt731' OR prpt_id = 'prpt732' OR prpt_id = 'prpt733' OR prpt_id = 'prpt734';
DELETE FROM owners O WHERE O.onr_ssn = '111-11-1111' OR onr_ssn ='111-11-1111(1)';




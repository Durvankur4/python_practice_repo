
---

## 🧩 I. SQL BASICS (Q2 – Q13)

### 1️⃣ Basic SQL Components

|Concept|Description|Important Points|
|:--|:--|:--|
|**Database**|A collection of related tables.|Use `CREATE DATABASE name;`|
|**Table**|Collection of rows (records) and columns (attributes).|Define using `CREATE TABLE`.|
|**Primary Key**|Unique identifier for each record.|Must be unique and `NOT NULL`.|
|**Foreign Key**|Links two tables.|References primary key of another table.|
|**Data Types**|Types of values a column can hold.|Examples: `INT`, `VARCHAR(50)`, `DATE`, `DECIMAL(10,2)`|

---

### 2️⃣ Data Manipulation Commands

|Command|Purpose|Syntax Example|
|:--|:--|:--|
|`SELECT`|Retrieve data.|`SELECT * FROM table_name;`|
|`INSERT`|Add new data.|`INSERT INTO emp VALUES (1,'Amit','Sales');`|
|`UPDATE`|Modify data.|`UPDATE emp SET salary=salary*1.1 WHERE deptno=10;`|
|`DELETE`|Remove data.|`DELETE FROM emp WHERE ename='Ravi';`|

---

### 3️⃣ Filtering & Sorting

|Concept|Example|Tips|
|:--|:--|:--|
|**WHERE**|`SELECT * FROM emp WHERE deptno=10;`|Filters rows|
|**LIKE**|`WHERE ename LIKE 'A%';`|`%` = any string, `_` = one char|
|**ORDER BY**|`ORDER BY salary DESC;`|Sort ascending (`ASC`) or descending (`DESC`)|

---

### 4️⃣ Aggregation & Grouping

|Function|Description|Example|
|:--|:--|:--|
|`COUNT()`|Number of rows.|`SELECT COUNT(*) FROM emp;`|
|`AVG()`|Average value.|`SELECT AVG(salary) FROM emp;`|
|`SUM()`|Total sum.|`SELECT SUM(salary) FROM emp;`|
|`MIN()` / `MAX()`|Min/max value.|`SELECT MAX(salary) FROM emp;`|
|**GROUP BY**|Group rows by column.|`SELECT deptno, AVG(salary) FROM emp GROUP BY deptno;`|
|**HAVING**|Filter grouped results.|`HAVING AVG(salary)>3000`|

🔹 **Important**:

- `WHERE` filters rows _before grouping_.
- `HAVING` filters _after grouping_.

---

### 5️⃣ Joins

| Type           | Purpose                                    | Example                                                                   |
| :------------- | :----------------------------------------- | :------------------------------------------------------------------------ |
| **INNER JOIN** | Returns rows that match in both tables.    | `SELECT e.ename, d.deptname FROM emp e JOIN dept d ON e.deptno=d.deptno;` |
| **LEFT JOIN**  | All rows from left + matched from right.   |                                                                           |
| **RIGHT JOIN** | All rows from right + matched from left.   |                                                                           |
| **FULL JOIN**  | All rows when a match exists in one table. | _(Not in MySQL directly)_                                                 |

🔹 **Tip:** Most DBMS practicals need INNER JOIN.

---

### 6️⃣ Views & Indexes

|Concept|Purpose|Syntax|
|:--|:--|:--|
|**View**|Virtual table based on query.|`CREATE VIEW emp_dept AS SELECT ename,deptno FROM emp;`|
|**Index**|Improves query performance.|`CREATE INDEX idx_salary ON emp(salary);`|

🟩 **Important:**

- Index speeds up `SELECT` but slows down `INSERT`/`UPDATE`.
- Views don’t store data, they reference other tables.

---

### 7️⃣ Subqueries (Nested Queries)

Example:

```
SELECT ename
FROM emp
WHERE salary > (SELECT AVG(salary) FROM emp);
```

🔹 Inner query runs first. 🔹 Use for “greater than average”, “not in list”, etc.

---

### 8️⃣ SQL Practice Focus

Common question themes:

- `MAX`, `AVG`, `SUM`
- `LIKE`, `BETWEEN`, `IN`
- Joins (Employee–Department)
- Updating data with conditions
- Creating Views or Indexes

---

## ⚙️ II. PL/SQL (Q14 – Q17)

### 1️⃣ PL/SQL Structure

```
DECLARE
-- variable declarations
BEGIN
-- executable statements
EXCEPTION
-- error handling
END;
```

🟩 **Important Keywords:**

|Keyword|Meaning|
|:--|:--|
|`DECLARE`|Define variables & cursors.|
|`BEGIN`|Start execution block.|
|`EXCEPTION`|Handle runtime errors.|
|`END`|Block termination.|

---

### 2️⃣ Variables

Variable declaration examples: `v_salary NUMBER(7,2);` `v_name VARCHAR2(20);`

Use `:=` for assignment: `v_salary := 5000;`

---

### 3️⃣ Control Structures

|Structure|Example|Usage|
|:--|:--|:--|
|**IF**|`IF v_att<75 THEN ...`|Conditional logic|
|**LOOP / FOR / WHILE**|`FOR i IN 1..10 LOOP ... END LOOP;`|Repetition|
|**CASE**|`CASE WHEN salary>5000 THEN ... END CASE;`|Multiple conditions|

---

### 4️⃣ Exception Handling

Standard exception handling:

```
EXCEPTION
WHEN NO_DATA_FOUND THEN
DBMS_OUTPUT.PUT_LINE('Record not found');
WHEN OTHERS THEN
DBMS_OUTPUT.PUT_LINE('Error occurred');
```

🟩 Create **user-defined exceptions**: `ex_invalid_balance EXCEPTION;` `RAISE ex_invalid_balance;`

---

### 5️⃣ Cursors

Cursors are used to **fetch multiple rows** into variables.

#### a) Implicit Cursor

- Automatically created for `SELECT INTO`, `UPDATE`, etc.
- Use attributes: `%FOUND`, `%NOTFOUND`, `%ROWCOUNT`.

#### b) Explicit Cursor

- Used when processing multiple rows manually.

```
DECLARE
CURSOR c_emp IS SELECT ename, salary FROM emp;
BEGIN
OPEN c_emp;
LOOP
FETCH c_emp INTO v_name, v_sal;
EXIT WHEN c_emp%NOTFOUND;
...
END LOOP;
CLOSE c_emp;
END;
```

#### c) Parameterized Cursor

```
CURSOR c1(dno NUMBER) IS
SELECT * FROM emp WHERE deptno=dno;
```

---

## 🧨 III. TRIGGERS (Q18)

### 🔹 What are Triggers?

Blocks of code that execute **automatically** on certain table actions.

### 🔹 Types:

|Type|Fires When|
|:--|:--|
|**BEFORE INSERT/UPDATE/DELETE**|Before modification|
|**AFTER INSERT/UPDATE/DELETE**|After modification|
|**ROW LEVEL**|For each row|
|**STATEMENT LEVEL**|Once per statement|

### 🔹 Syntax:

```
CREATE OR REPLACE TRIGGER trig_name
BEFORE UPDATE ON emp
FOR EACH ROW
BEGIN
IF :NEW.salary < 50000 THEN
RAISE_APPLICATION_ERROR(-20001,'Salary too low');
END IF;
END;
```

🟩 Important:

- `:OLD` → data before change
- `:NEW` → data after change
- Can be used to log changes to an **audit table**.

---

## 🍃 IV. MongoDB (Q19 – Q24)

### 1️⃣ Database & Collection

```
use BSIOTR
db.createCollection("Teachers")
```

### 2️⃣ Insert Data

```
db.Teachers.insert({Tname:"Rajesh", dname:"COMP", salary:25000})
```

### 3️⃣ Find Data

|Query|Example|
|:--|:--|
|Find all|`db.Teachers.find()`|
|With condition|`db.Teachers.find({salary:{$gte:10000}})`|
|OR condition|`db.Teachers.find({$or:[{dname:"COMP"},{dname:"IT"}]})`|
|Pretty print|`.pretty()`|

---

### 4️⃣ Update & Delete

Update command example: `db.Teachers.update({Tname:"Praveen"},{$set:{experience:10}}, {upsert:true})`

Delete command example: `db.Teachers.remove({dname:"IT"})`

### 5️⃣ Index

Creating an index: `db.Teachers.createIndex({salary:1})`

Viewing indexes: `db.Teachers.getIndexes()`

### 6️⃣ Aggregation

```
db.Teachers.aggregate([{$group:{_id:"$dname", avgSalary:{$avg:"$salary"}}}])
```

🟩 **Important operators:** `$gt`, `$lt`, `$gte`, `$lte`, `$and`, `$or`, `$in`, `$exists`

---

## 🧠 V. MapReduce (Q25 – Q27)

### 1️⃣ Concept

Used for **data summarization** (like group by but programmable).

- **map()**: Emits key-value pairs.
- **reduce()**: Combines results by key.

### 2️⃣ Syntax Example

```
var mapFn = function() {
emit(this.gender, 1);
};
var reduceFn = function(key, values) {
return Array.sum(values);
};
db.users.mapReduce(mapFn, reduceFn, {out:"gender_count"});
```

### 3️⃣ Common Use Cases

- Count males/females
- Count users by hobby
- Total population per state
- Classify books into “Small” and “Big”

🟩 **Important Concepts**

- Always emit a key for grouping.
- The output collection (`out`) stores final result.
- MapReduce can be replaced by **aggregate()** for performance.

---

## ⚡ WHAT EXTRA KNOWLEDGE HELPS YOU STAND OUT

### 1️⃣ **ER Model Basics**

You don’t need to design full diagrams, but know these:

- **Entity** → real-world object (e.g., Employee, Department)
    
- **Attribute** → property (e.g., Emp_name, DeptNo)
    
- **Relationship** → link between entities (e.g., Works_In)
    
- Cardinality → One-to-One, One-to-Many, Many-to-Many
    

🔹 _Why it helps:_ Many practicals start with table creation, and ER understanding helps define primary & foreign keys correctly.

---

### 2️⃣ **Normalization (Quick Overview)**

- **1NF** – No repeating groups
    
- **2NF** – No partial dependency (full dependency on PK)
    
- **3NF** – No transitive dependency
    
- **BCNF** – Stronger form of 3NF
    

🔹 _Why it helps:_ Sometimes viva or theory questions ask:  
“Why is normalization important?” → _It reduces redundancy and improves consistency._

---

### 3️⃣ **Transaction & Integrity Concepts**

Just know these terms:

|Concept|Meaning|
|---|---|
|**ACID**|Atomicity, Consistency, Isolation, Durability|
|**Commit**|Save changes permanently|
|**Rollback**|Undo recent changes|
|**Constraints**|Enforce rules (`PRIMARY KEY`, `NOT NULL`, `UNIQUE`, `FOREIGN KEY`, `CHECK`)|

🔹 _Why it helps:_ Triggers and exception blocks often deal with transactional control.

---

### 4️⃣ **Basic MongoDB Shell Knowledge**

Know how to:

- Show databases: `show dbs`
    
- Use database: `use db_name`
    
- Show collections: `show collections`
    
- Drop collection: `db.collection.drop()`
    
- Use comparison operators: `$gt`, `$lt`, `$eq`, `$ne`
    

🔹 _Why it helps:_ In viva, examiners often ask you to explain commands.

---

### 5️⃣ **Syntax Confidence**

Examiners often test how confidently you write:

- `CREATE TABLE`, `ALTER TABLE`
    
- `INSERT`, `UPDATE`, `DELETE`
    
- Joins with proper aliases
    
- PL/SQL structure with correct semicolons and `END;`
    

So, before your exam:

> 🔹 Practice 5 random queries _fully written by hand_ once.  
> 🔹 Ensure you remember a few column names logically (e.g., Emp_id, Emp_name, Salary).

---

### 6️⃣ **Short Explanations (for Viva)**

Prepare **one-line answers** like:

- **Trigger:** "It automatically runs on data modification events."
    
- **Cursor:** "Used to process multiple rows one by one in PL/SQL."
    
- **View:** "A virtual table based on a query."
    
- **Normalization:** "Process of organizing data to reduce redundancy."
    
- **MapReduce:** "Divides tasks into map and reduce for parallel processing."
    

Examiners love short, crisp definitions.

---

### 7️⃣ **Optional (if you want to go beyond)**

- **Stored Procedure vs Function** (used in Q13 sometimes)
    
- **JOIN vs Subquery** difference
    
- **Index types** – single field, composite, unique
    
- **Aggregations in MongoDB** – `$group`, `$match`, `$sum`, `$avg`
    

---

## 🎯 SUMMARY TABLE

|Area|Need for Practical|Bonus Knowledge|
|---|---|---|
|SQL Queries|✅ Essential|Add basic join theory|
|PL/SQL|✅ Essential|Learn exception keywords|
|Triggers|✅ Essential|Know :NEW and :OLD clearly|
|MongoDB|✅ Essential|Learn 2–3 aggregation queries|
|MapReduce|⚪ Optional|Just basic map/reduce logic|
|ER & Normalization|⚪ Optional|For viva confidence|
|Transaction Control|⚪ Optional|Know commit/rollback meaning|

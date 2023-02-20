import python

// GET LOCATION OF <ALL> DIFF STATEMENTS - AugAssign | Return | AssignStmt
// Stored in assignstmt.csv

from Function func, Stmt stmt, AssignStmt ass
where
(stmt instanceof AssignStmt) and
ass = stmt and
stmt.getLocation().getFile() = func.getLocation().getFile()
select stmt.getLocation().toString()
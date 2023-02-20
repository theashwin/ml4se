import python

// If -> AssignStmt -> dataflow.csv
from Function func, Stmt stmt, AssignStmt ass
where
(stmt instanceof AssignStmt) and
ass = stmt and
ass.getParentNode() instanceof If and
stmt.getLocation().getFile() = func.getLocation().getFile() and
ass.getTargets().getAnItem().getLocation() = ass.getAChildNode().getLocation()
// LOCATION OF PARENT IF, LOCATION OF STMT, LEFT ASSIGMENT, RIGHT ASSIGNMENT
select ass.getParentNode().getLocation().toString(), stmt.getLocation().toString(), ass.getTargets().getAnItem().toString(), ass.getAChildNode().toString(), ass
